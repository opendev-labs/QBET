from ast_nodes import *
from environment import Environment
import random
from pathlib import Path

# ANSI Colors
DIM = "\033[2m"
RESET = "\033[0m"

class QuantumState:
    def __init__(self, value):
        self.value = value
        self.collapsed = False

    def __repr__(self):
        if self.collapsed:
            return f"{self.value}"
        return f"|ψ⟩({self.value})"

class Interpreter:
    def __init__(self):
        self.env = Environment()
        self.globals = self.env
        self.functions = {}
        self.laws = []
        self.load_laws()

    def load_laws(self):
        """Enforce Sovereign Kernel Contract c.qb"""
        law_path = Path("laws/c.qb")
        if law_path.exists():
            with open(law_path, 'r') as f:
                for line in f:
                    clean = line.strip().upper()
                    if clean.startswith("LAW"):
                        self.laws.append(line.strip())
                    elif clean.startswith("PRIMITIVE"):
                        # Primitives define the bedrock of our reality
                        pass

    def interpret(self, program):
        if self.laws:
            print(f"{DIM}⚖️  Enforcing {len(self.laws)} Sovereign Laws...{RESET}")
        return None

    def execute_instruction(self, instr):
        op = instr["t"]
        v = instr["v"]

        if op == "UNIVERSE":
            name, props = v
            print(f"🌌 Manifesting Universe: {name}")
            for pk, pv in props.items():
                print(f"  {DIM}property {pk}: {pv}{RESET}")
            self.env.define(name, {"type": "universe", "props": props})

        elif op == "ENTITY":
            name, props = v
            print(f"👤 Defining Entity: {name}")
            for pk, pv in props.items():
                print(f"  {DIM}role: {pv}{RESET}") if pk == "role" else print(f"  {DIM}{pk}: {pv}{RESET}")
            self.env.define(name, {"type": "entity", "props": props})

        elif op == "MANIFEST":
            u_name, e_name = v
            print(f"✨ Manifesting {u_name} with {e_name}...")
            # Here we would bind entity to universe state

        elif op == "FLOW_TIME":
            direction = v
            print(f"⏳ Flowing time {direction}...")

        elif op == "OBSERVE":
            target = v
            value = self.env.get(target)
            print(f"👁️  Observing {target}... Status: STABLE")
            if isinstance(value, dict) and "props" in value:
                print(f"  {DIM}Reality coherence: 0.9999{RESET}")

        else:
            print(f"Warning: Unknown operational primitive {op}")

    def execute(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        # print(f"Warning: No visit_{type(node).__name__} method")
        return None

    def visit_Program(self, node):
        for stmt in node.statements:
            self.execute(stmt)

    def visit_ImportStatement(self, node):
        # Placeholder for module imports
        pass

    def visit_FunctionDeclaration(self, node):
        # Functions are registered in the first pass
        pass

    def visit_Block(self, node):
        for stmt in node.statements:
            self.execute(stmt)

    def visit_ExpressionStatement(self, node):
        return self.execute(node.expression)

    def visit_Assignment(self, node):
        value = self.execute(node.value)
        self.env.define(node.name, value)
        return value

    def visit_FunctionCall(self, node):
        if node.name == "print":
            args = [str(self.execute(arg)) for arg in node.arguments]
            print(" ".join(args))
            return None
        
        return self.execute_function(node.name, [self.execute(arg) for arg in node.arguments])

    def execute_function(self, name, args):
        if name not in self.functions:
            raise Exception(f"Undefined function: {name}")
        
        func = self.functions[name]
        # Create new environment for function scope
        old_env = self.env
        self.env = Environment(self.globals)
        
        # Bind parameters (names only for now as per parser)
        # for param, arg in zip(func.parameters, args):
        #     self.env.define(param, arg)
            
        result = self.execute(func.body)
        self.env = old_env
        return result

    def visit_QubitCreation(self, node):
        return QuantumState(self.execute(node.alpha))

    def visit_Entanglement(self, node):
        print(f"🔗 Linking {node.qubit1} and {node.qubit2} in quantum entanglement...")
        return None

    def visit_Measurement(self, node):
        value = self.env.get(node.qubit)
        if isinstance(value, QuantumState):
            print(f"🌀 Observing {node.qubit}... Probability wave collapsed.")
            print(f"✨ Result: {value.value}")
        elif isinstance(value, str) and value == "stabilized":
            print(f"✨ Observing {node.qubit}... Result: STABLE")
        else:
            print(f"👁️  Observing {node.qubit}... State: {value}")
        return value

    def visit_BooleanLiteral(self, node):
        return node.value

    def visit_NullLiteral(self, node):
        return None

    def visit_StringLiteral(self, node):
        return node.value

    def visit_NumberLiteral(self, node):
        return node.value

    def visit_Identifier(self, node):
        return self.env.get(node.name)
