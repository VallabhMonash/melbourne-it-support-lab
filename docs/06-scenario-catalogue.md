# Scenario catalogue

These are exercise specifications, not completed incidents. Faults target synthetic lab objects only. Record the real outcome in GLPI and a sanitised evidence summary; do not copy the planned success as an observed result.

24 local cases and eight cloud cases comprise v1. `M#` indicates the earliest prerequisite milestone; complete cases during M5/M6 as appropriate. The workstation refresh follows other dependent local cases and requires reinstating the baseline. Tabletop or simulated user reports are explicitly labelled.

## Index

| ID | Case | Phase | Prerequisite | Requirement IDs |
|---|---|---|---|---|
| INC-01 | Locked-out employee account | local | M2 | R11, R19 |
| INC-02 | Wrong client DNS server | local | M2 | R09, R10 |
| INC-03 | Incorrect DHCP option | local | M2 | R09, R10 |
| INC-04 | Missing Finance access group | local | M2 | R12, R11 |
| INC-05 | GPO not applying to workstation | local | M2 | R13 |
| INC-06 | Windows printing service issue | local | M2 | R07, R05 |
| INC-07 | Application install fails | local | M4 | R06 |
| INC-08 | Application problem affects one user | local | M2 | R05, R06 |
| INC-09 | Low-space monitoring alert | local | M4 | R18, R21 |
| INC-10 | Required test service stopped | local | M4 | R05, R18 |
| INC-11 | Patch or app-update failure | local | M4 | R16, R06 |
| INC-12 | Deleted file restoration | local | M4 | R20, R12 |
| INC-13 | Single-user versus shared connectivity outage | local | M2 | R02, R04, R09 |
| INC-14 | Managed endpoint offline | local | M4 | R18 |
| INC-15 | Mac connectivity diagnosis | local | M5 | R08, R09 |
| INC-16 | Mac audio or application permission | local | M5 | R08, R03 |
| INC-17 | Suspicious access or phishing report | local | M5 | R04, R19 |
| INC-18 | Mixed support queue and updates | local | M3 | R01, R02, R03 |
| REQ-01 | New employee onboarding | local | M2 | R01, R11, R19, R21 |
| REQ-02 | Department transfer | local | M2 | R11, R12 |
| REQ-03 | Employee offboarding | local | M2 | R11, R19 |
| REQ-04 | Workstation refresh | local | M4 | R14, R15, R20 |
| REQ-05 | Remote support session | local | M4 | R03, R17 |
| REQ-06 | Approved software deployment | local | M4 | R06, R15, R21 |
| INC-19 | Shared mailbox permission issue | cloud | M6 | R23 |
| INC-20 | OneDrive account or sync issue | cloud | M6 | R24 |
| INC-21 | SharePoint access denied | cloud | M6 | R24 |
| INC-22 | Cloud sign-in or MFA support | cloud | M6 | R22, R19 |
| INC-23 | Intune assignment or compliance issue | cloud | M6 | R26, R18 |
| REQ-07 | Microsoft 365 user lifecycle | cloud | M6 | R22, R19 |
| REQ-08 | Enrol and configure CLD01 | cloud | M6 | R26 |
| REQ-09 | Teams membership and user support | cloud | M6 | R25, R03 |

## Execution records

Use templates/ticket.md and save under evidence/tickets/CASE-ID.md. Store private raw captures in .local; only publish sanitised evidence. One case may provide evidence for multiple requirements, but each skill needs its own independent-repeat explanation before being marked demonstrated. For every case record the observed symptom, tests, result, verification and recovery. A failed hypothesis is useful evidence; a guessed resolution is not.

