# Fifth-Color Demand Theory (FCD Theory)

## A Foundational Framework for Studying the Origin, Propagation, and Uniqueness of Fifth-Color Demand

> **Status:** Research Framework (Version 0.1)

## Abstract

This document proposes a research framework named **Fifth-Color Demand Theory (FCD Theory)**. Rather than attempting to directly re-prove the Four Color Theorem, the framework introduces new mathematical objects centered on the concept of *fifth-color demand* and studies their structural properties.

The objective is to build a rigorous theory from definitions to conjectures, providing a foundation for future proofs or counterexamples.

---

# 1. Motivation

Classical four-color research focuses on:

- Critical graphs
- Kempe chains
- Reducible configurations
- Discharging

FCD Theory instead asks:

> Where does the necessity of a fifth color originate?
>
> How does it propagate?
>
> Can multiple independent fifth-color demands coexist?

---

# 2. Core Objects

Before introducing the global framework, several classical notions used by this theory must be fixed.

### Classical notions required by this framework

- Girth: the length of the shortest simple cycle in a graph.
- Degree: the number of incident edges at a vertex.
- 3-regular (cubic): every vertex has degree exactly 3.
- Unavoidable configuration: a local configuration that must appear in every graph of a specified class.
- Unavoidable set: a family of configurations such that every graph in the target class contains at least one of them.

These notions are not invented by FCD Theory, but FCD Theory uses them as structural constraints on the existence and propagation of fifth-color demand.

## Definition 2.1 Color Demand

Given a graph G and a partial 4-coloring φ,

D(v,φ) denotes the set of colors still available to vertex v.

---

## Definition 2.2 Fifth-Color Demand

If D(v,φ)=∅, vertex v is said to exhibit a fifth-color demand.

This is a local property.

---

## Definition 2.3 Coloring State Space (recommended refinement)

Instead of quantifying over all Kempe exchanges directly, define a state graph whose vertices are valid coloring states and whose edges correspond to one Kempe exchange.

All global notions are defined on this state space.

---

# 3. Kempe Obstruction

Define the obstruction responsible for preventing elimination of fifth-color demand.

Possible quantitative parameters include:

- obstruction strength
- obstruction depth
- obstruction radius

---

# 4. Obstruction Propagation

If a fifth-color demand at u forces demand at v, define

u → v.

The resulting directed graph is the Obstruction Propagation Graph.

---

# 5. Fifth-Color Core

Define C₅(G) as the set of vertices participating in persistent fifth-color demand.

Research questions:

- Is C₅ connected?
- Is C₅ unique?
- Is C₅ small?

---

# 6. Potential Function

Define a graph potential Φ(G).

Candidate:

Φ(G)=Σ I(F(v))

where I is the indicator of fifth-color demand.

Long-term objective:

Show Kempe transformations monotonically decrease Φ.

---

# 7. Central Conjecture

## Fifth-Color Core Uniqueness Conjecture

For planar graphs with girth ≥ 4,

|C₅(G)| ≤ 1

Refined target in the current framework:

For planar graphs with girth at least 5, at most one vertex can exhibit persistent fifth-color demand.

Important:

This is currently a conjecture, **not a theorem**.

---

# 8. Proposed Research Route

Euler Formula

↓

Average Degree Bound

↓

Abundance of Low-Degree Vertices

↓

Kempe Obstruction

↓

Propagation Graph

↓

Uniqueness of Fifth-Color Core

↓

Four Color Theorem (possible application)

---

# 9. Guiding Principles

- Separate definitions from conjectures.
- Prefer structural theory over proof-first approaches.
- Build computable mathematical objects.
- Treat the Four Color Theorem as an application rather than the starting point.

---

# 10. Roadmap

## Volume I — Foundations

Definitions, state space, invariants.

## Volume II — Structure

Propagation, potentials, uniqueness conditions.

## Volume III — Applications

Critical graphs, minimal counterexamples, and applications to planar graph coloring.

---

# Notes

This framework is exploratory and intentionally avoids claiming unproven results. Every conjecture should be validated through rigorous proof or explicit counterexample.
