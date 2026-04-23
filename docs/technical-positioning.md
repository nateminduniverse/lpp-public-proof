# Technical Positioning

## Purpose of this document

This document clarifies what the **LPP Admission Kernel MVP** is intended to do, what it is **not** intended to replace, and how it should be understood relative to existing open-source systems such as:

- OPA (Open Policy Agent)
- AWS Cedar
- SPIFFE / SPIRE
- Macaroons
- Biscuit

The goal is not to dismiss those systems.  
The goal is to explain that they primarily address **identity**, **authorization**, **policy evaluation**, or **delegated permission transport**, while the LPP Admission Kernel is positioned as a **pre-execution admissibility layer** for AI-triggered execution.

---

## Short definition

**LPP Admission Kernel is not a generic policy engine, not a workload identity framework, and not a token format.**

It is a governance boundary intended to answer a different upstream question:

> Before lower-layer policy enforcement is applied, is this AI-triggered action qualified to exist at all?

This is the core distinction between:

- **authorization**
- **execution governance**
- **constitutional admissibility**

---

## The problem being addressed

Many mature systems already solve important lower-layer security and authorization problems well.

Examples include:

- identifying workloads
- issuing trustable identities
- expressing authorization policies
- evaluating allow/deny decisions
- carrying delegated permissions in signed tokens
- producing logs and audit trails

Those are real and necessary capabilities.

However, in AI-triggered execution systems, a further upstream problem appears:

- an AI-generated execution intent may be syntactically valid
- identity may be present
- policy evaluation may succeed
- a token may be valid
- and yet the action may still lack a sufficiently defined **legitimacy boundary**

The LPP Admission Kernel is intended to define that upstream boundary.

It is designed around the claim that:

> For consequential AI-triggered execution, policy pass alone is not the full governance question.

---

## What existing systems generally answer

### 1. Identity systems

Identity-oriented systems answer questions such as:

- Who is this workload?
- Is the calling service identity valid?
- Can this workload prove membership in a trust domain?

These systems are essential for establishing machine identity and trust anchors for workloads.

They do **not**, by themselves, define whether an AI-triggered action is **admissible as a governance event**.

---

### 2. Authorization policy systems

Authorization systems answer questions such as:

- Should this request be allowed under current policy?
- Does this principal have permission to perform this action?
- Does the request satisfy the policy conditions?

These systems are essential for runtime allow/deny decisions.

They do **not**, by themselves, define whether the policy-governed action is grounded in a higher-order admissibility boundary.

---

### 3. Delegated permission token systems

Token-based authorization schemes answer questions such as:

- How are permissions carried?
- How can delegated permissions be attenuated?
- How can authorization be verified offline or across boundaries?

These systems are essential for portable, constrained authorization.

They do **not**, by themselves, define whether an AI-triggered action should be considered legitimate enough to instantiate prior to downstream enforcement.

---

## What LPP Admission Kernel is intended to answer

LPP Admission Kernel is intended to answer a narrower but more upstream question:

> Is this AI-triggered execution event admissible before lower-layer authorization and enforcement proceed?

This means the kernel is concerned with:

- authority state
- scope binding
- revocation awareness
- execution qualification
- reconstructable evidence of admission decision
- the difference between **policy success** and **governance sufficiency**

In this framing, the kernel is not trying to replace downstream security systems.  
It is trying to define the **entry condition** under which AI-triggered execution should be treated as legitimate enough to proceed into those systems.

---

## Layered interpretation

The simplest way to understand the distinction is by layer.

| Layer | Primary concern | Typical examples | Main question |
|---|---|---|---|
| Identity layer | workload / service identity | SPIFFE / SPIRE | Who is this caller? |
| Authorization policy layer | allow / deny evaluation | OPA / Cedar | Should this request be allowed under policy? |
| Permission transport layer | delegated / attenuated authorization | Macaroons / Biscuit | How is constrained permission carried and verified? |
| Admissibility layer | qualification before execution | LPP Admission Kernel | Is this AI-triggered action qualified to exist before enforcement? |

This is the intended positioning of the LPP Admission Kernel.

---

## Why this matters for AI-triggered execution

Traditional security architecture usually assumes that:

- the caller is already a recognized principal
- the request is already properly framed as a normal authorization subject
- the key question is whether policy should allow or deny it

In AI-triggered systems, an additional difficulty appears:

- the action may originate from model-generated reasoning or agent-generated intent
- the path between language output and executable action becomes more direct
- the governance question is no longer only “is this call permitted?”
- it also becomes “what makes this action a legitimate candidate for instantiation in the first place?”

