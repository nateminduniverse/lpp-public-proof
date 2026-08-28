# Validation Status — Public Proof v2.0

## Final source package

`admission-kernel-mvp-final.tar(1).gz`

SHA-256:

`84f901d8d170b5f4110149ce287ab1d722749581ac922151c92a578488bce2d5`

## Evidence states

> **Specified ≠ Implemented ≠ Validated ≠ Independently Reproduced**

Current public interpretation:

- protocol architecture: specified
- bounded Admission Kernel MVP: implemented
- disclosed ADMIT/DENY paths: internally validated within current MVP scope
- Public Proof v2.0: controlled technical evidence released
- independent external reproduction: not yet completed
- production validation: not claimed

## Track A — Six Core Execution Scenarios

| ID | Scenario | Expected | Observed | Artifact count in isolated captured run |
|---|---|---|---|---:|
| EX-01 | Valid execution | `ADMIT / OK` | `ADMIT / OK` | 2 |
| EX-02 | No Permit | `DENY / NO_PERMIT` | `DENY / NO_PERMIT` | 1 |
| EX-03 | Scope violation | `DENY / SCOPE_FAIL` | `DENY / SCOPE_FAIL` | 1 |
| EX-04 | Permit tampering | `DENY / SIG_FAIL` | `DENY / SIG_FAIL` | 2 |
| EX-05 | Replay | second execution `DENY / REPLAY` | second execution `DENY / REPLAY` | 3 |
| EX-06 | Post-revocation execution | `DENY / REVOKED` | `DENY / REVOKED` | 2 |

Why some counts exceed one: the Control Plane proposal decision and the later execution decision are separate admission/evidence events in the final MVP.

## Source test suite

The final source package contains **26 unittest test methods** across seven test files.

Release-builder compatibility run:

**26/26 PASS**

The raw output is in `evidence/test-runs/unittest-suite.txt`.

## Standalone core verification

The final package also contains `verify_core.py`, which is designed to run without Flask and exercises core invariants directly.

Release result:

**49/49 PASS**

Raw output: `evidence/test-runs/standalone-core-verification.txt`.

## Environment note

The release builder was offline and did not have the Flask package available. To execute the source application's 26-test test-client contract, the build used a local minimal compatibility shim implementing only the Flask APIs required by the tests (`Flask`, routing, test client, `request.get_json`, and `jsonify`).

This is evidence for the application logic exercised by the source tests, **not** validation of Flask itself or a production HTTP deployment. The standalone 49-check core verifier ran natively against the final source package with standard library + `cryptography`.

Independent users should rerun the original source suite with Flask 3.x as specified by the MVP README when they have access to the private runnable package.

## Track B — Artifact Verification / Audit Reconstruction

Track B is separate from the six execution scenarios.

Current MVP endpoint checks six direct reconstruction properties; replay and revocation are validated through execution/state paths. See `docs/artifact-verification.md`.

## Known implementation limitation

Source inspection of the final supplied MVP identified a mutable in-memory Authority Record snapshot-aliasing risk after later revocation. The persisted append-only JSONL record is serialized at artifact creation time and remains the canonical captured evidence source for this release. The static evidence capture does not independently demonstrate the mismatch in every run. See `docs/known-issues.md`.

Public Proof v2.0 therefore bases artifact reconstruction evidence on the persisted JSONL entries rather than claiming that the current in-memory `/chain` representation is immutable under later authority-state mutation.

## Non-claims

This release does not establish:
- independent reproduction
- production readiness
- universal non-bypassability across arbitrary infrastructure
- distributed replay consistency
- comprehensive continuous mid-execution revocation
- full DEFER/COLLAPSE implementation
- universal AI safety or alignment
