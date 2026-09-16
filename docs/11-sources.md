# Sources and verification notes

Checked 2026-09-16. Product links support software constraints and design choices; they are not a representative survey of the Melbourne job market. Terms/UI/version details must be checked again at installation or sign-up.

## Official product references

| ID | Source | What it supports |
|---|---|---|
| S01 | [Oracle VirtualBox downloads](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html) | Free base package and current Windows host installer; patch version to record at setup |
| S02 | [VirtualBox networking](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html) | NAT Network versus ordinary NAT, host-only/internal networking and DHCP control |
| S03 | [Windows Server 2025 evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2025) | Evaluation duration, installation choices and initial activation requirement |
| S04 | [Windows Server hardware](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements) | x64 requirements and minimum-storage caution |
| S05 | [Windows 11 Enterprise evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise) | Evaluation duration, download architecture and expiry limitations |
| S06 | [Windows 11 specifications](https://www.microsoft.com/en-us/windows/windows-11-specifications) | Supported minimum hardware, including storage |
| S07 | [UTM](https://mac.getutm.app/) | Free direct download and ARM virtualisation on Apple Silicon |
| S08 | [UTM shared networking](https://docs.getutm.app/settings-apple/devices/network/) | Host/guest service reachability in shared mode |
| S09 | [GLPI source](https://github.com/glpi-project/glpi) | Open-source self-hosted helpdesk/asset application |
| S10 | [GLPI prerequisites](https://glpi-install.readthedocs.io/en/latest/prerequisites.html) | Compatible PHP/database versions and required extensions; verify selected release |
| S11 | [Endpoint Central cloud editions](https://www.manageengine.com/products/desktop-central/cloud/edition-comparison-matrix.html) | Cloud Free feature column; distinguish from on-prem and trial privileges |
| S12 | [Endpoint Central edition comparison](https://www.manageengine.com/products/desktop-central/edition-comparison-matrix.html) | Vendor free-edition endpoint-limit claim; confirm actual cloud account entitlement |
| S13 | [Endpoint Central system requirements](https://www.manageengine.com/products/desktop-central/system-requirements.html) | On-prem server overhead informing the choice to avoid another local server |
| S14 | [Microsoft business trial details](https://www.microsoft.com/en-au/microsoft-365/business/microsoft-365-business-standard-one-month-trial) | Page covers business trial choices including Premium, card requirement and automatic conversion |
| S15 | [Microsoft 365 Business Premium](https://www.microsoft.com/en-au/microsoft-365/business/microsoft-365-business-premium) | Plan capabilities and Teams/no-Teams choices; verify actual SKU at signup |
| S16 | [Microsoft 365 developer sandbox](https://learn.microsoft.com/en-us/office/developer-program/microsoft-365-developer-program-get-started) | Restricted eligibility and development-only use; not assumed for this lab |
| S17 | [Intune enrolment guide](https://learn.microsoft.com/en-us/intune/device-enrollment/guide) | Enrolment prerequisites, platforms and Apple certificate requirement |
| S18 | [Intune macOS enrolment](https://learn.microsoft.com/en-us/intune/device-enrollment/apple/methods-macos) | Optional managed Mac phase, separate from core user-level Mac support |
| S19 | [Google Workspace trial](https://support.google.com/a/answer/6388094?hl=en-NZ) | Optional trial duration; verify current signup/domain requirements |
| S20 | [Jamf Pro trial request](https://www.jamf.com/request-trial/jamf-pro/) | Trial request exists; acceptance is not guaranteed |

## User-supplied job-ad corpus

| ID | Supplied role | Relevant emphasis |
|---|---|---|
| A1 | Muscatech graduate IT support and managed services | Windows/M365, identity, endpoints, monitoring, scripting and documentation |
| A2 | CC Solutions junior IT support technician | Desktop/macOS, networking, hardware, M365, ticketing and client support |
| A3 | Junior Operations Support Graduate contract | ITIL/incident platforms, Windows/Linux and M365 |
| A4 | Peoplebank banking desktop support contract | L1/L2 queue, deployments, Google Workspace, Endpoint Central and AV |
| A5 | SEW-EURODRIVE IT support | Helpdesk, response tracking, user training, devices, documentation and vendors |
| A6 | School-client Level 1 support ad | Ticketing/RMM/documentation products, Microsoft/Google, Apple and escalation |

The full advertisements and personal attachment paths are not reproduced in this public-ready repository. The lead-data-engineer line in A3 was treated as inconsistent with that ad's junior support scope, not added to the project. No claim is made that these six examples establish market-wide percentages.
