# Future automation specifications

These are implementation contracts, not scripts already written or tested. Build in M4 after performing basic tasks manually. Use Windows PowerShell 5.1-compatible syntax where practical, with explicit module requirements; the Lenovo having Python for repository checks is unrelated to guest PowerShell availability.

## S1 — Get-LabInventory.ps1

**Purpose:** read a test endpoint's configuration and produce a useful asset/diagnostic record.

- Target: WS01/CLD01 locally; no network scanning or implicit remote execution.
- Inputs: synthetic asset alias, output directory, optional inclusion of installed application names/versions.
- Output: JSON containing timestamp, asset alias, OS/build, RAM, disks/free space, adapter addressing, selected service/Defender status and installed applications. Missing/denied fields are explicit, not fabricated.
- Use normal diagnostic APIs/registry reads; avoid `Win32_Product` enumeration because it can trigger installer consistency actions.
- Collect only what supports the lab. Omit hardware serials, product keys, tokens and user documents. Raw network output still requires review before publication.
- Does not install, repair, delete, restart, alter permissions or change networking.

**Acceptance:** two real runs show an intentional harmless difference such as an added app; an unwritable output directory returns a clear nonzero result; unavailable fields are handled; standard-user run has documented limitations. Verify reported OS/disk/app values against another source. Re-running does not change endpoint configuration.

## S2 — Test-LabHealth.ps1

**Purpose:** evaluate explicit checks and produce results useful for a monitoring ticket.

- Target: local employee VM; optional DNS/HTTP probe targets supplied explicitly.
- Inputs: minimum free-space percentage, named services to inspect, DNS test name and optional HTTPS endpoint.
- Output: JSON check list with `pass`, `warn`, `fail` or `unknown`, measured value, threshold, timestamp and a short reason. Summary exit codes: 0 healthy, 1 warning/failure, 2 invalid input/execution error.
- No automatic remediation. A timeout, access error and proven service outage are different findings.
- Run on demand, then through a scheduled task every 15 minutes while the VM is awake. Record what happens when the VM sleeps; this is not a 24/7 availability service.
- Keep output under a bounded rotating local log folder ignored by Git. No credentials in command-line arguments or task definitions.

**Acceptance:** a healthy baseline; a safely triggered low-space warning using a raised threshold; a missing/invalid service; a DNS lookup failure; recovery returning healthy; invalid threshold rejected. Do not fill a disk to test low space. Verify one scheduled result, create a ticket, then document resolution. Reports sent automatically to GLPI are outside v1.

## S3 — New-LabUsers.ps1

**Purpose:** create a small batch of synthetic test users after the owner has created staff manually.

- Target: DC01, using the AD module and an appropriate lab account.
- Inputs: JSON fixture with fictional user IDs/display names/departments, expected domain, and explicit target OU under `OU=TestUsers,OU=YarraLab,DC=corp,DC=yarra,DC=example`.
- Runtime secrets: prompt securely or accept a SecureString from an interactive caller; never store initial passwords in the fixture, logs or repository.
- Preconditions: expected lab domain and OU both match; names valid/unique; every target is within the test OU. Reject other domains and broad/default target locations.
- Use `SupportsShouldProcess`, support `-WhatIf`, and preview each intended operation. Existing users are reported and skipped; never reset their passwords, move them, delete them or alter their access silently.
- Output: created/skipped/failed entries without secrets. A partial failure must be visible; do not report whole-batch success.
- Record IDs created by the current run for a narrowly scoped manual rollback. Do not include an automatic bulk-delete tool in v1.

**Acceptance:** WhatIf creates no objects; valid fixture creates the intended users; repeat run creates no duplicates; invalid domain/OU/name is rejected; an existing account is unchanged; partial failure is clearly reported. Review group assignment separately—do not bulk-create privileged users.

## Script quality and learning

Every script gets help text, a minimal example, prerequisites, output schema, known limits and a real execution record. Meaningful tests exercise invalid input, permissions, read-only behaviour, repeatability and partial failure. Do not add a large framework just to test simple lab scripts. A syntax check is useful but does not prove the AD script works on a live directory.

Have the owner explain one important command and one failure path in each script. Prefer readable code and a small number of parameters to a generic enterprise automation platform.
