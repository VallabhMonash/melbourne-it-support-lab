# Handover: continue this project

## Copy this into the next assistant session

> Continue implementing the Melbourne IT Support Lab in this repository. Read AGENTS.md, STATUS.md, docs/01-project-scope.md, docs/02-architecture.md and docs/04-implementation-plan.md before acting. The architecture and scope are settled; do not restart project selection or expand the tool list. Start with the next unverified milestone in STATUS.md. The current assistant environment may be on the Mac, while the Windows lab must be built on the separate Lenovo. Confirm execution location before giving or running commands. Teach me through small, practical steps: explain the purpose, identify the exact machine, provide the action, specify the expected result, then verify evidence before advancing. Prepare reversible repository work autonomously. Do not install software on the wrong host, start paid services, use personal data as test data, or claim that instructions you wrote were executed. Keep the project focused on junior/Level 1 IT support in Melbourne. Update the status, requirements and scenario records only from observed or clearly attributed user-reported results. Use the documented fallbacks for blocked trials or resource limits. End each session with the exact next action and a short explanation I should be able to give in an interview.

## Read order for a smaller context window

1. `AGENTS.md` — working rules.
2. `STATUS.md` — actual progress and next action.
3. `config/lab-plan.json` — fixed values.
4. Relevant milestone in `docs/04-implementation-plan.md`.
5. Only the relevant architecture section, scenario rows and template.

Do not load the entire scenario catalogue every turn. Use stable IDs to retrieve the relevant cases. All raw job ads have already been distilled into the requirements list; they are not needed to continue.

## First session contract

The first implementation session is **M0: preflight**, not a bulk download/install session. Confirm free SSD space on both laptops, Lenovo virtualisation support, the actual VirtualBox version, host OS versions, and the current network ranges. Record versions and observations in an environment record. Prepare exact installation steps for the Lenovo separately from Mac work.

No further project-choice interview is needed. Missing facts are limited to implementation inputs listed in STATUS.md. Do not begin Microsoft 365 or Google trials during preflight.

## When something fails

Capture the exact error and which machine produced it. Change one variable at a time. Explain the likely causes before trying a fix, and record which hypothesis the result supports. After two attempts with the same outcome, reassess the evidence instead of cycling through unrelated commands. An unavailable SaaS trial is a documented gap, not a reason to invent results or redesign the local lab.