## INC-01 — Locked-out employee account

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** An employee cannot sign in after repeated incorrect passwords.
- **Controlled setup:** Use a synthetic test account under the documented lockout policy; verify the recovery admin first.
- **Diagnosis:** Check exact error, account lockout/enable state, affected scope and recent attempts; verify the fictional requester.
- **Acceptance:** Approved unlock/reset permits a fresh sign-in; explain why unlocking without investigating can lead to recurrence.
- **Recovery:** Restore the test account to its intended state; do not expose or reuse its password.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-02 — Wrong client DNS server

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** Internet IP access works but domain names or shares fail.
- **Controlled setup:** Record WS01 DNS, then set an incorrect test DNS address on WS01 only.
- **Diagnosis:** Compare address/gateway, IP reachability, external versus internal resolution and domain discovery.
- **Acceptance:** Client uses DC01 DNS again; domain and external names resolve and the original share opens.
- **Recovery:** Restore DHCP-derived settings or the recorded baseline; verify no public secondary DNS.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-03 — Incorrect DHCP option

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** A renewed lease supplies the wrong DNS option.
- **Controlled setup:** Record the lab DHCP option, change only the test scope DNS option, then renew WS01.
- **Diagnosis:** Inspect lease server, address/mask/router/DNS; distinguish a valid lease with bad options from no lease.
- **Acceptance:** Correct scope option and renewed lease restore domain resolution.
- **Recovery:** Restore original scope settings and verify that home network configuration was untouched.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-04 — Missing Finance access group

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** A Finance employee receives access denied.
- **Controlled setup:** Remove an approved synthetic test user's Finance group membership after recording it.
- **Diagnosis:** Compare effective groups, share and NTFS permissions; verify authorisation and fresh token behaviour.
- **Acceptance:** Approved access works after a fresh sign-in; a Sales control account remains denied.
- **Recovery:** Restore the approved membership and log the access change without broad ACL changes.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-05 — GPO not applying to workstation

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** Expected screen-lock or drive mapping settings are missing.
- **Controlled setup:** Move WS01 into a deliberately untargeted lab OU, recording its prior OU.
- **Diagnosis:** Inspect OU/link/filter targeting and effective policy results; compare user versus computer settings.
- **Acceptance:** Return WS01 to intended scope and verify actual policy, not just a successful refresh command.
- **Recovery:** Restore OU membership and leave only the documented baseline GPOs active.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-06 — Windows printing service issue

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** A test print job cannot complete.
- **Controlled setup:** Use a synthetic PDF/available printer test; stop the print spooler only inside WS01 when appropriate.
- **Diagnosis:** Inspect queue, selected printer, spooler state and document/application scope.
- **Acceptance:** Restart/recover the guest print subsystem and produce a verified test output.
- **Recovery:** Remove synthetic queued jobs; restore original guest service state; disclose whether no physical printer was used.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-07 — Application install fails

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** A requested application does not install.
- **Controlled setup:** Use a safe incorrect package path or invalid deployment parameter; do not download malware or corrupt production apps.
- **Diagnosis:** Inspect return code/log and package path, installer type, permissions and supported version.
- **Acceptance:** A corrected approved package installs and launches under the standard test user.
- **Recovery:** Remove only test package artefacts; preserve useful sanitised logs.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-08 — Application problem affects one user

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** An application works in one test profile but not another.
- **Controlled setup:** Use a disposable browser/app profile and a reversible setting that causes the symptom.
- **Diagnosis:** Compare profiles, settings and errors; establish whether OS-wide reinstall is justified.
- **Acceptance:** Correct the specific setting/profile state and verify both affected and control profiles.
- **Recovery:** Restore/delete only the disposable profile after exporting synthetic files; do not delete real Windows profiles.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-09 — Low-space monitoring alert

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** Health output reports low free disk space.
- **Controlled setup:** Raise Test-LabHealth's warning threshold above current free space; never fill the SSD.
- **Diagnosis:** Check measured values, threshold, guest versus host storage and whether the warning represents a real capacity problem.
- **Acceptance:** Explain simulated alert, create a ticket, restore threshold and capture healthy result.
- **Recovery:** Restore production-like lab threshold and verify Lenovo free-space floor.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-10 — Required test service stopped

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** A health check reports a stopped service.
- **Controlled setup:** Choose a harmless lab-only service or disposable test component; record its original state.
- **Diagnosis:** Inspect service status/startup and relevant events; distinguish missing service, permission error and stopped state.
- **Acceptance:** Restore the test service and obtain healthy output; no automatic remediation needed.
- **Recovery:** Return service and monitoring configuration to baseline; never stop AD/security/host services for this case.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-11 — Patch or app-update failure

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** An approved test update reports failure or remains pending.
- **Controlled setup:** Use a reversible guest connectivity interruption or safe invalid app-update job; label which kind was used.
- **Diagnosis:** Inspect status/error, connectivity, pending restart, applicability and actual installed version.
- **Acceptance:** Correct the cause and verify update/version/restart result on the endpoint.
- **Recovery:** Restore connectivity and schedules; no indefinite pause of Windows updates or protection.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-12 — Deleted file restoration

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** An employee deleted a required sample document.
- **Controlled setup:** Back up a tiny synthetic file and record its hash/ACL before deleting the source copy.
- **Diagnosis:** Locate correct backup/version and distinguish missing file from denied access.
- **Acceptance:** Restore to a separate path first, compare content/hash and verify intended access before replacing the source.
- **Recovery:** Retain test evidence and remove redundant copies; document whether an independent-device copy was tested.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-13 — Single-user versus shared connectivity outage

