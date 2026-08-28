# Public Release Checklist — v2.0

## Provenance
- [x] Final MVP archive identified
- [x] Source SHA-256 pinned: `84f901d8d170b5f4110149ce287ab1d722749581ac922151c92a578488bce2d5`
- [x] Evidence generated from a temporary copy of the final package
- [x] Source-package bundled key material not reused in public evidence run

## Technical evidence
- [x] Exact five final-MVP JSON Schemas included
- [x] Current reason-code map included
- [x] Six core execution scenarios captured
- [x] Application source test inventory counted: 26
- [x] Release-builder compatibility test run: 26/26 PASS
- [x] Standalone core verification: 49/49 PASS
- [x] Public evidence verifier: 113/113 PASS
- [x] Artifact Verification separated from execution-scenario validation

## Disclosure safety
- [x] No private key intentionally copied to release
- [x] No full runnable Admission Kernel source copied
- [x] No complete private test harness copied
- [x] Public examples use synthetic test data
- [x] Public / private boundary documented

## Claim discipline
- [x] ADMIT/DENY distinguished from DEFER/COLLAPSE
- [x] Protocol specification distinguished from current MVP implementation
- [x] Internal validation distinguished from independent reproduction
- [x] Production readiness not claimed
- [x] Current MVP artifact-verifier six-check boundary documented
- [x] In-memory snapshot-aliasing limitation disclosed; persisted JSONL used for reconstruction evidence
