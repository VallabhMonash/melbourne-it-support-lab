# Architecture

## Physical placement and resources

| Node | Host | OS/runtime | vCPU | RAM | Growing disk | Role |
|---|---|---|---:|---:|---:|---|
| DC01 | Lenovo | Windows Server 2025 Standard Evaluation, Desktop Experience | 2 | 4 GB | 60 GB | AD DS, DNS, DHCP, small lab file shares |
| WS01 | Lenovo | Windows 11 Enterprise Evaluation x64, standard channel | 2 | 4 GB | 80 GB | Domain employee workstation |
| CLD01 | Lenovo | The WS01 VM repurposed in M6, not an extra VM | 2 | 4 GB | Same 80 GB | Entra-joined Intune test endpoint |
| HELP01 | Mac | Ubuntu Server 24.04 LTS ARM64 in free UTM; GLPI 11.x, Apache, PHP 8.3, MariaDB 10.11 | 2 | 2 GB initially | 24 GB | Tickets, assets, knowledge base |

Pin exact supported patch versions when installed. HELP01's memory is an initial small-lab allocation; increase to 3–4 GB if measured behaviour warrants it, preserving Mac host headroom. Verify the current GLPI prerequisite matrix before choosing package versions. Do not use an x64 Ubuntu ISO on the M3.

Combining file services with a domain controller saves a VM. It is an explicit lab compromise, not a production design recommendation. Do not install GLPI or Endpoint Central Server on DC01. Endpoint Central Cloud is selected to avoid another Windows management VM.

No CPU/RAM allocation is a performance guarantee. Run updates one VM at a time. Power down guests cleanly after a session; confirm host free space before snapshots or bulk downloads.

## Lenovo network — local phase

Create exactly one **VirtualBox NAT Network**, named `ITSUPPORT-LAB`, with `10.77.0.0/24`. Both Windows guests have one NIC attached to that same NAT Network. This differs from selecting ordinary per-VM `NAT`, which is unsuitable for the initial shared domain network. VirtualBox documents shared VM connectivity and outbound access for NAT Network. [Oracle networking](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html)

| Setting | Value |
|---|---|
| Network | 10.77.0.0/24; change consistently if M0 finds overlap with home/VPN networks |
| NAT gateway | Expected 10.77.0.1; verify actual VirtualBox configuration |
| VirtualBox DHCP | Disabled on this NAT Network |
| DC01 | Static 10.77.0.10/24, gateway 10.77.0.1 |
| WS01 during bootstrap | Static 10.77.0.20/24, gateway 10.77.0.1 |
| WS01 after DHCP setup | DHCP lease from 10.77.0.100–149 |
| DHCP server | DC01 only; authorise it in the lab domain |
| DHCP options | Router 10.77.0.1; DNS 10.77.0.10; DNS suffix corp.yarra.example |
| Internal DNS | DC01, including AD service discovery records |
| DNS forwarder | Start with a reachable public resolver such as 1.1.1.1; record a permitted alternative if blocked |
| Inbound exposure | No router forwarding, VirtualBox forwarding or bridged adapters |

During initial server installation use temporary working external DNS for downloads. After AD/DNS promotion, DC01 uses its own static address for DNS and forwards external queries; the domain client uses **only DC01 for DNS**. Do not add a public resolver as the client's secondary DNS, which can cause intermittent domain discovery failures.

If initial Windows setup needs internet before a static address can be configured, temporarily use ordinary NAT with automatic addressing for that guest. After setup, shut it down, attach its single adapter to ITSUPPORT-LAB, set the documented bootstrap address, and verify shared connectivity before promotion/domain join. Record this temporary setup state; do not leave separate ordinary-NAT adapters attached to the domain controller or domain client.

Use the IPv4 design for the learning exercises; do not disable IPv6 globally. Keep the host network configuration unchanged. DHCP exists only inside the virtual network. NAT is a connectivity boundary, not a guarantee that a compromised guest cannot reach the host or home LAN; this is not a malware lab.

### Network acceptance

1. WS01 receives the expected lease/options; only one DHCP service answers.
2. It resolves DC01 and an external name separately.
3. It discovers the domain, signs in and accesses a permitted share.
4. A test standard user cannot access an unpermitted department.
5. Taking DC01 offline produces understandable loss of domain DNS/file services; cached sign-in alone is not proof that the domain is healthy.

Record IP changes as leases change. Do not make ticket procedures depend on WS01 always retaining `.20`.

## Identity and naming

- AD DNS domain: `corp.yarra.example`; NetBIOS domain: `YARRA`.
- `.example` is deliberate synthetic naming; it is not a purchasable or publicly verified Microsoft 365 domain.
- Create an OU root `YarraLab`, with `Users/Finance`, `Users/Sales`, `Users/Operations`, `Groups`, `Workstations`, `ServiceAccounts` and `TestUsers`.
- Keep DC01 in the default Domain Controllers OU. Put WS01 in Workstations.
- Six staff: `alex.chen`, `priya.shah` (Finance); `sam.taylor`, `mia.patel` (Sales); `jordan.lee`, `casey.nguyen` (Operations).
- Separate technician identities: standard `tech.user` and privileged `adm.lab`. Reserve built-in domain Administrator for bootstrap/recovery, not everyday work.
- Give the employee VM a documented private local recovery administrator before domain/cloud transitions. Do not publish its password.
- Staff are standard users. Use a technician test OU/delegation exercise for password resets where practical; do not represent unrestricted Domain Admin as a normal Level 1 permission set.

