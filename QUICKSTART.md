# QBET Quick Start Guide

## Installation
```bash
cd /home/cube/Gh-sync/opendev-labs/QBET
chmod +x src/qbet.py
```

## Run the REPL
```bash
python3 src/qbet.py
```

## Run Examples
```bash
# Hello Universe - Basic introduction
python3 src/qbet.py examples/hello_universe.qbet

# Quantum Computing Demo
python3 src/qbet.py examples/quantum_demo.qbet

# Fibonacci & Sacred Geometry
python3 src/qbet.py examples/fibonacci_spiral.qbet

# Spiritual Algorithm
python3 src/qbet.py examples/spiritual_algorithm.qbet

# Comprehensive Demo
python3 src/qbet.py examples/comprehensive_demo.qbet
```

## Quick Examples

### Variables & Functions
```qbet
x = 42
name = "Quantum Seeker"

function greet(person) {
    return "Namaste, " + person
}

print(greet(name))
```

### Quantum Computing
```qbet
qubit q
hadamard(q)
result = measure(q)
print("Measured: " + string(result))
```

### Spiritual Functions
```qbet
phi = golden_ratio()
fib = fibonacci(10)
chakra root
balance_chakra(root)
manifest("abundance")
```

## Help
Type `help` in the REPL for more information.
