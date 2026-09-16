# Project status

Last updated: 2026-09-17 (Australia/Melbourne).

## Current position

**M0 host preflight complete. M1 has not started.** No project VM, virtual network, cloud enrolment, or ticket resolution has been created or verified.

| Milestone | State | Evidence |
|---|---|---|
| Design and repository scaffold | Complete | This planning package; repository integrity checks |
| M0 — Preflight | Complete | [Host preflight record](evidence/builds/environment.md) |
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
- VirtualBox: updated and owner-verified as 7.2.16r174877; the existing powered-off VM remained registered.
- VMware Workstation 17 Player is also installed; VirtualBox remains the selected platform.
- Lenovo: Windows reported 15.8 GB usable RAM and 181.6 GB free on C: during M0. Task Manager reported virtualisation enabled; `systeminfo.exe` detected an active Windows hypervisor.
- Mac: MacBook Air M3, 16 GB RAM, 512 GB SSD capacity; macOS 26.6.2 build 25G83; 75 GiB free after cleanup.
- Repository: branch `main` tracks `origin/main`. Remote publication was performed outside this M0 implementation session.

## Next action

Wait for the owner's next instruction and restored working permissions. Then start M1 on the LENOVO HOST by creating and validating the `ITSUPPORT-LAB` VirtualBox NAT Network. Do not download or install a guest OS until that network checkpoint passes.

## Remaining implementation gates

1. Preserve at least 30 GB free on each host throughout implementation; measure actual VM footprints rather than relying on configured limits.
2. Verify Windows guest firmware, virtual TPM, Secure Boot, boot, and performance on the real Lenovo during M1.
3. Repeat the `10.77.0.0/24` conflict check if a VPN that installs routes is connected during lab work.
4. Select a HELP01 VM directory outside the repository and synchronised folders before M3; UTM remains intentionally uninstalled.
5. Endpoint Central Cloud Free account/feature access must be confirmed at M4; do not assume a trial is already a permanent free edition.
6. Microsoft 365 Business Premium trial eligibility, included services and billing terms must be confirmed only when M6 is ready.
7. No managed Apple device, Google Workspace domain, or Jamf access is assumed.

## Session log

| Date | Work completed | Verification | Next step |
|---|---|---|---|
| 2026-09-16 | Finalised design, stage gates, scenario/requirement records and handover files | Repository checks only; no live lab checks | M0 preflight |
| 2026-09-17 | Completed M0 host/resource, virtualisation, subnet, download-access and VirtualBox preflight | Mac checks observed locally; Lenovo checks owner-run and recorded; VirtualBox updated with existing VM preserved | Await authorisation for M1 NAT Network checkpoint |

## Planning validation

The repository validator passed with all 26 requirements and 32 scenarios in their initial states. Local Markdown links and JSON/configuration invariants were checked. Requirement-to-scenario mappings were also checked for consistency. This validates the planning package only; actual guest compatibility, service reachability, performance and account eligibility still need the M0–M6 checks.
