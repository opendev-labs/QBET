"""
QBET Error Handling Module
Defines custom exceptions for lexical, syntax, and runtime errors.
"""

class QBETError(Exception):
    """Base exception for all QBET errors"""
    pass

class LexerError(QBETError):
    """Raised when lexer encounters invalid tokens"""
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Lexer Error at line {line}, column {column}: {message}")

class SyntaxError(QBETError):
    """Raised when parser encounters invalid syntax"""
    def __init__(self, message, token=None):
        self.message = message
        self.token = token
        if token:
            super().__init__(f"Syntax Error at line {token.line}, column {token.column}: {message}")
        else:
            super().__init__(f"Syntax Error: {message}")

class RuntimeError(QBETError):
    """Raised during program execution"""
    def __init__(self, message, node=None):
        self.message = message
        self.node = node
        super().__init__(f"Runtime Error: {message}")

class TypeError(QBETError):
    """Raised when type mismatch occurs"""
    def __init__(self, message, expected=None, got=None):
        self.message = message
        self.expected = expected
        self.got = got
        if expected and got:
            super().__init__(f"Type Error: Expected {expected}, got {got}. {message}")
        else:
            super().__init__(f"Type Error: {message}")

class NameError(QBETError):
    """Raised when variable/function not found"""
    def __init__(self, name):
        self.name = name
        super().__init__(f"Name Error: '{name}' is not defined")

class DivisionByZeroError(QBETError):
    """Raised when dividing by zero"""
    def __init__(self):
        super().__init__("Runtime Error: Division by zero")
