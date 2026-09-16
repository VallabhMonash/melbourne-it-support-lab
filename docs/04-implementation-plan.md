# Implementation plan

## Sequence and working method

M0 → M1 → M2 → M3 → M4 → M5 → M6 → M7. Mac service-desk setup can be prepared independently after M0, but do not run multiple unfinished build tracks with a beginner. Ticket practice starts as soon as GLPI is available and continues through later milestones.

Planning estimate: **74–109 focused hours**, plus downloads and troubleshooting. At 10–15 hours/week this is roughly 6–11 weeks. These are planning ranges, not a deadline. Do not activate short cloud trials until the owner has time allocated for the exercises. Each work session should produce an explanation and evidence, not just configuration.

The exact UI paths/commands for the installed version are written and verified during implementation. Each runbook must identify its target machine. This document specifies what to build and how to accept it; it does not claim installation has occurred.

## M0 — Preflight and repository setup (2–3 hours)

**Inputs:** known hardware in STATUS.md; no licence trials active.

1. LENOVO HOST: record Windows build, CPU/RAM, SSD free space, existing VM locations and virtualisation status in Task Manager → Performance → CPU. If disabled, locate the actual Lenovo model's firmware guidance before changing anything.
2. MAC HOST: record macOS version, available storage and whether UTM exists. Verify enough room for HELP01; do not infer free space from 512 GB capacity.
3. Both: record current home/VPN IP ranges and check the planned `10.77.0.0/24` for overlap. Check network access to official downloads.
4. LENOVO HOST: update VirtualBox from the official Windows hosts download after cleanly shutting existing VMs. Record version; a changed version number is not proof that a guest will boot.
5. Choose VM storage directories outside the Git checkout and outside automatically cloud-synchronised folders. Repository files may live in Git; VM disks must not.
6. Create evidence/builds/environment.md from the environment template. Record actual values without personal serials or account identifiers.
7. Follow docs/08-repository-and-portfolio.md for the local Git workflow. Remote creation/publishing remains the owner's next explicit GitHub step.

**Gate:** version/resource records complete, storage floors met, chosen subnet non-overlapping, VirtualBox opens, future actions clearly assigned to Mac or Lenovo. No Microsoft 365/Google trial started.

**If blocked:** complete documentation/checklist work. Do not compensate by installing Windows Server on the M3 or disabling host security blindly.

## M1 — Windows foundation (7–10 hours)

1. Download official Windows Server 2025 and Windows 11 Enterprise x64 evaluations. Record source, version and checksum where provided; review terms. Install only in guest disks.
2. Create ITSUPPORT-LAB NAT Network with its own DHCP disabled. Confirm the network exists before attaching guests.
3. Create DC01 and WS01 using config/lab-plan.json. Configure supported firmware and a virtual TPM 2.0/Secure Boot setup for Windows 11; follow current VirtualBox instructions instead of bypassing OS checks.
4. Choose **Standard Evaluation / Desktop Experience** for Server and the regular Windows 11 Enterprise evaluation, not a minimal/headless Server or LTSC client by accident.
   If setup requires internet before static networking is available, use the temporary ordinary-NAT bootstrap described in architecture, then return to the shared lab network before M2.
5. Install, activate, patch and record actual expiry dates. Use the official setup flow; do not embed personal account details in evidence.
6. Configure static bootstrap IPs, local recovery access and a timezone of Australia/Melbourne. Record time synchronisation; time errors can affect domain authentication.
7. Install matching Guest Additions if needed for usability. Leave broad host-folder sharing and automatic clipboard access off unless required for a reviewed transfer.

**Gate:** both guests boot and retain settings after restart; they communicate over the lab network; each reaches official update services; no host/VM disk below the resource floor. Save a build record and initial network diagram.

**Recovery:** reinstall a failed new guest from the recorded configuration. No user data should yet depend on it.

## M2 — Identity, networking and permissions (10–14 hours)

1. DC01: promote the new `corp.yarra.example` forest; verify AD DS/DNS and service discovery. Record the DSRM recovery secret privately.
2. Set final DNS behaviour from architecture. Configure/authorise Windows DHCP and its scope/options; switch WS01 to a DHCP lease.
3. Create OUs, synthetic users, role/resource groups and technician identities. Perform the first few users manually so the owner understands the fields.
4. WS01: join the domain, move the computer to the intended OU and verify standard-user sign-in.
5. Create departmental shares and the access matrix. Test Finance allowed/Sales denied and equivalent cases for the other departments.
6. Apply two baseline GPOs and verify their effective application rather than assuming link creation equals success.
7. Prepare controlled lockout, share-permission, wrong-DNS and wrong-OU faults with written reversals. Do not execute multiple faults together yet.

**Gate:** domain discovery, DHCP, permitted/denied shares and GPO results verified; recovery admin works; six staff accounts and current asset record exist. Save access and identity evidence.

**Recovery:** reverse only the changed group/ACL/GPO. If rebuilding DC01 becomes necessary, use the recorded configuration; do not treat arbitrary old DC snapshot restores as a production recovery practice.

## M3 — Service desk and knowledge base (6–9 hours)

1. MAC HOST: install free UTM; create HELP01 as Ubuntu ARM64 with shared networking.
2. HELP01: install the compatible web/database stack and supported GLPI release. Configure application paths, permissions and scheduled actions per vendor docs.
3. MAC HOST: open GLPI at its recorded private guest address. Verify it is not publicly hosted and its database is not exposed.
4. Configure a fictional organisation, local requester and technician accounts, categories, priorities and lab service targets from docs/05-service-operations.md.
5. Enter DC01, WS01 and MAC01 as assets. Mark MAC01 as an existing personal device used for limited local exercises, not a managed fleet endpoint.
6. Create one request, assign it, add an internal note and a user-facing update, resolve it and reopen it. Verify the timestamp/timezone and audit history.
7. Back up GLPI's database and required files/configuration privately; verify a small restore using the same installation with a recovery plan or a temporary isolated database, without overwriting the only copy.

