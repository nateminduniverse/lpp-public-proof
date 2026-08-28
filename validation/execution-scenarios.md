# Six Core Execution Scenarios

| ID | Scenario | Trigger | Expected | Observed |
|---|---|---|---|---|
| EX-01 | Valid execution | active authority + valid in-scope intent + valid Permit | `ADMIT / OK` | `ADMIT / OK` |
| EX-02 | No Permit | execution path invoked without Permit | `DENY / NO_PERMIT` | `DENY / NO_PERMIT` |
| EX-03 | Scope violation | function outside authorized scope | `DENY / SCOPE_FAIL` | `DENY / SCOPE_FAIL` |
| EX-04 | Permit tampering | signed Permit field modified after issuance | `DENY / SIG_FAIL` | `DENY / SIG_FAIL` |
| EX-05 | Replay | same Permit/nonce submitted after a successful execution | second execution `DENY / REPLAY` | second execution `DENY / REPLAY` |
| EX-06 | Post-revocation execution | authority revoked after Permit issuance | `DENY / REVOKED` | `DENY / REVOKED` |

Captured isolated-run evidence is under `../evidence/public-run/scenarios/`.

The final MVP records signed Admission Artifacts for the disclosed ADMIT/DENY decisions. Proposal and execution decisions are recorded separately, so an isolated scenario may contain multiple linked artifacts.