That is where LPP Admission Kernel is positioned.

It is intended to treat AI-triggered execution not merely as a request to authorize, but as an event that may require a prior admissibility determination.

---

## Core conceptual distinction

### Existing lower-layer framing

A mature lower-layer stack often works like this:

1. establish identity
2. evaluate policy
3. verify token or credentials
4. allow or deny execution
5. log the result

This is correct and necessary.

### LPP Admission Kernel framing

The LPP framing inserts an upstream question:

1. determine whether the AI-triggered action is admissible
2. bind authority and scope to the execution intent
3. produce an admission decision
4. produce reconstructable evidence of that decision
5. only then allow downstream authorization and execution handling

In this interpretation:

- downstream systems still matter
- policy still matters
- identity still matters
- tokens still matter

But they are not treated as the whole governance boundary.

---

## What LPP Admission Kernel does not claim

The public MVP does **not** claim that the kernel replaces:

- OPA
- Cedar
- SPIFFE / SPIRE
- Macaroons
- Biscuit
- enterprise IAM
- runtime sandboxing
- existing policy engines
- general-purpose service authorization systems

It also does **not** claim that lower-layer systems are insufficient in their own domain.

Those systems are mature because they solve their own layer well.

The LPP claim is narrower:

> For AI-triggered execution, there exists an upstream admissibility problem that is not exhausted by identity, policy, or token validation alone.

---

## What the MVP is actually trying to prove

This MVP is not trying to prove that a new policy engine is needed.

It is trying to prove that the following structure is coherent and implementable:

- authority-aware admission
- non-bypassable execution gate
- revocation-aware decisioning
- signed admission artifact generation
- reconstructable evidence chain

The proof objective is architectural:

- that pre-execution admissibility can be modeled
- that it can be enforced through a chokepoint
- that both ADMIT and DENY can become reconstructable artifacts
- that the governance question can be framed above lower-layer authorization machinery

---

## Comparison summary

### OPA / Cedar
OPA and Cedar are best understood as systems for policy expression and policy evaluation.

They are strong at answering:

- what policy says
- whether a request matches policy
- whether access should be allowed or denied

LPP Admission Kernel is not trying to be a better policy language.

It is positioned as asking:

- what makes the AI-triggered action a valid admissibility subject before policy enforcement becomes the decisive step?

---

### SPIFFE / SPIRE
SPIFFE / SPIRE are best understood as workload identity infrastructure.

They are strong at answering:

- who the workload is
- whether the workload identity can be trusted
- whether trust-domain identity can be established

LPP Admission Kernel is not trying to replace workload identity.

It is positioned as asking:

- once identity is known, what makes the AI-triggered execution event itself admissible?

---

### Macaroons / Biscuit
Macaroons and Biscuit are best understood as portable, attenuable authorization token mechanisms.

They are strong at answering:

- how delegated permission is carried
- how constraints are embedded
- how authorization can be verified and attenuated

LPP Admission Kernel is not trying to be a superior token primitive.

It is positioned as asking:

- even if a valid token exists, should this AI-triggered action be considered legitimate enough to instantiate as an execution event?

---

## Practical interpretation

A practical engineering interpretation of LPP Admission Kernel is:

- it can sit above policy and enforcement
- it can bind authority and scope before action
- it can convert admission into a signed evidence object
- it can provide a governance checkpoint before execution becomes runtime reality

In that sense, it is intended to complement lower-layer systems, not erase them.

The intended relationship is:

- **identity systems** identify
- **policy systems** decide permissions
- **token systems** transport constrained rights
- **LPP Admission Kernel** determines whether the AI-triggered execution event should enter that decision path as an admissible governance subject

---

## Why this document exists in the public proof edition

This public proof repository is intentionally limited.  
It does not include full implementation disclosure.

Because of that, technical readers may otherwise assume the project is simply restating already mature authorization practice.

This document exists to state clearly:

- the project is aware of existing lower-layer authorization and identity systems
- the project is not claiming novelty by ignoring them
- the intended distinction is a layer distinction, not a generic “we are better” claim
- the public proof edition should be evaluated as a claim about **admissibility framing**, not as a replacement package for existing security infrastructure

---

## Bottom line

The core technical positioning is:

> OPA, Cedar, SPIFFE / SPIRE, Macaroons, and Biscuit solve important lower-layer problems in policy, identity, and delegated authorization.

> LPP Admission Kernel is intended to define the admissibility boundary above those layers for AI-triggered execution.

That is the intended difference.

It is a difference in **governance layer**, not merely a difference in syntax, tooling, or implementation detail.
