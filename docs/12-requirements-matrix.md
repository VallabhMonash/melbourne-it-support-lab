# Core requirements matrix

Derived from the supplied ads, not a market-wide survey. All rows start not_started; see tracking/requirements.json for mutable execution state and docs/07-validation-and-coverage.md for scoring rules.

| ID | Skill | Phase | Ad sources | Cases | Acceptance |
|---|---|---|---|---|---|
| R01 | Ticket lifecycle, accurate notes and knowledge documentation | local | A1, A2, A3, A4, A5, A6 | INC-18, REQ-01 | Create, classify, assign, update, resolve and reopen a GLPI ticket; link an asset and useful KB article. |
| R02 | Impact-based prioritisation and response tracking | local | A2, A3, A4, A5, A6 | INC-13, INC-18 | Prioritise a mixed queue with business reasons and separate practice-time targets from actual timestamps. |
| R03 | Customer communication and user guidance | local | A1, A2, A4, A5, A6 | INC-18, REQ-05 | Write acknowledgement, progress and closure updates and guide a simulated user through a verified task. |
| R04 | Escalation and vendor/senior handover | local | A1, A2, A3, A5, A6 | INC-13, INC-17 | Prepare an evidence-based escalation with impact, timeline, checks, changes, workaround and next action. |
| R05 | Windows OS and user-context troubleshooting | local | A1, A2, A3, A4, A5, A6 | INC-08, INC-10 | Use relevant Windows diagnostics and a control account to isolate a service or user-specific issue. |
| R06 | Application installation and software diagnosis | local | A1, A2, A4, A5, A6 | INC-07, REQ-06 | Investigate a failed install and verify a correctly deployed application for a standard user. |
| R07 | Printing and peripheral fundamentals | local | A2, A4, A6 | INC-06 | Restore the lab print subsystem and test output; disclose PDF/virtual versus physical printer limits. |
| R08 | Basic macOS support | local | A2, A6 | INC-15, INC-16 | Diagnose Mac connectivity and app/audio permission issues using reversible user-level actions. |
| R09 | IP, gateway and connectivity diagnosis | local | A2, A3, A4, A6 | INC-13, INC-15 | Separate endpoint, addressing, route and application failures using relevant observations. |
| R10 | DNS and DHCP support | local | A2, A3, A6 | INC-02, INC-03 | Verify lease/options and name resolution; correct lab DNS/DHCP faults without changing the home network. |
| R11 | AD account lifecycle and sign-in support | local | A1, A2, A5, A6 | INC-01, REQ-01, REQ-02, REQ-03 | Create/move/disable test users and recover a lockout while checking identity and access authorisation. |
| R12 | Groups and file permissions | local | A1, A2, A5, A6 | INC-04, REQ-02 | Use group-based access and prove both permitted and denied access after a change. |
| R13 | Group Policy and workstation configuration | local | A1, A2 | INC-05 | Find a targeting problem and verify effective policy on the test workstation. |
| R14 | Device provisioning and refresh | local | A1, A2, A4, A5, A6 | REQ-04 | Follow a build/refresh checklist, preserve synthetic data and validate the rebuilt/reprovisioned client. |
| R15 | Asset and installed-software inventory | local | A1, A2, A4, A5, A6 | REQ-04, REQ-06 | Reconcile actual client inventory with the service-desk asset record and record lifecycle changes. |
| R16 | Patch and endpoint protection checks | local | A1, A2, A6 | INC-11 | Inspect update/security health, diagnose a controlled failure and verify the subsequent result. |
| R17 | Remote support workflow | local | A1, A2, A4, A6 | REQ-05 | Record simulated consent, reach the intended test VM remotely, resolve a task and end the session. |
| R18 | Monitoring and alert response | local | A1, A6 | INC-09, INC-10, INC-14 | Generate a safe fault, capture its alert/check, open a ticket and verify return to healthy. |
| R19 | Security, credential handling and least privilege | local | A1, A2, A5, A6 | INC-17, REQ-01, REQ-03 | Handle synthetic identity verification/credential references and a phishing escalation without exposing secrets. |
| R20 | Backup and verified file restoration | local | A1, A2 | INC-12, REQ-04 | Recover a deleted file and check content/access; explain independent backup versus same-disk copy/snapshot. |
| R21 | PowerShell support automation | local | A1 | REQ-01, INC-09, REQ-06 | Implement and verify the three bounded script contracts, including failure/WhatIf/repeat behaviour. |
| R22 | Cloud identity, licensing and MFA support | cloud | A1, A2, A4, A6 | REQ-07, INC-22 | Administer licensed synthetic users and safely investigate sign-in/MFA with separate recovery admin access. |
| R23 | Exchange Online and shared mailbox support | cloud | A1, A2, A6 | INC-19 | Verify distinct mailbox access/send permissions with test users and demonstrate actual behaviour. |
| R24 | OneDrive and SharePoint support | cloud | A1, A2, A4, A6 | INC-20, INC-21 | Diagnose sync/account context and sharing/access, verify recovery and retain a negative permission test. |
| R25 | Teams user support | cloud | A1, A3, A5, A6 | REQ-09 | Verify test-team membership and user access and explain app/account troubleshooting under the actual licence. |
| R26 | Intune enrolment, configuration and compliance | cloud | A1, A6 | REQ-08, INC-23 | Prove Entra join plus MDM enrolment; diagnose one targeted assignment/compliance issue on CLD01. |