- **Mode / prerequisite:** hands_on_with_simulated_reports; M2.
- **User symptom:** A user says the internet is down.
- **Controlled setup:** Disconnect only WS01's virtual cable for one run; use an explicitly simulated multi-user report for the queue comparison.
- **Diagnosis:** Inspect link/address/route/DNS/application in order and separate observed scope from reported scope.
- **Acceptance:** Reconnect and verify original task; explain how multi-user impact would change priority/escalation.
- **Recovery:** Reconnect the guest adapter and verify DNS/domain access; do not change the home router.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-14 — Managed endpoint offline

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** The management console shows a stale/offline endpoint.
- **Controlled setup:** Record WS01 check-in then cleanly power it down.
- **Diagnosis:** Check last-contact age, maintenance window and guest power before treating it as an outage.
- **Acceptance:** Power up and capture real renewed check-in; document observed reporting delay.
- **Recovery:** Restore running or intentionally scheduled-off state and close the alert appropriately.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-15 — Mac connectivity diagnosis

- **Mode / prerequisite:** hands_on; M5.
- **User symptom:** A Mac application cannot reach an online resource.
- **Controlled setup:** During a suitable break, briefly disable Wi-Fi or use a disposable app's offline setting; record the original state.
- **Diagnosis:** Check connection, address, gateway, DNS and another app/site; avoid changing router settings.
- **Acceptance:** Restore the original setting and verify the original task plus a control resource.
- **Recovery:** Restore personal Mac connectivity immediately; no lab MDM/network profiles installed.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-16 — Mac audio or application permission

- **Mode / prerequisite:** hands_on; M5.
- **User symptom:** A meeting/test recording app has no microphone input.
- **Controlled setup:** Use a test app and reversible input selection or microphone permission change.
- **Diagnosis:** Inspect selected input, input meter, application permission and another app as a control.
- **Acceptance:** Correct the selection/permission and verify a harmless test recording without publishing personal audio.
- **Recovery:** Restore preferred settings and delete unwanted private recordings.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-17 — Suspicious access or phishing report

- **Mode / prerequisite:** tabletop; M5.
- **User symptom:** A fictional user reports a suspicious link or MFA prompt.
- **Controlled setup:** Create a text-only synthetic example; use no live malicious URL or actual phishing delivery.
- **Diagnosis:** Ask what happened, preserve useful reported details, identify scope and prepare escalation without requesting a password.
- **Acceptance:** Complete an accurate handover and safe user guidance; label the entire case tabletop.
- **Recovery:** No live security controls or accounts changed; remove any misleading mock content from normal inboxes.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-18 — Mixed support queue and updates

