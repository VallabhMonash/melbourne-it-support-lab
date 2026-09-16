#!/usr/bin/env python3
"""Validate the planning repository, not the live IT environment. Stdlib only."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def read_json(relative):
    try:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        ERRORS.append(f"{relative}: {error}")
        return {}


def evidence_exists(relative, owner):
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT / "evidence"),
            f"{owner}: evidence must be a repository evidence/ path: {relative}")
    require(path.is_file() and path.name not in {".gitkeep", "README.md"},
            f"{owner}: missing or placeholder evidence: {relative}")


def main():
    config = read_json("config/lab-plan.json")
    requirements = read_json("tracking/requirements.json").get("requirements", [])
    scenarios = read_json("tracking/scenarios.json").get("scenarios", [])
    targets = config.get("targets", {})

    rids = [r.get("id") for r in requirements]
    sids = [s.get("id") for s in scenarios]
    require(len(rids) == len(set(rids)), "Duplicate requirement ID")
    require(len(sids) == len(set(sids)), "Duplicate scenario ID")
    require(len(requirements) == targets.get("core_requirements") == 26,
            "Core requirement denominator must remain 26")
    require(len(scenarios) == targets.get("total_scenarios") == 32,
            "Core scenario denominator must remain 32")
    for phase, rcount, scount in [("local", 21, 24), ("cloud", 5, 8)]:
        require(sum(r.get("phase") == phase for r in requirements) == rcount,
                f"Expected {rcount} {phase} requirements")
        require(sum(s.get("phase") == phase for s in scenarios) == scount,
                f"Expected {scount} {phase} scenarios")

    requirement_states = {"not_started", "guided", "demonstrated", "blocked"}
    scenario_states = {"not_started", "in_progress", "blocked", "passed"}
    for r in requirements:
        rid = r.get("id", "<missing>")
        require(r.get("status") in requirement_states, f"{rid}: invalid state")
        require(r.get("phase") in {"local", "cloud"}, f"{rid}: invalid phase")
        require(bool(r.get("scenario_ids")), f"{rid}: no scenario mapping")
        for sid in r.get("scenario_ids", []):
            require(sid in sids, f"{rid}: unknown scenario {sid}")
        if r.get("status") in {"guided", "demonstrated"}:
            require(bool(r.get("evidence")), f"{rid}: evidence required")
        if r.get("status") == "demonstrated":
            require(bool(r.get("independent_repeat", "").strip()),
                    f"{rid}: independent-repeat record required")
        if r.get("status") == "blocked":
            require(bool(r.get("notes", "").strip()), f"{rid}: blocker reason required")
        for path in r.get("evidence", []):
            evidence_exists(path, rid)

    for s in scenarios:
        sid = s.get("id", "<missing>")
        require(s.get("status") in scenario_states, f"{sid}: invalid state")
        require(s.get("phase") in {"local", "cloud"}, f"{sid}: invalid phase")
        for field in ["title", "milestone", "mode", "symptom", "setup",
                      "diagnostics", "success", "cleanup"]:
            require(bool(s.get(field)), f"{sid}: missing {field}")
        for rid in s.get("requirement_ids", []):
            require(rid in rids, f"{sid}: unknown requirement {rid}")
        if s.get("status") == "passed":
            require(bool(s.get("evidence")), f"{sid}: passed without evidence")
        if s.get("status") == "blocked":
            require(bool(s.get("notes", "").strip()), f"{sid}: blocker reason required")
        for path in s.get("evidence", []):
            evidence_exists(path, sid)

    # Architecture invariants: prevent accidental third Windows VM or host crossover.
    vms = config.get("vms", [])
    lenovo_vms = [vm for vm in vms if vm.get("host") == "lenovo"]
    require(len(lenovo_vms) == 2, "Plan must have two simultaneous Lenovo VMs")
    require(sum(vm.get("ram_gb", 0) for vm in lenovo_vms) <= 8,
            "Initial Lenovo VM RAM allocation exceeds 8 GB")
    for vm in vms:
        expected_arch = "x64" if vm.get("host") == "lenovo" else "arm64"
        require(vm.get("architecture") == expected_arch,
                f"{vm.get('name')}: wrong architecture for host")
        require(vm.get("disk_allocation") == "dynamic",
                f"{vm.get('name')}: disk must grow dynamically")
    network = config.get("network", {})
    require(network.get("mode") == "natnetwork", "Local phase requires NAT Network")
    require(network.get("virtualbox_dhcp") is False, "Disable VirtualBox DHCP")
    require(network.get("bridged") is False, "No bridged lab network in v1")
    require(network.get("domain_client_dns") == [network.get("dc_ip")],
            "Domain client must use DC01 DNS only")
    ws = next((vm for vm in vms if vm.get("name") == "WS01"), {})
    require(ws.get("cloud_is_additional_vm") is False,
            "CLD01 must reuse WS01 instead of adding a disk")

    # Check relative file links outside fenced examples; external URLs are not fetched.
    md_files = [p for p in ROOT.rglob("*.md")
                if not any(part in {".git", ".local", ".venv", "node_modules"}
                           for part in p.relative_to(ROOT).parts)]
    for path in md_files:
        content = path.read_text(encoding="utf-8")
        content = re.sub(r"```.*?```", "", content, flags=re.S)
        for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
            link = raw.strip().strip("<>")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = unquote(link.split("#", 1)[0])
            if target:
                require((path.parent / target).exists(),
                        f"{path.relative_to(ROOT)}: broken local link {raw}")

    # Catalogue must contain every fixed case and the readable matrix every skill.
    catalogue = (ROOT / "docs/06-scenario-catalogue.md").read_text(encoding="utf-8")
    matrix = (ROOT / "docs/12-requirements-matrix.md").read_text(encoding="utf-8")
    for sid in sids:
        require(f"## {sid} —" in catalogue, f"Catalogue missing {sid}")
    for rid in rids:
        require(f"| {rid} |" in matrix, f"Readable matrix missing {rid}")

    if ERRORS:
        print("Repository validation FAILED:")
        for message in ERRORS:
            print(f"- {message}")
        return 1
    demonstrated = sum(r["status"] == "demonstrated" for r in requirements)
    guided = sum(r["status"] == "guided" for r in requirements)
    passed = sum(s["status"] == "passed" for s in scenarios)
    print(f"Repository validation passed: {len(md_files)} Markdown files, "
          f"{len(requirements)} requirements, {len(scenarios)} scenarios.")
    print(f"Recorded skills: {demonstrated}/26 demonstrated "
          f"({demonstrated / 26:.1%}); {guided} guided.")
    print(f"Recorded cases: {passed}/32 passed. Live lab was NOT tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
