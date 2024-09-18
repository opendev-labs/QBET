# QBET Syntax Rules

## 1. Basic Syntax Structure

### Quantum Spiritual Way
The syntax of QBET is like the cosmic dance of the universe, where each element has its place and purpose, creating harmony and balance.

### Normal Way
1. **Statements**: End with a semicolon (`;`). Define how statements are structured in QBET, including assignment, function call, and return statements.
2. **Expressions**: Describe the rules for forming expressions, including operator precedence and associativity.
3. **Blocks**: Defined using curly braces `{}`. Explain how code blocks are defined and used, specifying if they are delimited by braces or indentation.
4. **Comments**: Single-line comments start with `//`, multi-line comments are enclosed in `/* */`.

## 2. Data Types

### Quantum Spiritual Way
Data types in QBET are like the elements of nature, each with its unique essence, contributing to the wholeness of the program.

### Normal Way
- **Primitive Types**: List and describe the basic data types (e.g., integers, floats, strings) with examples.
  ```qbet
  int x = 10;
  float y = 20.5;
  string name = "QBET";
```
Complex Types: Introduce complex data types (e.g., arrays, objects) and explain their declaration and access.
```qbet
int[] numbers = {1, 2, 3, 4, 5};
object person = {name: "Alice", age: 30};
```
3. Variables
Declaration: Syntax for declaring variables.
```qbet
int x;
```
Initialization: Rules for initializing variables.
```qbet
int x = 10;
```
Scope: Explain variable scope and lifetime, differentiating between local, global, and block scope.

### 4. Operators
Quantum Spiritual Way
Operators in QBET are the forces of nature, guiding the flow of energy and interactions within the program.

Normal Way
Arithmetic Operators: Define operators for arithmetic operations with examples.
```qbet
int sum = a + b;
```
Logical Operators: Describe logical operators and their usage, specifying short-circuit behavior.
```qbet
bool result = (a > b) && (c < d);
```
Comparison Operators: Explain operators for comparison and any type coercion rules.
```qbet
bool isEqual = (a == b);
```
### 5. Control Structures
Conditionals: Syntax for if-else statements, including nested examples.
```qbet
if (x > 5) {
    print("x is greater than 5");
} else {
    print("x is not greater than 5");
}
```
Loops: Describe loops (e.g., for, while) and their syntax with examples.
```qbet
for (int i = 0; i < 10; i++) {
    print(i);
}
```
Switch Statements: Explain switch-case syntax and mention if fall-through behavior is allowed.
```qbet
switch (day) {
    case 1:
        print("Monday");
        break;
    case 2:
        print("Tuesday");
        break;
    default:
        print("Other day");
}
```
6. Functions
Definition: Syntax for defining functions.
```qbet
function add(int a, int b) {
    return a + b;
}
```
Parameters: Rules for passing parameters, including default parameters and variadic functions if supported.
```qbet
function greet(string name = "Guest") {
    print("Hello, " + name);
}
```
Return Values: Explain how functions return values, including multiple values if supported.
```qbet
function getCoordinates() {
    return (x, y);
}
```
### Semantics of QBET
1. **Execution Model**
Evaluation Order: Describe the order in which expressions are evaluated, including operator precedence and function call evaluation.
Function Calls: Explain how function calls are handled, including argument passing (by value or reference).
2. **Type System**
Static vs. Dynamic Typing: Define whether QBET uses static or dynamic typing and provide examples.
Type Inference: Explain how types are inferred with examples.
3. **Memory Management**
Allocation: Describe how memory is allocated for variables and objects, including stack vs. heap allocation if relevant.
Garbage Collection: Explain the garbage collection mechanism, describing the algorithm used (e.g., reference counting, mark-and-sweep).
4. **Error Handling**
Exceptions: Syntax and semantics for handling exceptions, including try-catch blocks.
```qbet
try {
    // code that may throw an exception
} catch (Exception e) {
    print(e.message);
}
```
Error Propagation: Explain how errors propagate through the program and how uncaught exceptions are handled.
5. **Concurrency**
Threads and Processes: Describe how QBET handles concurrency with examples of creating and managing threads or processes.
```qbet
thread t = new Thread(function() {
    // code to run in a new thread
});
t.start();
```
Synchronization: Explain mechanisms for synchronizing concurrent tasks, such as mutexes or semaphores.
```qbet
mutex m = new Mutex();
m.lock();
// critical section
m.unlock();
```
### Examples
1. Hello World
```qbet
print("Hello, World!");
```
2. Variable Declaration and Initialization
```qbet
int x = 10;
float y = 20.5;
string name = "QBET";
```
3. Conditional Statement
```qbet
if (x > 5) {
    print("x is greater than 5");
} else {
    print("x is not greater than 5");
}
```
4. Loop Example
```qbet
for (int i = 0; i < 10; i++) {
    print(i);
}
```
5. Function Definition
```qbet
function add(int a, int b) {
    return a + b;
}
```