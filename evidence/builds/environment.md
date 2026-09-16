# M0 host preflight — 2026-09-17

Status: passed. No lab virtual machine, virtual network, cloud tenant, or paid service was created during this milestone.

## LENOVO HOST

- Date/time and timezone: 2026-09-17, Australia/Melbourne.
- Evidence source: commands and Task Manager checks performed by the owner and reported in the project session.
- Host OS/build and architecture: Microsoft Windows 11 Home Single Language, version 10.0.22631, build 22631, 64-bit/x64.
- CPU/RAM: Intel Core i5-1135G7; 15.8 GB usable RAM reported by Windows.
- Actual free SSD space: 181.6 GB on a 475.6 GB C: volume at preflight.
- VM directory: local VirtualBox default folder on the Lenovo C: drive, outside the Git repository.
- Hypervisor: Oracle VirtualBox 7.2.16r174877, updated in place from 7.0.20r163906.
- Virtualisation status: Enabled in Task Manager. `systeminfo.exe` reported that a Windows hypervisor was already detected, so individual Hyper-V requirement fields were not displayed. Existing Windows security/hypervisor settings were not disabled.
- Existing VM safety check: `lu16d-coremu-v1.3` remained registered after the update; no VM was running before or after the update.
- Planned subnet check: no active Lenovo IPv4 address or route was found for `10.77.0.0/24`. The check must be repeated if a VPN that installs additional routes is used during lab work.
- Internet/download check: TCP 443 connectivity to Oracle VirtualBox and Microsoft download services returned `True` in owner-run PowerShell checks.
- Guest/stack versions: none installed for this project.

## MAC HOST

- Date/time and timezone: 2026-09-17, Australia/Melbourne.
- Evidence source: read-only commands executed by Codex on the local Mac host.
- Host OS/build and architecture: macOS 26.6.2, build 25G83, Darwin arm64.
- CPU/RAM: Apple M3; 16 GB RAM from the owner-supplied hardware record.
- Actual free SSD space: 75 GiB available on the writable Data volume after owner cleanup; the preflight target was 60 GB.
- VM directory: not selected yet; it must be outside the Git repository and automatically synchronised folders.
- Hypervisor: UTM is not installed. Installation is intentionally deferred to M3.
- Planned subnet check: no active Mac IPv4 address or route was found for `10.77.0.0/24`.
- Guest/stack versions: HELP01, Ubuntu, GLPI, Apache, PHP, and MariaDB are not installed.

## Repository and scope checks

- The repository is on branch `main` and tracks `origin/main`.
- The selected local network remains `ITSUPPORT-LAB` on `10.77.0.0/24`, subject to another conflict check when a VPN is active.
- No Microsoft 365, Google Workspace, Endpoint Central, or Jamf trial was started.
- No personal host was enrolled, domain-joined, or subjected to a lab policy.

## Acceptance result

The M0 resource and compatibility gate passed: both hosts meet their planned storage floors, the Lenovo exposes hardware virtualisation, the selected subnet has no observed current conflict, VirtualBox opens at the selected stable version, the existing VM was preserved, and work for each host is clearly separated.

Known limitations: Lenovo results are attributed to owner-run checks rather than direct remote observation. VPN routes were not verified while a VPN was connected. Guest firmware, TPM, boot, performance, and OS compatibility remain M1 validation tasks.

Next action: do not start automatically. When authorised, begin M1 on the LENOVO HOST by creating and validating the isolated `ITSUPPORT-LAB` VirtualBox NAT Network before downloading or installing guest operating systems.
