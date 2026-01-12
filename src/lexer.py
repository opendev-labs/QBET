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

    def tokenize(self):
        tokens = []
        while self.pos < len(self.source):
            char = self.source[self.pos]
            
            if char.isspace():
                if char == '\n':
                    self.line += 1
                self.pos += 1
                continue
                
            if char == '#': # Comments
                while self.pos < len(self.source) and self.source[self.pos] != '\n':
                    self.pos += 1
                continue
                
            if char.isalpha() or char == '_':
                start = self.pos
                while self.pos < len(self.source) and (self.source[self.pos].isalnum() or self.source[self.pos] == '_'):
                    self.pos += 1
                value = self.source[start:self.pos]
                type = self.KEYWORDS.get(value, TokenType.IDENTIFIER)
                tokens.append(Token(type, value, self.line))
                continue
                
            if char == '"': # Strings
                self.pos += 1
                start = self.pos
                while self.pos < len(self.source) and self.source[self.pos] != '"':
                    self.pos += 1
                value = self.source[start:self.pos]
                self.pos += 1
                tokens.append(Token(TokenType.STRING, value, self.line))
                continue
                
            if char == '=':
                if self.pos + 1 < len(self.source) and self.source[self.pos+1] == '=':
                    tokens.append(Token(TokenType.EQ, '==', self.line))
                    self.pos += 2
                else:
                    tokens.append(Token(TokenType.ASSIGN, '=', self.line))
                    self.pos += 1
                continue
                
            if char == '{':
                tokens.append(Token(TokenType.LBRACE, '{', self.line))
                self.pos += 1; continue
            if char == '}':
                tokens.append(Token(TokenType.RBRACE, '}', self.line))
                self.pos += 1; continue
            if char == '(':
                tokens.append(Token(TokenType.LPAREN, '(', self.line))
                self.pos += 1; continue
            if char == ')':
                tokens.append(Token(TokenType.RPAREN, ')', self.line))
                self.pos += 1; continue
                
            self.pos += 1 # Skip unhandled chars for now
            
        tokens.append(Token(TokenType.EOF, '', self.line))
        return tokens
