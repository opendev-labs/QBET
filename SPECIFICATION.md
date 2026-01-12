# QBET v0.1 Formal Specification

This document defines the formal grammar and operational semantics for QBET version 0.1, focusing on the core manifestation and observation logic.

## 1. Scope
QBET v0.1 targets **semantic manifestation**. It provides the fundamental primitives required to declare potential states and observe their collapse within a controlled execution field (qvenv).

## 2. Lexical Grammar

### Keywords
- `manifest`, `use`, `function`, `state`, `observe`, `flow`, `bind`, `universe`, `within`, `when`, `collapse`, `into`

### Literals
- **String**: Enclosed in matching double quotes (`"`).
- **Number**: Integer or floating-point values.
- **Identifier**: Alphanumeric sequence starting with a letter or underscore.

---

## 3. Syntactic Grammar (EBNF)

```ebnf
program      = { statement } ;
statement    = manifest_stmt | use_stmt | func_stmt | state_stmt | flow_stmt | if_stmt | expr_stmt ;

manifest_stmt = "manifest" identifier [ "within" identifier ] block ;
use_stmt      = "use" identifier ;
func_stmt     = "function" identifier "(" [ params ] ")" block ;
state_stmt    = "state" identifier "=" expression ;
flow_stmt     = "flow" "time" ( "forward" | "backward" | "still" ) ;

block         = "{" { statement } "}" ;

expression    = call_expr | superposition | primary ;
superposition = "superposition" "(" params ")" ;
call_expr     = identifier "(" [ params ] ")" ;
primary       = identifier | string | number | "observe" expression ;
```

---

## 4. Operational Semantics

### The Reality State ($\mathcal{R}$)
A QBET program executes within a Reality State $\mathcal{R}$, which is a mapping of identifiers to **Potential Fields** ($\mathcal{P}$).

### $\text{manifest}(I)$
Declares an intention $I$ in $\mathcal{R}$. $I$ is added to the set of manifested entities. If executed within a universe $U$, it creates a child relationship $I \subset U$.

### $\text{state } x = \mathcal{P}$
Assigns a Potential Field $\mathcal{P}$ to identifier $x$. 
- If $\mathcal{P}$ is a single value, it is **collapsed** by default.
- If $\mathcal{P}$ is a `superposition(v1, v2, ...)`, $x$ remains in an **uncollapsed** state.

### $\text{observe } x$
Triggers a **Wavefunction Collapse** of the potential field assigned to $x$.
1. Access the Potential Field $\mathcal{P}$ associated with $x$.
2. If $\mathcal{P}$ is in superposition, select a value $v \in \mathcal{P}$ based on the probability distribution (default: uniform).
3. Replace $\mathcal{P}$ with $v$ in $\mathcal{R}$.
4. Return $v$.

### $\text{flow time forward}$
Advances the causal state of all manifested entities. In v0.1, this primarily serves as a semantic marker for the transition from declaration to execution.

---

## 5. Domain Bindings

Domains are mapped metaphor $\to$ mechanism via the `use` directive:
- `use core`: Logic, Math, IO.
- `use quantum`: Advanced superposition and interference logic.

---

**LOCKED FOR v0.1**  
**Finalized by opendev-labs**
