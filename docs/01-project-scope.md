# Project scope

## Outcome

Build and operate a small, realistic IT support environment that provides interview evidence for junior and Level 1 roles in Melbourne. The owner must be able to explain a symptom, investigate it, choose a proportionate action, validate recovery, communicate with a user and document the work.

The project is deliberately one connected story with two parts: workplace administration and service operations. It is not a coding showcase; a small amount of automation supports the support work.

## Business scenario

Yarra Office Services is fictional. Its 20 staff work across Finance, Sales and Operations. Six synthetic staff accounts represent the workforce. A technician supports one Windows workstation and investigates issues using separate standard and privileged accounts. The Mac supplies real macOS support practice and hosts the service desk independently of the Windows infrastructure. Lab service targets are invented for learning and are not presented as Australian industry standards.

## Core scope

| Area | Required practical outcome |
|---|---|
| Windows support | Use Settings, Task Manager, Event Viewer, Services and network diagnostics; compare affected and unaffected users |
| Identity | Join a client to AD; create, move, disable and unlock accounts; distinguish identity verification from account administration |
| Access | Use groups for departmental file permissions; demonstrate permitted and denied access |
| Networking | Explain IP/subnet/gateway/DNS/DHCP; isolate client versus shared-service failures without changing the home router |
| Device lifecycle | Document build, software configuration, update, user-data backup, refresh and verification |
| Endpoint operations | Inventory, software deployment, patch results, remote support and health checks with explicit alert handling |
| Service desk | Tickets, categorisation, priority, user updates, escalation, knowledge articles and asset links |
| Security fundamentals | Standard-user working, MFA in the cloud phase, protected credentials, Defender/firewall health and phishing escalation |
| Recovery | Restore synthetic files and validate content; distinguish a VM snapshot from an independent backup |
| macOS | Account/app/connectivity/audio or peripheral diagnosis using the actual Mac, without fleet enrolment |
| Microsoft 365 | User/licence lifecycle, Exchange/shared mail, OneDrive, SharePoint, Teams where licensed, and sign-in support |
| Intune | Enrol one disposable Windows VM; target a small app/configuration/compliance assignment; verify device state |
| Automation | Three small scripts with readable outputs and appropriate non-destructive defaults |

## Extensions, ordered by value

1. Google Workspace: admin user/group lifecycle, Drive permissions and a Gmail/sign-in case, if legitimate trial and domain access are available. Personal Gmail use does not satisfy Workspace administration.
2. Apple management: device enrolment, app deployment and inventory through Intune or Jamf on a suitable disposable target. This is separate from everyday Mac troubleshooting.
3. Physical hardware/printing/AV: test an available printer, headset, external display or spare computer. Do not buy equipment for a required milestone.
4. Imaging: capture and redeploy a generalised Windows image when storage permits. A clean installation or VM snapshot is not an imaging qualification.
5. Additional networking: packet capture or a virtual router exercise once basic diagnosis is solid.

These do not extend the fixed v1 completion criteria. A new job ad may suggest an extension but does not automatically change the architecture.

## Explicit exclusions

- Exact product coverage for ConnectWise, NinjaOne, IT Glue, ServiceNow, Jamf, UniFi, SAP or VoIP.
- Azure compute, Kubernetes, CI/CD application platforms, custom helpdesk development and enterprise data engineering.
- AD-to-Entra synchronisation, hybrid join, enterprise PKI, multiple domain controllers and disaster-recovery claims.
- Operating a real MSP, providing support to real schools, or collecting real customer/student information.
- Automated production remediation, host OS replacement, personal-device wipe/enrolment, router reconfiguration or public inbound access.
- Certification exams, job applications and recruiter outreach; the portfolio prepares for them but does not perform them.

## Deliverables and definition of done

| Deliverable | Acceptance |
|---|---|
| Environment | Named VMs match the architecture; actual versions and resource footprints recorded |
| Local cases | All 24 local scenarios pass, with recoveries verified and no fault left active |
| Cloud cases | All eight cloud scenarios pass for full v1; blocked access remains visible |
| Knowledge base | Eight useful articles, at least two written directly for nontechnical users |
| Runbooks | Six reproducible procedures with prerequisites, checks and rollback |
| Automation | Three implemented scripts meet docs/09-automation-specifications.md |
| Evidence | One sanitised record per case, plus six detailed case studies and three short demo recordings |
| Skill assessment | Requirements marked demonstrated only after independent repetition with a different input |
| Portfolio | README matches actual results, limitations are disclosed, publication review passes |

The 32 records need not be 32 long essays: GLPI tickets and concise Markdown summaries are sufficient. Select six cases for deeper analysis. Required knowledge articles: sign-in, shared-folder access, network diagnosis, software installation, printing, onboarding, safe credential handling, and cloud sharing/sign-in. Required runbooks: VM build, joiner/mover/leaver, incident triage, patch/application change, file recovery, cloud trial teardown.

## Applying the 80% aim

The fixed 26-item core skills list in tracking/requirements.json is a transparent project checklist derived from the supplied ads. **21 demonstrated items out of 26 reaches at least 80% of this checklist.** It does not establish 80% of Melbourne jobs or eligibility for a particular employer. Report both demonstrated and guided items; do not shrink the denominator when a trial is blocked. Formal local/full completion still requires the corresponding milestone gates, not merely a score.

## Experience boundaries

Customer updates, SLAs and escalations are simulated unless another person actually participates. Paid service-desk history, real teamwork, work rights, driving licences and formal qualifications are not awarded by this lab. Label evidence accordingly and use the owner's existing degree/programming experience as separate background.
