import enum

class TokenType(enum.Enum):
    MANIFEST = "MANIFEST"
    USE = "USE"
    FUNCTION = "FUNCTION"
    STATE = "STATE"
    OBSERVE = "OBSERVE"
    IF = "IF"
    ELSE = "ELSE"
    PRINT = "PRINT"
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"
    ASSIGN = "ASSIGN"
    EQ = "EQ"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    SEMICOLON = "SEMICOLON"
    EOF = "EOF"

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}')"

class Lexer:
    KEYWORDS = {
        "manifest": TokenType.MANIFEST,
        "use": TokenType.USE,
        "function": TokenType.FUNCTION,
        "state": TokenType.STATE,
        "observe": TokenType.OBSERVE,
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "print": TokenType.PRINT,
    }

    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1

    # Lexing logic... (placeholder for implementation)
