# Migration Notes — Existing Public Proof → v2.0

## Replace / update

Recommended replacement files:
- `README.md`
- `PUBLIC_RELEASE_CHECKLIST.md`
- `docs/public-overview.md`
- `docs/architecture-summary.md`
- `docs/public-scope.md`
- `docs/technical-positioning.md`
- `docs/validation-status.md`
- `docs/ip-notice.md`

## Add

- `docs/decision-model.md`
- `docs/reason-codes.md`
- `docs/artifact-verification.md`
- `docs/known-issues.md`
- `schemas/`
- `validation/`
- `examples/`
- `evidence/`
- `tools/verify_evidence.py`
- `requirements-public-proof.txt`
- `RELEASE_NOTES_v2.0.md`

## Preserve if already canonical/current

Existing repository documents not duplicated by this release may remain, including broader research, project provenance, and public governance-stack material, provided their claims do not conflict with v2.0 validation status.

## Important supersession rule

Do not publish the earlier draft Public Proof v2.0 package generated from `admission-kernel-mvp.zip`. This release is rebuilt against `admission-kernel-mvp-final.tar(1).gz` and supersedes it.
