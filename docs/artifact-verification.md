# Admission Artifact Verification

## Current MVP verifier endpoint

The final MVP `/artifact/<id>/verify` path performs six mechanical checks:

1. `cp_signature`
2. `policy_hash`
3. `authority_state_hash`
4. `scope_hash`
5. `result_hash`
6. `chain_linkage`

The final MVP source test suite includes eight Artifact Verification tests covering valid artifacts, signature tampering, decision mutation, policy-snapshot tampering, authority-snapshot tampering, multi-artifact chain linkage, broken linkage, and the genesis hash.

## Protocol-level specification boundary

The broader Admission Artifact Verification specification describes seven verification categories, including replay and revocation checks.

Public Proof v2.0 does **not** collapse these two layers into one claim. In the current MVP:

- artifact verifier endpoint: six direct reconstruction checks
- replay: validated through nonce/gate execution paths
- revocation: validated through authority-state/gate execution paths

Artifact Verification remains a separate validation track from the six core execution scenarios.
