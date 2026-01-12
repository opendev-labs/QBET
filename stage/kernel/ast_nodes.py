"""
QBET Abstract Syntax Tree (AST) Nodes
Defines all node types for the parse tree.
"""

class ASTNode:
    """Base class for all AST nodes"""
    pass

# ============= Expressions =============

class NumberLiteral(ASTNode):
    """Numeric literal"""
    def __init__(self, value):
        self.value = value

class StringLiteral(ASTNode):
    """String literal"""
    def __init__(self, value):
        self.value = value

class BooleanLiteral(ASTNode):
    """Boolean literal"""
    def __init__(self, value):
        self.value = value

class NullLiteral(ASTNode):
    """Null literal"""
    pass

class Identifier(ASTNode):
    """Variable or function name"""
    def __init__(self, name):
        self.name = name

class BinaryOp(ASTNode):
    """Binary operation (e.g., a + b)"""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOp(ASTNode):
    """Unary operation (e.g., -a, not b)"""
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class Assignment(ASTNode):
    """Variable assignment"""
    def __init__(self, name, value):
        self.name = name
        self.value = value

class FunctionCall(ASTNode):
    """Function call"""
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class MethodCall(ASTNode):
    """Method call on object (e.g., obj.method())"""
    def __init__(self, object, method, arguments):
        self.object = object
        self.method = method
        self.arguments = arguments

class MemberAccess(ASTNode):
    """Access object member (e.g., obj.property)"""
    def __init__(self, object, member):
        self.object = object
        self.member = member

class ArrayLiteral(ASTNode):
    """Array literal [1, 2, 3]"""
    def __init__(self, elements):
        self.elements = elements

class IndexAccess(ASTNode):
    """Array/object index access"""
    def __init__(self, object, index):
        self.object = object
        self.index = index

# ============= Statements =============

class Program(ASTNode):
    """Root node containing all statements"""
    def __init__(self, statements):
        self.statements = statements

class ExpressionStatement(ASTNode):
    """Statement that is just an expression"""
    def __init__(self, expression):
        self.expression = expression

class Block(ASTNode):
    """Block of statements"""
    def __init__(self, statements):
        self.statements = statements

class IfStatement(ASTNode):
    """If-else statement"""
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class WhileStatement(ASTNode):
    """While loop"""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForStatement(ASTNode):
    """For loop"""
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

class FunctionDeclaration(ASTNode):
    """Function declaration"""
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

class ReturnStatement(ASTNode):
    """Return statement"""
    def __init__(self, value=None):
        self.value = value

class ImportStatement(ASTNode):
    """Import statement"""
    def __init__(self, module, alias=None):
        self.module = module
        self.alias = alias

# ============= Quantum Nodes =============

class QubitCreation(ASTNode):
    """Create a qubit"""
    def __init__(self, name, alpha=1.0, beta=0.0):
        self.name = name
        self.alpha = alpha
        self.beta = beta

class Entanglement(ASTNode):
    """Entangle two qubits"""
    def __init__(self, qubit1, qubit2):
        self.qubit1 = qubit1
        self.qubit2 = qubit2

class Measurement(ASTNode):
    """Measure a qubit"""
    def __init__(self, qubit):
        self.qubit = qubit

class Superposition(ASTNode):
    """Put qubit in superposition"""
    def __init__(self, qubit, states):
        self.qubit = qubit
        self.states = states

# ============= Spiritual Nodes =============

class UniverseCreation(ASTNode):
    """Create a universe"""
    def __init__(self, name):
        self.name = name

class ChakraCreation(ASTNode):
    """Create a chakra"""
    def __init__(self, name, chakra_type, level=50):
        self.name = name
        self.chakra_type = chakra_type
        self.level = level

class EnergyCreation(ASTNode):
    """Create energy"""
    def __init__(self, name, amount, frequency=1.0, vibration=1.0):
        self.name = name
        self.amount = amount
        self.frequency = frequency
        self.vibration = vibration

class KarmaAction(ASTNode):
    """Karma action-consequence"""
    def __init__(self, action, consequence):
        self.action = action
        self.consequence = consequence

class DharmaAction(ASTNode):
    """Dharma purpose"""
    def __init__(self, process, purpose):
        self.process = process
        self.purpose = purpose
