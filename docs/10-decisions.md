# Architecture decisions

Status: accepted for planning on 2026-09-16. Changes require a concrete reason and updates to affected documents/configuration; routine patch-version selection is not a redesign.

| ID | Decision | Reason and consequence |
|---|---|---|
| D01 | One small-business support lab with two parts | Gives infrastructure tasks and support tickets a coherent context |
| D02 | Optimise for junior/Level 1 roles | Deep cloud/data engineering and specialist product collecting do not serve the main goal |
| D03 | Keep VirtualBox on Lenovo; update before build | Already installed; no need to switch to VMware Player/Pro |
| D04 | Run x64 Windows on Intel, ARM Linux on M3 | Matches host architecture and avoids Windows Server emulation |
| D05 | Two simultaneous Lenovo VMs | Fits 16 GB RAM and current storage better than a multi-server enterprise simulation |
| D06 | File shares on DC01 for the lab only | Saves resources; disclose production separation limitations |
| D07 | One shared NAT Network with lab DHCP on DC01 | Provides domain connectivity and outbound access without bridging DHCP to the home LAN |
| D08 | GLPI on an independent Mac-hosted Ubuntu VM | Preserves Lenovo capacity and keeps support records available when the Windows lab is down |
| D09 | Manual ticket entry; no cross-laptop VM routing | Avoids unnecessary integration/network complexity while teaching actual service workflow |
| D10 | Endpoint Central Cloud Free is the initial tool | Avoids another management VM; access/features must be checked, and no paid subscription is assumed |
| D11 | Repurpose WS01 as CLD01 after local cases | Provides practical Entra/Intune experience without a third permanent Windows disk |
| D12 | Local AD and cloud identities remain separate | Hybrid synchronisation adds complexity beyond Level 1 learning outcomes |
| D13 | Activate Microsoft 365 only at M6 | Protects the short trial window from being consumed during foundation learning |
| D14 | Synthetic data and private credential storage | Makes evidence publishable and prevents accidental personal/customer data exposure |
| D15 | 26 fixed core requirements and 32 cases | Enables traceable evidence without claiming population-wide market coverage |
| D16 | Product substitutions are labelled | GLPI is not ConnectWise; Endpoint Central is not NinjaOne; generic documentation is not IT Glue |
| D17 | Google Workspace/Apple MDM are extensions | Useful across some roles, but access/hardware constraints should not block core progress |
| D18 | No implementation or SaaS activation during planning | User requested a design and handover package; actual setup follows later |

## Earlier discussion clarified

“Enough space to start” never meant both Windows disks could grow to maximum plus unlimited snapshots. “Free” means no additional software spend for eligible phases, not perpetual Microsoft licensing. A Mac can support useful macOS exercises without being enrolled into Intune/Jamf. A clean workstation rebuild is useful lifecycle practice but does not prove enterprise image capture/deployment.

## Change record template

Date; decision affected; new evidence; chosen adjustment; rejected alternatives; scope/cost/resource effect; documents/config values changed; validation needed. Add a record only when something actually changes.
