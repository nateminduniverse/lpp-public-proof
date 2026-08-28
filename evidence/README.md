# Evidence

This directory contains release-specific evidence generated from the final supplied MVP package.

## Provenance

- source archive hash: `source-package-sha256.txt`
- build/test metadata: `run-metadata.json`
- observed six-scenario summary: `observed-summary.json`
- machine-readable status: `validation-manifest.json`

## Raw test outputs

- `test-runs/unittest-suite.txt`
- `test-runs/standalone-core-verification.txt`
- `test-runs/unittest-environment-note.md`

## Captured public run

`public-run/scenarios/` contains isolated scenario inputs, observed responses, persisted `artifact_log.jsonl` records, in-memory `/chain` captures, authority/scope/policy snapshots, and replay state.

For reconstructability checks, the persisted append-only JSONL record is treated as the canonical captured evidence because source inspection identified an in-memory snapshot-aliasing risk described in `docs/known-issues.md`.

A fresh CP signing key was generated for the evidence run after the uploaded source package was copied into a temporary build directory. Only the public key is included here. The source package's bundled key files were not reused or published.
