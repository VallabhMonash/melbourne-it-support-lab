# Working instructions for this repository

## Objective and authority

Help the owner build demonstrable junior/Level 1 IT support skills for Melbourne jobs. This is a learning lab and portfolio, not a production business, commercial service or advanced cloud engineering project. The owner has authorised planning and repository preparation; subsequent implementation requests authorise the relevant lab work. Do not add approval checkpoints for routine reversible work already authorised.

Read STATUS.md and the relevant milestone before acting. Keep architecture choices in docs/10-decisions.md stable unless evidence requires a change. Record any change there and update dependent configuration and plans together.

## Host boundary

- The Lenovo is an Intel i5-1135G7 Windows 11 Home laptop with 16 GB RAM. It hosts DC01 and the sequential WS01/CLD01 VM.
- The Mac is an M3 MacBook Air with 16 GB RAM. It hosts the repository and planned ARM Linux/GLPI VM.
- A command executed on the Mac does not configure the Lenovo. No Windows remote execution connection is assumed.
- Prefix instructions with the target, e.g. `LENOVO HOST`, `DC01`, `WS01`, `MAC HOST`, `HELP01`, or `CLOUD ADMIN`.
- Never paste Windows commands into a macOS shell or install x64 Windows Server on the M3 as if it were native virtualisation.

## Teaching and implementation

Work one milestone and one small checkpoint at a time. State purpose, target machine, action and expected evidence. Let the owner perform the core support tasks; automation should assist learning rather than hide all administration behind scripts. Reuse existing products; do not build a custom ticketing application.

Prepare runbooks and scripts with explicit preconditions, validation, failure paths and rollback. Read-only diagnostics precede changes. Never disable host security controls as a routine virtualisation fix. Fault injection belongs only in the synthetic lab, with a recorded reversal.

## Data and access

Use synthetic identities and documents. Do not put passwords, MFA seeds, recovery codes, enrolment packages, raw logs, real serial numbers, personal screenshots or full job ads in Git. Store raw material in ignored .local/ outside publication paths; keep secrets in the owner's chosen private password manager. Do not treat .gitignore as a secret scanner.

Do not enrol, wipe, domain-join or apply lab-wide policies to either personal host. Scope management to the named VMs. An optional managed Mac/iPad exercise requires a separately agreed disposable target. Do not route lab DHCP onto the home LAN or expose directory, SMB, RDP or GLPI services publicly.

Do not activate billing, subscribe, purchase a domain, publish the GitHub repository or send external messages merely because a plan mentions them. Prepare reviewable material; follow the user's explicit action request for those external steps. Do not ask again if already authorised in the session.

## Evidence and state

`not_started`, `in_progress`, `blocked`, `passed` are scenario states. Requirement states are `not_started`, `guided`, `demonstrated`, `blocked`. Plans and generated examples are never execution evidence. Attribute user-reported results as such. A demonstrated requirement needs its evidence path plus a successful independent repeat with a changed input.

Use local relative Markdown links inside repository files so GitHub links work. Reference actual local files with absolute links when reporting to the user. Maintain STATUS.md, tracking JSON and environment records after meaningful changes. Keep private tenant identifiers out of public state.

Run `python3 tools/validate_repo.py` (Windows: `py -3 ...`) after changing plans/tracking. It checks documentation consistency only. Live tests are those in the milestone and scenario gates; do not claim them from a successful repository check.

Do not add elaborate CI, a frontend, Kubernetes, paid RMM, hybrid identity sync, domain-controller fleets or certification requirements. Do not spawn agents unless the user explicitly requests delegation.