**Gate:** complete ticket lifecycle and asset linkage demonstrated; two initial KB articles created; backup/restore of a test ticket verified. Record the GLPI-to-Markdown evidence export convention.

**Recovery:** use interim Markdown tickets if HELP01 is blocked, but M3 remains incomplete until the actual service desk works.

## M4 — Endpoint operations, scripts and recovery (10–15 hours)

1. CLOUD ADMIN: verify Endpoint Central Cloud Free route and account scope. Enrol WS01 manually; record which features remain available in Free, not just trial.
2. Inventory the client; deploy a small approved free application using a vendor-supported package; verify version and installation under a standard user.
3. Inspect updates, schedule one limited patch/app update and verify the result/restart. Do not schedule BIOS/firmware changes or broad automatic remediation.
4. Perform a consent-recorded remote session to the test guest from the technician console. No unattended access to personal hosts.
5. Implement Get-LabInventory, Test-LabHealth and New-LabUsers using the contracts in docs/09-automation-specifications.md. Prove failure handling and repeatability.
6. Run scheduled health checks while the guest is awake. Create a ticket from a safely simulated alert, investigate, recover and run a healthy check.
7. Prepare the small file backup and restoration exercise. Verify both content and intended permissions after restore; document the backup's failure boundary.
8. Prepare a workstation refresh checklist: preserve test files, record apps/configuration, rebuild or reprovision the guest, restore data and test user access. Recreating a VM from a known snapshot alone is not a full refresh demonstration.

**Gate:** tool-enrolment, inventory, app deployment, patch result and remote session evidenced; scripts meet their acceptance contracts; a deleted test file has been restored. If product access fails, mark the affected requirements blocked and complete independent work.

## M5 — Local support practice and assessment (20–30 hours)

Work through the 24 local scenarios in docs/06-scenario-catalogue.md. Each has one ticket and one concise evidence summary. Reuse actual build/recovery events where appropriate, but do not fabricate a fault that did not occur.

Include the two Mac cases, a safe phishing tabletop, queue prioritisation, joiner/mover/leaver, device refresh and remote support. At least six cases should be independently repeated using a different user, group, device state or symptom. For every requirement marked demonstrated, record its independent repeat even if several requirements share the same case.

Complete eight KB articles/six runbooks across M5–M6, with cloud-specific documents prepared as drafts until tested. Prepare four of the six deep case studies here. Record clean end state after fault exercises.

**Gate — local core complete:** all 24 local scenarios passed, all applicable local requirements demonstrated, required local runbooks/scripts tested, no active faults, and three example support stories can be explained without copying an assistant's answer. An honest local-only portfolio can be prepared at this point while cloud access remains pending.

## M6 — Microsoft 365 and Intune (12–18 hours)

**Preconditions:** local evidence is exported; the owner can allocate time during the trial; guest local access verified; trial/billing terms reviewed.

1. CLOUD ADMIN: establish an eligible Business Premium trial with the services needed, including Teams if possible. Record actual licence assignments, trial dates and renewal controls privately.
2. Create two or three licensed synthetic test users and separate admin access. Enable appropriate MFA without locking out the only administrator. Keep tenant identifiers and verification details out of Git.
3. Configure a shared mailbox, test user access/send permissions, a small SharePoint site/library and OneDrive test files. Scope sharing to test identities; no public links required.
4. Carry out WS01 → CLD01 transition exactly as in architecture. Verify Entra join and Intune enrolment as separate facts.
5. Target the CLD01 test group with a small app, one safe configuration and supported compliance checks. Record assignment, device check-in, actual setting and report latency.
6. Complete all eight cloud cases. Repeat selected cases independently; create the remaining case studies and knowledge articles.
7. Export sanitised evidence, retire test management as appropriate and verify billing/cancellation state before trial expiry. Preserve local recovery access.

**Gate:** eight cloud cases passed; five cloud requirements demonstrated; cloud join/licence/enrolment evidence exists; no unsupported claim of hybrid sync, Autopilot or physical fleet management. If access is blocked, M6 remains blocked; M7 may still publish an explicitly local-only release.

## M7 — Portfolio packaging (7–10 hours)

1. Update the README with actual results, architecture versions and known gaps. Keep design history separate from achieved behaviour.
2. Choose six detailed case studies: account/access, DNS/network, device/software, recovery, cloud sharing/mail and Intune.
3. Make three short demonstrations, approximately 3–5 minutes each: local troubleshooting, ticket/communication workflow, cloud device/app support. If cloud is blocked, label that demo absent rather than replacing it with an implied cloud success.
4. Complete eight KB articles and six runbooks; remove drafts from claims of completion.
5. Validate tracking/evidence links and review all staged files for secrets, personal information and large binaries.
6. Prepare a GitHub description, release notes and CV bullets using only verified outcomes. Follow the owner's publishing request when creating/pushing the remote.

**Gate — full v1:** all M0–M6 gates passed, all 26 core skills demonstrated, 32 cases passed, deliverables reviewed and repository validation successful. A local-only release must say so visibly.

## Optional backlog

Google Workspace, Jamf/Apple MDM, physical printer/AV, generalised imaging and deeper networking are in scope only as named extensions after the core. For each extension create a short decision note with learning outcome, access/cost, resources and evidence. Do not add products merely to lengthen a CV tool list.
