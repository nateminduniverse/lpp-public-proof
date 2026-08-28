# Current MVP Reason Codes

This file follows the **final supplied MVP implementation**, not earlier draft labels.

| Code | Final MVP trigger / meaning | Six-scenario coverage |
|---|---|---:|
| `OK` | all required checks passed | Yes |
| `NO_PERMIT` | execution requested without a Permit | Yes |
| `SIG_FAIL` | Permit Ed25519 signature invalid | Yes |
| `EXPIRED` | Permit expired | Core verifier |
| `REVOKED` | authority has a revocation timestamp | Yes |
| `AUTHORITY_EXPIRED` | authority expiry is in the past | Core verifier |
| `AUTHORITY_NOT_ACTIVE` | authority missing or state not ACTIVE | Core verifier / source paths |
| `SCOPE_FAIL` | scope hash, function or target check failed | Yes |
| `INTENT_MISMATCH` | Permit intent hash does not match current Execution Intent | Core verifier / source tests |
| `POLICY_MISMATCH` | Permit policy hash does not match current policy hash | Core verifier |
| `REPLAY` | Permit nonce has already been consumed | Yes |
| `INTERNAL_ERROR` | CP unreachable or unexpected internal failure | Source path |

## Artifact behavior

In the final MVP application code, disclosed ADMIT and DENY decision paths create signed Admission Artifacts. This includes the current `NO_PERMIT` and `SIG_FAIL` execution-gate rejections.

## Draft reconciliation

Earlier design documents may contain different or provisional reason-code labels. Public Proof v2.0 intentionally follows the final implementation package for implementation-specific evidence.
