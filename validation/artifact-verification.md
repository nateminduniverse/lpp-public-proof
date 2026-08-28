# Artifact Verification / Audit Reconstruction

This is a separate evidence track from the six core execution scenarios.

## Current MVP direct verifier checks

| Check | Current MVP endpoint |
|---|---:|
| CP signature | Implemented |
| Policy hash | Implemented |
| Authority-state hash | Implemented |
| Scope hash | Implemented |
| Execution-result hash | Implemented |
| Previous-artifact chain linkage | Implemented |

## Adjacent execution/state verification

| Property | Current evidence path |
|---|---|
| Replay | EX-05 + replay nonce state |
| Revocation | EX-06 + authority state / revoked_at |

The broader protocol-level verification specification contains seven categories. Public Proof v2.0 preserves the distinction between that specification and the current MVP endpoint implementation.
