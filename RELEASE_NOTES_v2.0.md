# Release Notes — Public Proof v2.0

## Controlled Technical Evidence Release

Public Proof v2.0 is rebuilt against the final Admission Kernel MVP archive (`84f901d8d170…`).

### Added
- exact final-MVP public schemas
- final implementation reason-code map
- six isolated execution-scenario captures
- signed Permit and Admission Artifact examples
- evidence-run CP public key
- application source test run output
- standalone 49-check core verification output
- public evidence verifier and machine-readable manifest

### Corrected from the earlier draft Public Proof build

The final MVP package differs materially from the earlier package used for the first draft release:

1. The final implementation emits signed Admission Artifacts for the disclosed `NO_PERMIT` and `SIG_FAIL` DENY paths.
2. `POLICY_MISMATCH` is present in the final implementation gate and schema.
3. The final package includes a 26-test application suite and an 8-test Artifact Verification file.
4. The final MVP artifact verifier directly implements six reconstruction checks; broader replay/revocation verification remains represented through execution/state evidence.
5. Source inspection of the final MVP identified a mutable in-memory authority-snapshot aliasing risk after later revocation. Persisted JSONL evidence is unaffected and is used as the canonical captured reconstruction source; see `docs/known-issues.md`.

This v2.0 package supersedes the earlier draft Public Proof v2.0 generated from the non-final MVP archive.
