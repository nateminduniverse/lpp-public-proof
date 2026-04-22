# Architecture Summary

## Core model

The public MVP architecture is defined by three structural ideas:

1. **Authority is evaluated upstream**
2. **Execution is gated before action**
3. **Every decision leaves reconstructable evidence**

## Plane separation

### Control Plane
The control side is responsible for:
- authority state
- scope definition
- policy reference
- permission issuance
- artifact signing
- revocation state

### Execution Plane
The execution side is responsible for:
- accepting execution intents
- enforcing a mandatory gate
- checking whether execution may proceed
- producing the execution-side outcome that can be bound to an admission artifact

## Chokepoint principle

No execution path should bypass the verification gate.

This is the central engineering proof point of the MVP.

## Publicly disclosed invariant level

The public edition discloses the following invariant-level claims only:

- no execution without a valid permit-equivalent authority result
- no silent bypass around the execution gate
- revocation must be enforceable
- both ADMIT and DENY should be representable as structured artifacts

## Deliberately withheld detail

This public edition does not disclose:
- full API contracts
- full object schemas
- full verification internals
- exact implementation-specific storage conventions
- internal engineering patches and handoff details
