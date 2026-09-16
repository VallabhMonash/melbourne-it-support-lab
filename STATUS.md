# Project status

Last updated: 2026-09-16 (Australia/Melbourne).

## Current position

**Planning package complete. Lab implementation not started.** No VM installation, cloud enrolment or ticket resolution has been verified.

| Milestone | State | Evidence |
|---|---|---|
| Design and repository scaffold | Complete | This planning package; repository integrity checks |
| M0 — Preflight | Not started | None |
| M1 — Windows foundation | Not started | None |
| M2 — Accounts, files and baseline | Not started | None |
| M3 — GLPI service desk | Not started | None |
| M4 — Endpoint operations and recovery | Not started | None |
| M5 — Local support cases and skill assessment | Not started | None |
| M6 — Microsoft 365 and Intune | Not started | None |
| M7 — Portfolio release | Not started | None |

## Known facts supplied by the owner

- Main goal: junior/Level 1 IT support in Melbourne, not cloud engineering or matching a single ad.
- Background: Master of IT, programming and backend cloud experience; little relevant support practice.
- Lenovo: Intel i5-1135G7, 16 GB RAM, x64, Windows 11 Home Single Language.
- VirtualBox: last reported 7.0.20 r163906; update was advised but is unverified.
- VMware Workstation 17 Player is also installed; VirtualBox remains the selected platform.
- Lenovo had 116 GB free; uninstalling Anaconda recovered approximately 50 GB. **About 166 GB free is an estimate, not a fresh measurement.**
- Mac: MacBook Air M3, 16 GB RAM, 512 GB SSD capacity. Free space and macOS version unknown.
- Workspace was empty and was not a Git repository when planning began. A remote repository has not been created or published by this assistant.

## Next action

Start M0. Record actual free space on both machines, BIOS/Task Manager virtualisation status on Lenovo, Windows/macOS build versions, current VirtualBox version, home/VPN subnet overlap and the location for lab files. Use templates/environment-record.md and save the sanitised result under evidence/builds/.

## Remaining implementation gates

1. Mac needs room for a 24 GB growing HELP01 disk plus host headroom; target at least 60 GB free before installation.
2. Lenovo needs at least 30 GB host free space preserved throughout; actual VM footprints determine feasibility.
3. Verify supported VirtualBox release and Windows VM firmware/TPM configuration on the real Lenovo.
4. Endpoint Central Cloud Free account/feature access must be confirmed at M4; do not assume a trial is already a permanent free edition.
5. Microsoft 365 Business Premium trial eligibility, included services and billing terms must be confirmed only when M6 is ready.
6. No managed Apple device, Google Workspace domain or Jamf access is assumed.

## Session log

| Date | Work completed | Verification | Next step |
|---|---|---|---|
| 2026-09-16 | Finalised design, stage gates, scenario/requirement records and handover files | Repository checks only; no live lab checks | M0 preflight |

## Planning validation

The repository validator passed with all 26 requirements and 32 scenarios in their initial states. Local Markdown links and JSON/configuration invariants were checked. Requirement-to-scenario mappings were also checked for consistency. This validates the planning package only; actual guest compatibility, service reachability, performance and account eligibility still need the M0–M6 checks.
