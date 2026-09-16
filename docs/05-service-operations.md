# Service operations design

## Support workflow

Capture request → verify requester/impact → categorise → prioritise → investigate → resolve or escalate → validate with test user → document → close. Use GLPI's installed status names and map them to this workflow; do not claim a particular UI label before checking the version.

Log: timestamp, requester, affected asset/service, symptom, scope, urgency, impact, priority reason, assignment, work notes, user updates, resolution, verification, elapsed working time, and linked knowledge article. Record lab requester interaction as simulated unless another person actually participated.

An incident restores a disrupted service. A service request supplies something expected, such as access or software. A change alters configuration and should have an impact check and rollback. A recurring problem may need a root-cause investigation beyond the immediate workaround. Use these distinctions in tickets, without claiming an ITIL certification.

## Lab priorities and targets

These are deliberately chosen exercise targets, not contractual SLAs or claims about typical Melbourne employers. Count time only during declared practice sessions; record wall-clock timestamps separately.

| Priority | Example | Initial response target | Action |
|---|---|---|---|
| P1 | Several users unable to access a critical shared service, no workaround | 15 practice minutes | Assess shared scope; escalate promptly; update every 30 practice minutes |
| P2 | One user cannot perform essential work, no workaround | 30 practice minutes | Investigate promptly; escalate if no safe progress within 30 practice minutes |
| P3 | Limited disruption or working alternative | 4 practice hours | Schedule investigation; update before agreed next checkpoint |
| P4 | Planned new access/software request | 1 practice day | Confirm authorisation and delivery expectation |

Do not promise a resolution time without diagnosis. An executive request is not automatically P1. Security concerns receive prompt escalation even if only one person reports them.

## Minimum diagnostic method

1. Restate the symptom and ask when it began, what changed, who is affected and whether a workaround exists.
2. Establish a baseline: another user, another application, local versus network, IP versus DNS, web versus desktop client.
3. Gather relevant evidence before changing settings. Record hypotheses and the next test that separates them.
4. Apply the smallest justified change. Record previous values and rollback.
5. Test the original task as the affected standard user and run a negative/control test where relevant.
6. Explain the outcome in plain language. Record remaining risk, escalation or follow-up.

For network cases distinguish physical/link, addressing, routing, name resolution and application access. A successful ping does not prove an application works; a failed ping can reflect ICMP filtering rather than an outage.

## Communication examples — templates, not actual messages

Acknowledgement: “I understand you cannot open the Finance folder and this is blocking your report. I’m checking whether the issue affects your account or the shared folder. I’ll update you by [time].”

Progress: “Your network connection is working. I found that the expected Finance access group is missing from your account. I’m checking the approved access request before changing it.”

Closure: “Your Finance folder access is restored. We tested opening and saving the sample report using your account. I’ve documented the access change and the checks performed.”

Do not send these to real people. Use them as simulated GLPI user updates.

## Escalation handover

Include business impact, affected scope, timeline, exact error, environment/version, checks and outcomes, changes made, rollback state, workaround, requested next action and next user update due. Escalate when permissions exceed the technician role, evidence suggests a security incident, several users are affected, or the next action risks broader disruption. Do not “fix” an access problem by granting everyone administrator privileges.

## Asset and documentation model

Required fields: synthetic asset ID, hostname, device type, OS/build, assigned fictional user, role, lab network, lifecycle state, management platform, patch/check date and related tickets. Use `MAC01` for the real Mac's public alias and omit its serial number. Keep actual serials, licence keys and personal account details private if needed at all.

Maintain a small environment overview, access matrix, known-issue list and service dependency map. Link tickets to assets and KB articles. Capture changes in a runbook/build record rather than silently editing old evidence to match the new state.

## Credential handling

Use the owner's chosen private password manager for actual lab credentials. Tickets and runbooks contain an item reference such as `vault://YarraLab/DC01-admin`, never the secret. Practise verifying a fictional requester, checking an access approval, resetting one test password, requiring change at next sign-in where appropriate, and documenting the action without storing the password.

Use only dummy text to demonstrate what credential documentation should look like. Do not put real MFA seeds, recovery codes, tenant enrolment tokens or agent packages into Git. A document containing a password-manager reference is not itself a credential vault and is not evidence of IT Glue product experience.

## Monitoring and maintenance

During scheduled practice windows, review endpoint reachability/check-in, updates, free disk, required service state and backup success. Every actionable alert becomes a ticket with validation after recovery. An off-hours powered-down lab is expected, not a production outage. Record false positives and adjust thresholds with a reason.

Simulate low disk by temporarily raising the test alert threshold above current free space. Never fill the host disk. Simulate an offline device by powering off WS01 after recording its state; restore and allow real check-in latency. Use a harmless custom service or safe test endpoint component for service checks; do not stop security, AD or host network services to make an alert.
