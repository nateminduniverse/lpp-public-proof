# Architecture Summary

## Two-plane MVP

The current Admission Kernel MVP separates two trust roles.

### Control Plane (CP)

The final MVP source contains:
- Authority Registry
- Scope Registry
- Policy Registry
- Permit Issuer
- Artifact Signer
- Revocation Store
- append-only Admission Artifact chain

### Execution Plane (EP)

The final MVP source contains:
- Execution Intent construction
- Permit verification gate
- replay guard
- executor
- CP client boundary

## Gate order in the final MVP

The current `VerifyPermit` path evaluates:

1. Permit present
2. CP signature valid
3. Permit not expired
4. intent-hash binding
5. authority revocation
6. authority expiry
7. authority active state
8. scope-hash currency
9. function in scope
10. target-pattern match
11. policy-hash match
12. nonce replay

A failed check returns DENY with the corresponding implementation reason code.

## Boundary

The MVP implements ADMIT and DENY only. DEFER and COLLAPSE remain protocol-level decisions outside the current executable decision set.
