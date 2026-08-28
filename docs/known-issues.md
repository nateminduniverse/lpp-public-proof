# Known MVP Implementation Limitation

## Mutable in-memory authority snapshot after revocation

Source inspection of the final supplied MVP identified an implementation-level snapshot-aliasing risk in the current in-memory artifact chain.

During the Control Plane proposal path, an Authority Record snapshot may be stored by reference to the live in-memory registry object. A later revocation mutates that registry object. As a result, a previously created in-memory artifact entry may subsequently reflect the newer `REVOKED` Authority Record even though its `authority_state_hash` was computed and signed against the earlier `ACTIVE` state.

The persisted append-only `artifacts.jsonl` record is serialized at artifact creation time and therefore preserves the original Authority Record snapshot.

This condition was identified from implementation inspection. The static evidence capture included in this release does not independently demonstrate the mismatch in every run.

Public reconstructability evidence in this release therefore treats the persisted append-only JSONL representation as the canonical captured evidence source.

Recommended implementation repair: deep-copy immutable snapshots before storing them in the in-memory artifact chain, so later authority-state mutations cannot alter previously created in-memory evidence representations.

This is an implementation-level limitation and does not change LPP protocol semantics.
