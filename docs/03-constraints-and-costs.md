# Constraints, cost and risk controls

## Hardware budget

Lenovo has 16 GB RAM and about 166 GB free by user estimate. Allocate 8 GB total to two Windows guests initially and leave the rest to Windows/VirtualBox overhead. An 80 GB plus 60 GB virtual capacity is **not** 140 GB immediately consumed, but those files can grow to that amount and snapshots add more.

| Item | Working allowance; measure at M0 and after each milestone |
|---|---|
| Lenovo free-space floor | 30 GB; stop growth-producing operations below this |
| Initial DC01 actual footprint | Planning estimate 25–40 GB, not guaranteed |
| Initial WS01 actual footprint | Planning estimate 30–45 GB, not guaranteed |
| ISOs/installers/updates | Allow roughly 10–20 GB temporarily; remove or relocate unneeded installers after verification |
| Snapshot/backup allowance | Prefer one short-lived snapshot for the active exercise; no long chains or full VM clones by default |
| HELP01 on Mac | 24 GB growing disk, 2 GB initial RAM; target 60 GB free on Mac before starting |

These are estimates, not benchmark results. VM disk deletion inside a guest does not necessarily shrink the host file automatically. Snapshot deletion/merging can need working space. Monitor actual host free space rather than adding only configured disk limits. Do not delete VDI or snapshot files manually in Finder/Explorer.

If storage is tight, remove no-longer-needed downloads, export sanitised evidence, then retire obsolete snapshots through the hypervisor. If still tight, defer cloud transition/optional imaging until space is available. Do not reduce the Windows 11 virtual disk below supported requirements or delete personal files without the owner's selection.

## Software and licence position, checked 2026-09-16

| Component | Budget assumption | Gate / limitation |
|---|---|---|
| VirtualBox base package | Free | Update reported 7.0.20 to a current supported release; record actual version; Extension Pack not required |
| UTM direct download | Free | Mac App Store purchase is unnecessary |
| Ubuntu, Apache/PHP/MariaDB, GLPI | Free self-hosted software | Host resources and maintenance are ours; no commercial GLPI hosting needed |
| Windows Server 2025 | 180-day evaluation | Activate online within the published initial window; record actual expiry |
| Windows 11 Enterprise | 90-day evaluation | Terms, activation and runtime expiry apply; host Windows Home licence does not licence an extra VM |
| Endpoint Central Cloud | Free-edition route | Confirm current account limits/features and distinguish initial trial privileges from retained free features |
| Microsoft 365 Business Premium | One-month eligible business trial | Card/verification may be required; automatic paid conversion must be prevented; services/SKUs must be checked |
| Google Workspace | Optional 14-day trial route | Domain/identity requirements may prevent a zero-cost admin lab; personal Gmail is not equivalent |
| Jamf | Optional trial request | Access not guaranteed; needs a suitable managed target |
| GitHub repository | User will create it | No paid GitHub features or large-file storage are required |

Sources and current links are in [sources](11-sources.md). Commercial rules can change; verify at sign-up, not only from this planning document. No accounts or trials have been started. The design does not rely on eligibility for Microsoft's development-only E5 sandbox.

## Trial schedule

Do M0–M5 before starting Microsoft 365. Plan 12–18 focused hours for the core cloud exercises within its trial window. At activation, keep a private register of activation date, actual expiry, cancellation/renewal setting and evidence-export deadline. Use the vendor's actual date, not an assumed fixed 30-day calculation. Disable recurring billing/cancel as appropriate for the offered terms and verify the effect on access.

Complete exports several days before expiry; verify cancellation rather than assuming closing a browser cancels a service. Stop/retire test management at the end. Keep no recurring paid subscription unless the owner separately chooses it. Google and Jamf trials, if attempted, should be scheduled later, not consumed simultaneously with the Windows build.

## Bounded fallbacks

| Blocker | Approved planning response |
|---|---|
| HELP01 cannot fit on Mac | Start tickets with the Markdown template, marked interim; reclaim space or agree a small local host before claiming GLPI completion. Do not silently add a third Lenovo VM |
| Endpoint Central Cloud unavailable | Complete native inventory/update/remote-diagnosis and scripted monitoring exercises; leave product-specific requirements blocked. An on-prem server is a later design change requiring a revised resource/network budget, not an automatic fallback |
| A Free edition lacks an alert feature | Use Test-LabHealth with scheduled output and manual ticket creation; label it scripted monitoring, not native RMM alert integration |
| Microsoft 365 unavailable | Finish/publish local core; leave M365/Intune requirements blocked and maintain the same denominator |
| Teams not in trial SKU | Request an eligible Teams-inclusive trial only if available within the agreed budget; otherwise leave that case blocked, not replaced by a personal Teams call |
| No hardware printer | Test Windows print subsystem/PDF queue; disclose lack of physical printer experience |
| Google domain verification requires a purchase | Defer admin module; user-level browser/app exercises do not count as Workspace administration |
| Intune rejects VM/edition/enrolment | Check current requirements, licence and join state; do not enrol the personal Lenovo to get a green check |

## Risks and practical response

- **Configuration drift:** maintain a build record and one change ticket; update config and actual state separately.
- **Personal device disruption:** all AD, policy, fault and MDM changes target named guest VMs. Mac core exercises are reversible user-level changes.
- **Lost access:** verify a separate guest recovery administrator and tenant admin before modifying test user access.
- **Host disk exhaustion:** honour the 30 GB floor; simulate a low-space alert by adjusting a test threshold rather than filling the SSD.
- **Credential publication:** no real or lab secrets in tickets/Git; record password-manager item references only.
- **Trial expiry:** schedule cloud work late and keep evidence portable; no clock manipulation or licence circumvention.
- **Shallow learning:** require a changed-input repeat and an explanation, not just successful screenshots.
- **Scope expansion:** additions must map to recurring junior support skills; specialise only after v1 is evidenced.