- **Mode / prerequisite:** hands_on_with_simulated_reports; M3.
- **User symptom:** Several requests arrive with different impact and urgency.
- **Controlled setup:** Create three synthetic GLPI tickets with different scopes, workarounds and requested dates.
- **Diagnosis:** Justify ordering, assign owners, record response times and separate internal notes from user updates.
- **Acceptance:** Resolve/reopen a test ticket, link an asset/KB and explain a prioritisation decision.
- **Recovery:** Close or clearly label remaining practice tickets; report timings as simulated practice metrics.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-01 — New employee onboarding

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** A new Finance employee needs access and a configured workstation.
- **Controlled setup:** Use an approved fictional request and an extra test identity; baseline staff remain unchanged.
- **Diagnosis:** Check role approval, naming, groups, device needs, standard-user privileges and credential delivery procedure.
- **Acceptance:** User signs in and reaches intended resources; unrelated department access is denied; script batch variant verified separately.
- **Recovery:** Disable/remove only disposable users when finished after recording IDs; retain no passwords in ticket.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-02 — Department transfer

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** An employee moves from Sales to Operations.
- **Controlled setup:** Record the test user's approved old/new access.
- **Diagnosis:** Check group memberships and resource access, including inherited membership and fresh logon token.
- **Acceptance:** New department access works and old access no longer works after refresh/sign-in.
- **Recovery:** Restore baseline department if the fixture is reused; record change history.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-03 — Employee offboarding

- **Mode / prerequisite:** hands_on; M2.
- **User symptom:** A fictional employee leaves the organisation.
- **Controlled setup:** Use a disposable account with synthetic data and a recorded approved request.
- **Diagnosis:** Check disablement, active sessions, access removal and data-retention needs; distinguish new authentication from existing sessions.
- **Acceptance:** Fresh access is prevented and lab sessions handled; synthetic data preserved according to the request.
- **Recovery:** Keep account disabled or remove it only after review; do not delete baseline staff or real data.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-04 — Workstation refresh

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** The employee workstation needs a documented rebuild/reprovision.
- **Controlled setup:** Complete dependent local cases, back up test files, inventory apps and record recovery credentials before rebuilding the guest.
- **Diagnosis:** Follow a deployment checklist and verify package/configuration choices; plan storage without a permanent duplicate VM.
- **Acceptance:** Rebuilt/reprovisioned client rejoins domain, restores test data, runs required apps and has updated asset record.
- **Recovery:** Reconcile old/new device records and remove obsolete agent registrations; disclose that image capture is not included.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-05 — Remote support session

- **Mode / prerequisite:** hands_on_with_simulated_reports; M4.
- **User symptom:** A simulated remote employee needs help with an application setting.
- **Controlled setup:** Use the endpoint tool's supported session to WS01 and record simulated consent.
- **Diagnosis:** Verify target identity, communicate intended action and observe the symptom before changing it.
- **Acceptance:** Resolve and verify the task; record session start/end and end access cleanly.
- **Recovery:** Close the session and restore any temporary setting; personal hosts were not targeted.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-06 — Approved software deployment

