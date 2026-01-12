"""
QBET Interpreter
Executes the Abstract Syntax Tree.
"""

from ast_nodes import *
from environment import Environment
from qbet_types import *
from lexer import TokenType
from errors import RuntimeError as QBETRuntimeError, TypeError as QBETTypeError, DivisionByZeroError
import math

class ReturnValue(Exception):
    """Exception to handle return statements"""
    def __init__(self, value):
        self.value = value

class Interpreter:
    """Tree-walking interpreter for QBET"""
    
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self._setup_builtins()
    
    def _setup_builtins(self):
        """Setup built-in functions"""
        from stdlib.core import setup_core_functions
        from stdlib.quantum import setup_quantum_functions
        from stdlib.spiritual import setup_spiritual_functions
        from stdlib.tars import setup_tars
        
        setup_core_functions(self.global_env)
        setup_quantum_functions(self.global_env)
        setup_spiritual_functions(self.global_env)
        setup_tars(self.global_env)
    
    def interpret(self, ast):
        """Interpret the AST"""
        try:
            return self.visit(ast)
        except ReturnValue as rv:
            return rv.value
    
    def visit(self, node):
        """Visit a node and execute it"""
        method_name = f'visit_{node.__class__.__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node):
        """Fallback for unimplemented nodes"""
        raise QBETRuntimeError(f"No visit method for {node.__class__.__name__}")
    
    # ============= Program and Statements =============
    
    def visit_Program(self, node):
        """Execute program"""
        result = None
        for statement in node.statements:
            result = self.visit(statement)
        return result
    
    def visit_ExpressionStatement(self, node):
        """Execute expression statement"""
        return self.visit(node.expression)
    
    def visit_Block(self, node):
        """Execute block with new scope"""
        # Create new environment for block scope
        previous_env = self.current_env
        self.current_env = Environment(parent=previous_env)
        
        result = None
        try:
            for statement in node.statements:
                result = self.visit(statement)
        finally:
            self.current_env = previous_env
        
        return result
    
    def visit_IfStatement(self, node):
        """Execute if statement"""
        condition = self.visit(node.condition)
        
        if self.is_truthy(condition):
            return self.visit(node.then_block)
        elif node.else_block:
            return self.visit(node.else_block)
        
        return Null()
    
    def visit_WhileStatement(self, node):
        """Execute while loop"""
        result = Null()
        while self.is_truthy(self.visit(node.condition)):
            result = self.visit(node.body)
        return result
    
    def visit_ForStatement(self, node):
        """Execute for loop"""
        iterable = self.visit(node.iterable)
        
        # Create new scope for loop variable
        previous_env = self.current_env
        self.current_env = Environment(parent=previous_env)
        
        result = Null()
        try:
            if isinstance(iterable, ArrayLiteral):
                for element in iterable.elements:
                    self.current_env.define(node.variable, self.visit(element))
                    result = self.visit(node.body)
            elif hasattr(iterable, 'value') and isinstance(iterable.value, list):
                for element in iterable.value:
                    self.current_env.define(node.variable, element)
                    result = self.visit(node.body)
            else:
                raise QBETTypeError("For loop requires iterable")
        finally:
            self.current_env = previous_env
        
        return result
    
    def visit_FunctionDeclaration(self, node):
        """Define function"""
        func = Function(node.parameters, node.body, self.current_env)
        self.current_env.define(node.name, func)
        return func
    
    def visit_ReturnStatement(self, node):
        """Execute return"""
        value = Null()
        if node.value:
            value = self.visit(node.value)
        raise ReturnValue(value)
    
    def visit_ImportStatement(self, node):
        """Import module"""
        # For now, just acknowledge the import
        # In a full implementation, this would load external modules
        return Null()
    
    # ============= Expressions =============
    
    def visit_NumberLiteral(self, node):
        """Evaluate number"""
        return Number(node.value)
    
    def visit_StringLiteral(self, node):
        """Evaluate string"""
        return String(node.value)
    
    def visit_BooleanLiteral(self, node):
        """Evaluate boolean"""
        return Boolean(node.value)
    
    def visit_NullLiteral(self, node):
        """Evaluate null"""
        return Null()
    
    def visit_Identifier(self, node):
        """Get variable value"""
        return self.current_env.get(node.name)
    
    def visit_Assignment(self, node):
        """Assign variable"""
        value = self.visit(node.value)
        
        if self.current_env.exists(node.name):
            self.current_env.set(node.name, value)
        else:
            self.current_env.define(node.name, value)
        
        return value
    
    def visit_BinaryOp(self, node):
        """Execute binary operation"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.operator.type
        
        # Arithmetic
        if op == TokenType.PLUS:
            if isinstance(left, Number) and isinstance(right, Number):
                return Number(left.value + right.value)
            elif isinstance(left, String) or isinstance(right, String):
                return String(str(left.value) + str(right.value))
            else:
                raise QBETTypeError("Invalid operands for +")
        
        elif op == TokenType.MINUS:
            self._check_number_operands(left, right)
            return Number(left.value - right.value)
        
        elif op == TokenType.MULTIPLY:
            self._check_number_operands(left, right)
            return Number(left.value * right.value)
        
        elif op == TokenType.DIVIDE:
            self._check_number_operands(left, right)
            if right.value == 0:
                raise DivisionByZeroError()
            return Number(left.value / right.value)
        
        elif op == TokenType.MODULO:
            self._check_number_operands(left, right)
            return Number(left.value % right.value)
        
        elif op == TokenType.POWER:
            self._check_number_operands(left, right)
            return Number(left.value ** right.value)
        
        # Comparison
        elif op == TokenType.EQUAL:
            return Boolean(self.is_equal(left, right))
        
        elif op == TokenType.NOT_EQUAL:
            return Boolean(not self.is_equal(left, right))
        
        elif op == TokenType.LESS:
            self._check_number_operands(left, right)
            return Boolean(left.value < right.value)
        
        elif op == TokenType.LESS_EQUAL:
            self._check_number_operands(left, right)
            return Boolean(left.value <= right.value)
        
        elif op == TokenType.GREATER:
            self._check_number_operands(left, right)
            return Boolean(left.value > right.value)
        
        elif op == TokenType.GREATER_EQUAL:
            self._check_number_operands(left, right)
            return Boolean(left.value >= right.value)
        
        # Logical
        elif op == TokenType.AND:
            if not self.is_truthy(left):
                return left
            return right
        
        elif op == TokenType.OR:
            if self.is_truthy(left):
                return left
            return right
        
        else:
            raise QBETRuntimeError(f"Unknown binary operator: {op}")
    
    def visit_UnaryOp(self, node):
        """Execute unary operation"""
        operand = self.visit(node.operand)
        op = node.operator.type
        
        if op == TokenType.MINUS:
            if not isinstance(operand, Number):
                raise QBETTypeError("Unary minus requires number")
            return Number(-operand.value)
        
        elif op == TokenType.NOT:
            return Boolean(not self.is_truthy(operand))
        
        else:
            raise QBETRuntimeError(f"Unknown unary operator: {op}")
    
    def visit_FunctionCall(self, node):
        """Call function"""
        func = self.current_env.get(node.name)
        
        # Built-in function
        if callable(func):
            args = [self.visit(arg) for arg in node.arguments]
            return func(*args)
        
        # User-defined function
        if isinstance(func, Function):
            args = [self.visit(arg) for arg in node.arguments]
            
            if len(args) != len(func.params):
                raise QBETRuntimeError(f"Function {node.name} expects {len(func.params)} arguments, got {len(args)}")
            
            # Create new environment for function
            previous_env = self.current_env
            self.current_env = Environment(parent=func.env)
            
            # Bind parameters
            for param, arg in zip(func.params, args):
                self.current_env.define(param, arg)
            
            try:
                self.visit(func.body)
                result = Null()
            except ReturnValue as rv:
                result = rv.value
            finally:
                self.current_env = previous_env
            
            return result
        
        raise QBETTypeError(f"{node.name} is not callable")
    
    def visit_MethodCall(self, node):
        """Call method on object"""
        obj = self.visit(node.object)
        method_name = node.method
        args = [self.visit(arg) for arg in node.arguments]
        
        # Check if object has the method
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                result = method(*args)
                # Wrap result if needed
                if not isinstance(result, QBETValue):
                    if isinstance(result, (int, float)):
                        return Number(result)
                    elif isinstance(result, str):
                        return String(result)
                    elif isinstance(result, bool):
                        return Boolean(result)
                    elif result is None:
                        return Null()
                return result
        
        raise QBETRuntimeError(f"Object has no method '{method_name}'")
    
    def visit_MemberAccess(self, node):
        """Access object member"""
        obj = self.visit(node.object)
        
        if hasattr(obj, node.member):
            attr = getattr(obj, node.member)
            # Wrap primitive values
            if not isinstance(attr, QBETValue):
                if isinstance(attr, (int, float)):
                    return Number(attr)
                elif isinstance(attr, str):
                    return String(attr)
                elif isinstance(attr, bool):
                    return Boolean(attr)
            return attr
        
        raise QBETRuntimeError(f"Object has no member '{node.member}'")
    
    def visit_ArrayLiteral(self, node):
        """Create array"""
        elements = [self.visit(elem) for elem in node.elements]
        return QBETValue(elements, QBETType.ARRAY)
    
    def visit_IndexAccess(self, node):
        """Access array element"""
        obj = self.visit(node.object)
        index = self.visit(node.index)
        
        if not isinstance(index, Number):
            raise QBETTypeError("Array index must be a number")
        
        idx = int(index.value)
        
        if hasattr(obj, 'value') and isinstance(obj.value, list):
            if 0 <= idx < len(obj.value):
                return obj.value[idx]
            raise QBETRuntimeError(f"Index {idx} out of range")
        
        raise QBETTypeError("Index access requires array")
    
    # ============= Quantum Nodes =============
    
    def visit_QubitCreation(self, node):
        """Create qubit"""
        alpha = 1.0 if isinstance(node.alpha, float) else self.visit(node.alpha).value
        beta = 0.0 if isinstance(node.beta, float) else self.visit(node.beta).value
        return Qubit(alpha, beta)
    
    def visit_UniverseCreation(self, node):
        """Create universe"""
        return Universe()
    
    def visit_ChakraCreation(self, node):
        """Create chakra"""
        level = 50 if isinstance(node.level, int) else self.visit(node.level).value
        return Chakra(node.chakra_type, level)
    
    def visit_EnergyCreation(self, node):
        """Create energy"""
        amount = self.visit(node.amount).value if not isinstance(node.amount, (int, float)) else node.amount
        frequency = self.visit(node.frequency).value if not isinstance(node.frequency, (int, float)) else node.frequency
        vibration = self.visit(node.vibration).value if not isinstance(node.vibration, (int, float)) else node.vibration
        return Energy(amount, frequency, vibration)
    
    # ============= Helper Methods =============
    
    def is_truthy(self, value):
        """Determine if value is truthy"""
        if isinstance(value, Null):
            return False
        if isinstance(value, Boolean):
            return value.value
        if isinstance(value, Number):
            return value.value != 0
        if isinstance(value, String):
            return len(value.value) > 0
        return True
    
    def is_equal(self, left, right):
        """Check equality"""
        if type(left) != type(right):
            return False
        if isinstance(left, Null):
            return True
        return left.value == right.value
    
    def _check_number_operands(self, left, right):
        """Verify operands are numbers"""
        if not isinstance(left, Number) or not isinstance(right, Number):
            raise QBETTypeError("Operands must be numbers")