Cloud users are separate identities in `<tenant>.onmicrosoft.com`. Reuse fictional display names for continuity, but **no synchronisation or shared password is implied**. There is no need to buy a domain for the Microsoft 365 core exercises.

## Files and group-based access

Use tiny synthetic files under `C:\LabData\Shares`, with `Finance`, `Sales`, `Operations` and `Public`. Track expected access in an access matrix.

For each department create a global membership group, e.g. `GG_Finance`, and a domain-local resource group, e.g. `DL_Finance_RW`. Put staff in the global group, nest it in the resource group, then grant the resource group Modify on its folder. Keep Administrators and SYSTEM full control. Deliberately inspect and remove unintended inherited broad access on the lab folder; do not edit unrelated system ACLs.

Share permission can grant authenticated lab users Change while NTFS supplies departmental restrictions; document how the more restrictive combination determines access. Avoid explicit Deny rules in the baseline. Public permits all staff to read; a designated resource group can modify it. Test a positive and a negative case for every department.

Two initial GPOs: `Yarra-Workstation-Baseline` (e.g. screen lock and firewall-preserving settings) and `Yarra-Drive-Maps` (department group targeting). Domain account lockout/password settings must be applied at the correct domain scope, not assumed effective from a workstation OU. Choose and record a modest lab lockout policy; fault exercises use only test staff, never recovery administrators.

## Mac service desk

Use UTM's free download, ARM virtualisation and **Shared Network** for HELP01. The Mac can reach the guest web service on its actual shared-network IP; discover and record it after installation. Do not hard-code a guessed UTM subnet or assume the Lenovo can route to it. UTM documents host/guest service access in shared mode. [UTM networking](https://docs.getutm.app/settings-apple/devices/network/)

GLPI, Apache/PHP and MariaDB run together in HELP01. MariaDB listens locally to the VM; no remote database access is required. Configure GLPI's web root and permissions using the installed release's official instructions. Use local GLPI technician/requester accounts, synthetic records and a unique private password. No SMTP, inbound mail collector, LDAP link or automatic AD inventory is required for v1. Configure scheduled actions as required for the chosen GLPI version, then verify ticket times and backups.

The technician records a request in GLPI on the Mac, investigates in VirtualBox on the Lenovo and returns to GLPI with findings. This is a deliberate manual workflow. Windows-to-GLPI integration and public hosting are excluded. A local-only HTTP setup is acceptable for synthetic data on the private UTM network; record this limitation and do not enter personal credentials. HTTPS can be an extension.

## Endpoint operations

Default: **Endpoint Central Cloud Free**, manually enrol WS01 with its agent. Manage only the test VM. Access the console from the Mac browser; guest connections go out through NAT. Verify region, account access, feature availability, enrolment token protection and free-edition status before using it. The cloud matrix lists patching, software deployment, inventory and remote control in its Free column. [Vendor feature matrix](https://www.manageengine.com/products/desktop-central/cloud/edition-comparison-matrix.html)

Do not enable Endpoint Central MDM for this core phase. It is an agent-based endpoint exercise; Intune owns MDM only in the later phase. Keep patch downloads and app packages small. No distribution server, broad network discovery or agent on the personal hosts is required.

If cloud access is unavailable, follow the bounded fallback in docs/03-constraints-and-costs.md. Do not quietly place a management server on the domain controller or claim NinjaOne experience.

## Cloud transition — same Windows VM, sequential phase

Finish local evidence first. Then:

1. Export evidence and back up the tiny user data set; verify a local administrator can sign in.
2. Record WS01 build and asset history. Remove its Endpoint Central assignments/agent after saving results.
3. Unjoin the **guest** from AD, reboot and verify local sign-in. Retain the lab DC and AD object until the transition is verified, then mark the old workstation record retired.
4. Rename the guest CLD01. Change its adapter from NAT Network to ordinary NAT for the independent cloud phase and set guest IP/DNS to automatic. Verify internet access without DC01 running.
5. Verify the trial tenant, user licence, enrolment scope and supported Windows edition/build. Join Microsoft Entra ID using the intended device-join flow; adding an Office account alone is not proof of Entra join or Intune enrolment.
6. Verify `dsregcmd /status` locally and a matching, healthy device record in Entra and Intune. Redact identifiers before publication.
7. Target one test group with one app, one configuration setting and a supported compliance policy. Do not make BitLocker, Autopilot or hardware attestation a dependency of the VM exercise.
8. At teardown retire/remove management, remove stale test objects as appropriate, and retain local access. Rebuild/rejoin the guest if returning to local AD exercises.

Never restore a cloud-enrolled snapshot and assume tenant/device identity is consistent. Re-enrol a clean test device when identity is stale. Keeping a permanent local and cloud client simultaneously is outside the storage budget.

## Data, backups and operational boundaries

Keep synthetic business data under 100 MB. Store a file-level backup on a separate small virtual disk or outside the source folder for deletion recovery, plus an independently stored copy of that tiny backup on the Mac through an owner-controlled transfer. The former demonstrates file restoration; only the latter survives Lenovo disk loss. Record which protection was actually tested.

GLPI backups include database and required application files/configuration, kept privately. Test restore before deleting the source VM. Git stores sanitised configuration and case summaries, not database dumps, VM images, installers or secrets. A snapshot is a short-term rollback aid, not a backup strategy.
