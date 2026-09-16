# Repository and portfolio plan

## Repository identity

Suggested GitHub name: `melbourne-it-support-lab`.

Suggested description: “Independent IT support lab covering Windows, Active Directory, service-desk workflows, endpoint operations and a Microsoft 365/Intune extension.” Update this description to reflect actual completed work when publishing.

This folder is ready to become a Git repository. No remote has been created, no user account inferred and no files published. The owner intends to create the GitHub repository. Avoid putting the entire Desktop or attachments folder into Git.

## Repository layout

| Path | Content |
|---|---|
| README.md | Public orientation and accurate current status |
| START-HERE.md / AGENTS.md | Continuation prompt and assistant instructions |
| STATUS.md | Actual progress and exact next action |
| docs/ | Design, implementation stages, case catalogue and source references |
| config/lab-plan.json | Planned values; no passwords or real tenant IDs |
| tracking/ | Stable requirement/case IDs and evidence status |
| templates/ | Reusable records, explicitly not completed evidence |
| evidence/builds/ | Sanitised installation and environment verification |
| evidence/tickets/ | Concise case outcomes linked to GLPI ticket IDs |
| evidence/case-studies/ | Six selected investigations explained in depth |
| evidence/knowledge-base/ | Eight reviewed articles |
| evidence/runbooks/ | Six tested procedures |
| evidence/demos/ | Recording scripts and links to owner-approved hosted videos |
| scripts/ | Three small lab utilities, added during implementation |
| tools/ | Local repository consistency checker |
| .local/ | Ignored raw/private files, never a public evidence source |

## Git workflow

When the owner starts local Git, initialise **this directory** with `git init -b main`. Inspect `git status` and stage only reviewed project files. Make one coherent commit per completed work package, e.g. `docs: record verified DC01 network setup` or `feat: add read-only endpoint inventory script`.

Use short task branches if helpful, e.g. `m1-windows-foundation`. Do not require a formal pull request for every small lab note. `.github/ISSUE_TEMPLATE/build-task.md` provides a work-package template; scenario IDs already provide the incident backlog.

Before committing run the repository validator and review `git diff --cached`. An ignore file only prevents normal accidental staging; it does not remove secrets from existing history. If a secret is published, revoke/rotate it and address the history; deleting the current file is insufficient.

When creating an empty GitHub remote, avoid adding another README if this project already has one. Add the actual remote URL supplied by the owner; never invent an account/repository destination. Push only after the user requests publication. No GitHub connector or paid account is required to prepare these files.

## Evidence policy

Public evidence contains synthetic names, asset aliases, small redacted screenshots and short text outputs. Do not include VM images, OS ISOs, package installers, licence keys, backup archives, GLPI database dumps, agent enrolment installers, raw event-log bundles, passwords, real serial numbers or personal account screens.

Keep raw captures in `.local/`, review them, then create a separate sanitised copy under evidence. Do not rely on cropping a password while leaving a recovery QR code visible. Re-read textual outputs for home paths, email addresses, tokens and tenant identifiers. Use synthetic lab network values openly; avoid publishing actual public/home network details.

Video files stay outside Git by default. Store an outline and, after explicit owner approval, a link to a hosted recording. Keep the repository lightweight; target less than 50 MB of reviewed documentation/images for v1. This is a project preference, not a GitHub platform limit.

## Case-study structure

Use templates/case-study.md. Explain the request, impact, environment, hypotheses, evidence, chosen fix/escalation, verification, user message and prevention. Include a limitation such as “single-client synthetic lab” where relevant. Good evidence includes a failed test that narrowed the cause, not just a final green screenshot.

Proposed six case studies:

1. User access: approved Finance membership missing.
2. Networking: incorrect DNS versus working internet route.
3. Endpoint: failed application deployment or patch.
4. Recovery: deleted file restored and checked.
5. Microsoft 365: shared mailbox or sharing-permission issue.
6. Intune: assignment/compliance state investigated on the real test VM.

## Demonstrations and interview preparation

Create three 3–5 minute demos: local support diagnosis; ticket/communication/escalation workflow; cloud app/device support. Show the relevant action, evidence and conclusion. A recording of reading this plan is not an implementation demonstration.

Prepare a 60-second explanation for each core skill: what failed, what evidence mattered, what you changed, how you checked it, and when you would escalate. Explain the lab compromises: one domain controller, combined file role, one sequential Windows client, synthetic users, finite trials and limited physical hardware.

## CV wording — future template, not a current claim

After verification, adapt: “Built a Windows/Active Directory support lab and resolved [actual count] documented incidents and requests covering [actually completed areas]. Used [actual products] for ticketing and endpoint administration, with tested recovery procedures and PowerShell diagnostics.”

Keep this under Projects, labelled independent/homelab. Do not describe simulated SLAs as a real service-level achievement, 20 fictional staff as supported customers, or Endpoint Central as NinjaOne experience. Do not claim full v1 while Microsoft 365/Intune is blocked.

## Publication checklist

- Status and summary counts agree with tracking JSON.
- All claimed completed cases have reviewed evidence and verified recovery.
- No secrets, personal data, vendor installers or large VM/video files are staged.
- Links work; diagrams explain the actual deployment and phased reuse.
- Sources and product versions are dated; trial limitations are clear.
- Templates/drafts are distinct from achievements.
- Repository validator passes; a human review of screenshots and claims is complete.

No licence file is imposed by this scaffold. The owner can choose a code/document licence when publishing; third-party products and documentation keep their own licences.
