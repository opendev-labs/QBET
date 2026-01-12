"""
QBET Lexer (Tokenizer)
Converts source code into a stream of tokens.
"""

from enum import Enum, auto
from errors import LexerError

class TokenType(Enum):
    """All token types in QBET"""
    # Literals
    NUMBER = auto()
    STRING = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    
    # Identifiers and keywords
    IDENTIFIER = auto()
    
    # Keywords - Core
    CREATE = auto()
    IMPORT = auto()
    AS = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    IN = auto()
    RETURN = auto()
    FUNCTION = auto()
    NEW = auto()
    
    # Keywords - Quantum
    QUBIT = auto()
    WAVE = auto()
    PARTICLE = auto()
    MATRIX = auto()
    ENTANGLE = auto()
    SUPERPOSITION = auto()
    
    # Keywords - Spiritual
    SPIRIT = auto()
    SOUL = auto()
    CONSCIOUSNESS = auto()
    CHAKRA = auto()
    KARMA = auto()
    DHARMA = auto()
    ENERGY = auto()
    FREQUENCY = auto()
    VIBRATION = auto()
    BALANCE = auto()
    
    # Keywords - Cosmic
    UNIVERSE = auto()
    MULTIVERSE = auto()
    PLANET = auto()
    STAR = auto()
    GALAXY = auto()
    
    # Keywords - Special
    DIVINE_CREATOR = auto()
    HIGHER_SELF = auto()
    LOWER_SELF = auto()
    ASTRAL = auto()
    
    # Keywords - 2037 Creator Level
    VOID = auto()
    INTENTION = auto()
    MANIFEST = auto()
    OBSERVE = auto()
    INVOKE = auto()
    FLOW = auto()
    COLLAPSE = auto()
    ENTITY = auto()
    DEPLOY = auto()
    GENERATE = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    POWER = auto()
    
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    SEMICOLON = auto()
    ARROW = auto()
    
    # Special
    NEWLINE = auto()
    EOF = auto()

class Token:
    """Represents a single token"""
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"