- **Mode / prerequisite:** hands_on; M4.
- **User symptom:** An employee requests a small approved free application.
- **Controlled setup:** Use a vendor-sourced package and target only WS01.
- **Diagnosis:** Check approval, architecture, install parameters and detection method; capture pre-install inventory.
- **Acceptance:** Tool reports deployment and actual client version/launch verifies it; inventory difference captured.
- **Recovery:** Document uninstall/rollback and remove extra package copies if storage requires.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-19 — Shared mailbox permission issue

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A test user can see a mailbox but cannot send as it, or cannot open it.
- **Controlled setup:** Use two licensed synthetic users and a test shared mailbox; change one intended permission.
- **Diagnosis:** Inspect access versus Send As/delegation separately and allow recorded propagation time; check web client as control.
- **Acceptance:** Authorised user can perform requested action; unapproved user cannot.
- **Recovery:** Restore intended delegation and clean up synthetic messages/objects during trial teardown.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-20 — OneDrive account or sync issue

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A sample file is missing locally or not synchronising.
- **Controlled setup:** Use synthetic files and pause sync or select a deliberately different test folder/account context.
- **Diagnosis:** Compare web and desktop state, correct account, sync status and specific error before resetting anything.
- **Acceptance:** Correct state results in the intended file appearing/syncing and a verified edit.
- **Recovery:** Restore normal test sync; preserve needed evidence before removing test account.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-21 — SharePoint access denied

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A test employee cannot open a document library.
- **Controlled setup:** Remove only a test group's expected access on the test site/library.
- **Diagnosis:** Inspect account, group/site/library permissions and broken inheritance where relevant; check approved access.
- **Acceptance:** Expected user can access, a control user remains denied and no public sharing was needed.
- **Recovery:** Restore the intended access matrix and remove temporary sharing links.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-22 — Cloud sign-in or MFA support

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A test user reports a sign-in/MFA problem.
- **Controlled setup:** Use a safe wrong-account or unregistered test MFA-method scenario with separate working admin access.
- **Diagnosis:** Inspect exact error, account/licence/role, available sign-in evidence and allowed recovery path.
- **Acceptance:** Restore intended user sign-in with MFA where applicable and document verification without secrets.
- **Recovery:** Remove temporary test methods securely; never remove the only administrator's recovery access.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## INC-23 — Intune assignment or compliance issue

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** CLD01 does not receive an expected setting/app or reports a compliance issue.
- **Controlled setup:** Use an intentionally incorrect test-group assignment or one supported reversible compliance setting.
- **Diagnosis:** Check licence, Entra/MDM state, group assignment, last check-in, supported setting and device-side evidence.
- **Acceptance:** Correct targeted assignment/state, sync and verify device behaviour plus report update; record latency.
- **Recovery:** Restore intended policy and remove duplicate/stale records through documented teardown.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-07 — Microsoft 365 user lifecycle

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A new employee needs cloud services, then a mover/leaver change.
- **Controlled setup:** Use two or three licensed synthetic users and a fictional approved request.
- **Diagnosis:** Check available licences, groups, intended services, least privilege and data ownership.
- **Acceptance:** User accesses licensed services; later block/revoke/remove access appropriately and verify new access denied.
- **Recovery:** Preserve test evidence/data as planned, recover licences and document actual remaining objects.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-08 — Enrol and configure CLD01

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A test endpoint must be managed through Intune.
- **Controlled setup:** Finish local phase, verify recovery admin, repurpose WS01 and follow cloud transition runbook.
- **Diagnosis:** Check correct join flow, supported edition, licence/enrolment scope and device identity; distinguish registration from join.
- **Acceptance:** Entra join plus Intune record verified, one app and safe setting reach CLD01, and compliance status is explained.
- **Recovery:** Retire management before trial expiry; verify local access and stale-object cleanup.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## REQ-09 — Teams membership and user support

- **Mode / prerequisite:** hands_on; M6.
- **User symptom:** A user needs access to the test team's channel/files.
- **Controlled setup:** Verify a Teams-capable licence, create a tiny test team and use a second test account.
- **Diagnosis:** Check account/tenant, membership and web versus desktop behaviour; no personal Teams substitution.
- **Acceptance:** Intended user can access the team/channel and a synthetic collaboration action works.
- **Recovery:** Remove test content/membership during teardown and record any licence limitation.
- **Evidence:** ticket notes plus relevant before/after observation, affected-user verification, clean end-state check and source of observations. Do not publish secrets or personal identifiers.

## Optional extension cases

- EXT-G01: Google Workspace user/group lifecycle in an actual admin tenant; requires legitimate admin/domain access.
- EXT-G02: Drive sharing or Gmail support with two synthetic managed identities; record exact product/edition.
- EXT-A01: Apple MDM inventory/app assignment on an agreed disposable target; do not enrol the everyday Mac implicitly.
- EXT-H01: Physical printer, external display or headset diagnosis using available equipment.
- EXT-I01: Capture/redeploy a generalised Windows image after reviewing storage and licensing.

Extensions do not affect the fixed 32-case or 26-requirement denominator. Give them separate execution records if attempted.
