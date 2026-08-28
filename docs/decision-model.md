# Decision Model

## Protocol model

LPP defines four Layer 0 decisions:

- `ADMIT`
- `DENY`
- `DEFER`
- `COLLAPSE`

## Current MVP implementation

The final Admission Kernel MVP schema and executable paths implement:

- `ADMIT`
- `DENY`

`DEFER` and `COLLAPSE` are not present in the current MVP Admission Artifact decision enum and are not claimed as implemented or validated here.

## Execution implication

Only an admitted path may carry a valid signed Execution Permit into the execution boundary.

An Execution Permit does not create upstream legitimacy; it carries an existing admission decision into the execution gate.