class Lexer:
    """Tokenizes QBET source code"""
    
    KEYWORDS = {
        'create': TokenType.CREATE,
        'import': TokenType.IMPORT,
        'as': TokenType.AS,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'while': TokenType.WHILE,
        'for': TokenType.FOR,
        'in': TokenType.IN,
        'return': TokenType.RETURN,
        'function': TokenType.FUNCTION,
        'new': TokenType.NEW,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'null': TokenType.NULL,
        
        # Quantum
        'qubit': TokenType.QUBIT,
        'wave': TokenType.WAVE,
        'particle': TokenType.PARTICLE,
        'matrix': TokenType.MATRIX,
        'entangle': TokenType.ENTANGLE,
        'superposition': TokenType.SUPERPOSITION,
        
        # Spiritual
        'spirit': TokenType.SPIRIT,
        'soul': TokenType.SOUL,
        'consciousness': TokenType.CONSCIOUSNESS,
        'chakra': TokenType.CHAKRA,
        'karma': TokenType.KARMA,
        'dharma': TokenType.DHARMA,
        'energy': TokenType.ENERGY,
        'frequency': TokenType.FREQUENCY,
        'vibration': TokenType.VIBRATION,
        'balance': TokenType.BALANCE,
        
        # Cosmic
        'universe': TokenType.UNIVERSE,
        'multiverse': TokenType.MULTIVERSE,
        'planet': TokenType.PLANET,
        'star': TokenType.STAR,
        'galaxy': TokenType.GALAXY,
        
        # Special
        'divine_creator': TokenType.DIVINE_CREATOR,
        'higher_self': TokenType.HIGHER_SELF,
        'lower_self': TokenType.LOWER_SELF,
        'astral': TokenType.ASTRAL,
        
        # 2037 Creator Level
        'void': TokenType.VOID,
        'intention': TokenType.INTENTION,
        'manifest': TokenType.MANIFEST,
        'observe': TokenType.OBSERVE,
        'invoke': TokenType.INVOKE,
        'flow': TokenType.FLOW,
        'collapse': TokenType.COLLAPSE,
        'entity': TokenType.ENTITY,
        'deploy': TokenType.DEPLOY,
        'generate': TokenType.GENERATE,
        
        # Logical
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
    }
    
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
    
    def current_char(self):
        """Get current character"""
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset=1):
        """Look ahead at character"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        """Move to next character"""
        if self.pos < len(self.source):
            if self.source[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self):
        """Skip whitespace except newlines"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        """Skip comments starting with #"""
        if self.current_char() == '#':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self):
        """Read numeric literal"""
        start_col = self.column
        num_str = ''
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    raise LexerError("Invalid number format", self.line, self.column)
                has_dot = True
            num_str += self.current_char()
            self.advance()
        
        return Token(TokenType.NUMBER, float(num_str), self.line, start_col)
    
    def read_string(self):
        """Read string literal"""
        start_col = self.column
        quote = self.current_char()
        self.advance()  # Skip opening quote
        
        string = ''
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    string += '\n'
                elif self.current_char() == 't':
                    string += '\t'
                elif self.current_char() == '\\':
                    string += '\\'
                elif self.current_char() == quote:
                    string += quote
                else:
                    string += self.current_char()
                self.advance()
            else:
                string += self.current_char()
                self.advance()
        
        if not self.current_char():
            raise LexerError("Unterminated string", self.line, start_col)
        
        self.advance()  # Skip closing quote
        return Token(TokenType.STRING, string, self.line, start_col)
    
    def read_identifier(self):
        """Read identifier or keyword"""
        start_col = self.column
        ident = ''
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()
        
        token_type = self.KEYWORDS.get(ident, TokenType.IDENTIFIER)
        value = ident if token_type == TokenType.IDENTIFIER else None
        
        return Token(token_type, value, self.line, start_col)
    
    def tokenize(self):
        """Convert source code to tokens"""
        while self.current_char():
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            # Comments
            if self.current_char() == '#':
                self.skip_comment()
                continue
            
            # Newlines
            if self.current_char() == '\n':
                token = Token(TokenType.NEWLINE, None, self.line, self.column)
                self.tokens.append(token)
                self.advance()
                continue
            
            # Numbers
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Strings
            if self.current_char() in '"\'':
                self.tokens.append(self.read_string())
                continue
            
            # Identifiers and keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            # Operators and delimiters
            col = self.column
            char = self.current_char()
            
            if char == '+':
                self.tokens.append(Token(TokenType.PLUS, None, self.line, col))
                self.advance()
            elif char == '-':
                if self.peek_char() == '>':
                    self.tokens.append(Token(TokenType.ARROW, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.MINUS, None, self.line, col))
                    self.advance()
            elif char == '*':
                if self.peek_char() == '*':
                    self.tokens.append(Token(TokenType.POWER, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.MULTIPLY, None, self.line, col))
                    self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, None, self.line, col))
                self.advance()
            elif char == '%':
                self.tokens.append(Token(TokenType.MODULO, None, self.line, col))
                self.advance()
            elif char == '=':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.EQUAL, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, None, self.line, col))
                    self.advance()
            elif char == '!':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.NOT_EQUAL, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    raise LexerError(f"Unexpected character: {char}", self.line, col)
            elif char == '<':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.LESS_EQUAL, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.LESS, None, self.line, col))
                    self.advance()
            elif char == '>':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.GREATER, None, self.line, col))
                    self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, None, self.line, col))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, None, self.line, col))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, None, self.line, col))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, None, self.line, col))
                self.advance()
            elif char == '[':
                self.tokens.append(Token(TokenType.LBRACKET, None, self.line, col))
                self.advance()
            elif char == ']':
                self.tokens.append(Token(TokenType.RBRACKET, None, self.line, col))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, None, self.line, col))
                self.advance()
            elif char == '.':
                self.tokens.append(Token(TokenType.DOT, None, self.line, col))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, None, self.line, col))
                self.advance()
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, None, self.line, col))
                self.advance()
            else:
                raise LexerError(f"Unexpected character: {char}", self.line, col)
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
