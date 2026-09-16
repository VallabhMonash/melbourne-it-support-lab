# Validation and skill coverage

## Evidence states

Requirements: `not_started` → `guided` → `demonstrated`; use `blocked` for missing access/resources. Guided means the owner performed the procedure with assistance and captured a real result. Demonstrated additionally requires an independent repeat with a changed input and an explanation. Reading a guide or generating a script does not satisfy either state.

Scenarios: `not_started`, `in_progress`, `blocked`, `passed`. Passed requires evidence of the actual outcome, verification and clean end state. A guided case can pass while its related skill remains guided. Tabletop cases must remain labelled as tabletop.

Update tracking/requirements.json and tracking/scenarios.json with real evidence paths. For demonstrated skills also fill the independent-repeat note. Keep all 26 requirements in the denominator: `demonstrated / 26 × 100`. No scores are assigned to university education, paid experience, work rights or job-market coverage.

## Live acceptance checklist

| Gate | Check and required evidence |
|---|---|
| Host capacity | Actual free disk/RAM and version record; guest startup and normal host usability |
| Network | Correct DHCP lease/options, internal/external DNS tests, domain discovery and no bridged lab DHCP |
| Identity | New test user can sign in; disabled test user cannot establish a new authorised session |
| Access | Allowed department can read/write intended files; unrelated department is denied |
| GPO | Effective policy/result verified on WS01; moving a test object changes targeting as expected |
| Ticketing | Create, assign, update, resolve and reopen a synthetic ticket linked to an asset |
| Endpoint | Tool sees correct client; deployment/update actually changes client; remote session reaches only test VM |
| Monitoring | Fault produces a meaningful result; ticket opened; recovery produces a healthy check |
| Restore | Deleted synthetic file recovered; content/hash checked; intended permissions verified |
| macOS | User-level diagnosis verified with before/after and reversible settings |
| Microsoft 365 | Licensed test user accesses intended service; wrong permissions reproduced and corrected |
| Intune | Entra join and MDM enrolment both confirmed; targeted policy/app appears on the actual device |
| Teardown | Management/trial disposition recorded; local recovery sign-in works; evidence retained |

No repository script can prove these live gates. Screenshots need context: asset alias, action, expected result, observed result, verification and limitations. Redact personal/tenant identifiers before moving files from .local to evidence.

## Independent assessment

For each skill, ask the owner to perform a variant without step-by-step instructions: a different user/group, another file, a changed symptom or an unfamiliar error. They may consult official documentation as a technician would. Record the variant, assistance used, outcome, evidence and a short explanation.

Assess whether the owner can:

- Describe impact before touching configuration.
- Distinguish observation from assumption.
- Choose a test that rules a cause in or out.
- Avoid using excessive privileges or broad changes as shortcuts.
- Verify with the affected account and a control case.
- Explain when escalation is the right outcome.

An escalation can be a successful Level 1 outcome if diagnosis and handover are sound; the owner need not pretend to solve every advanced issue.

## Portfolio acceptance

Local release requires 24 local passed scenarios and all 21 local requirements demonstrated, M0–M5 complete and honest resource/product limitations. Full v1 requires all 32 scenarios, all 26 requirements, M6 and M7 gates, eight KB articles, six runbooks, three scripts, six deep case studies and three demonstrations. If cloud access is unavailable, retain its blocked entries and label the release local-only.

The generated counts are a project measure. For a real job application, compare that ad's requirements separately and describe direct product use versus transferable experience. Do not say “80% of Melbourne IT support skills” based on this repository.

## Repository verification

Run tools/validate_repo.py after changing plans or tracking. It checks parseable JSON, known states, unique IDs, valid scenario references, required evidence for completion, local file links and resource/configuration invariants. It does not validate cloud licensing, scan every possible secret or test Windows configuration.

Before publication also inspect staged diffs and every image/document manually. Verify links on GitHub after the owner publishes. Automated link checks cannot detect an incorrect conclusion inside a screenshot or an exaggerated CV claim.
