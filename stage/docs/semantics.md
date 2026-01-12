# QBET Semantics

This document defines the mapping between QBET metaphors and their underlying mechanisms.

## Layered Mapping

| Metaphor | Engine Layer (`engine.qbet`) | Physical Layer (`c.qbet`) |
| :--- | :--- | :--- |
| **Qubit** | `qubit(α, β)` | `c.allocate` + `probabilistic` |
| **Universe** | `universe(name)` | `macro_field` allocation |
| **Observe** | `observe(field)` | `c.collapse` |
| **Karma** | `karma(action, consequence)` | `c.causality.after` |
| **Flow Time** | `flow time forward` | `c.time.tick()` |
| **Entangle** | `entangle(q1, q2)` | `c.causality.entangle` |

## Core Metaphors

### Quantum
- **Superposition**: A field with multiple potential states defined in `engine.qubit`.
- **Collapse**: The transition from potential to realization via `c.collapse`.

### Spiritual
- **Karma**: The causal link between states.
- **Dharma**: The intended purpose of a manifested entity, defining its `c.causality` guards.
- **Chakra**: Localized energy fields (specialized memory allocations).

---

**DEFINED BY opendev-labs**