"""
QBET Parser
Converts tokens into an Abstract Syntax Tree (AST).
"""

from lexer import TokenType
from ast_nodes import *
from errors import SyntaxError as QBETSyntaxError

class Parser:
    """Recursive descent parser for QBET"""
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        """Get current token"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]  # EOF
    
    def peek_token(self, offset=1):
        """Look ahead at token"""
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]
    
    def advance(self):
        """Move to next token"""
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return self.current_token()
    
    def expect(self, token_type):
        """Expect specific token type"""
        token = self.current_token()
        if token.type != token_type:
            raise QBETSyntaxError(f"Expected {token_type}, got {token.type}", token)
        self.advance()
        return token
    
    def skip_newlines(self):
        """Skip newline tokens"""
        while self.current_token().type == TokenType.NEWLINE:
            self.advance()
    
    def parse(self):
        """Parse tokens into AST"""
        statements = []
        self.skip_newlines()
        
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        return Program(statements)
    
    def parse_statement(self):
        """Parse a single statement"""
        self.skip_newlines()
        token = self.current_token()
        
        # Function declaration
        if token.type == TokenType.FUNCTION:
            return self.parse_function_declaration()
        
        # If statement
        if token.type == TokenType.IF:
            return self.parse_if_statement()
        
        # While loop
        if token.type == TokenType.WHILE:
            return self.parse_while_statement()
        
        # For loop
        if token.type == TokenType.FOR:
            return self.parse_for_statement()
        
        # Return statement
        if token.type == TokenType.RETURN:
            return self.parse_return_statement()
        
        # Import statement
        if token.type == TokenType.IMPORT:
            return self.parse_import_statement()
        
        # Universe creation
        if token.type == TokenType.DIVINE_CREATOR:
            return self.parse_universe_creation()
        
        # Qubit creation
        if token.type == TokenType.QUBIT:
            return self.parse_qubit_creation()
        
        # Chakra creation
        if token.type == TokenType.CHAKRA:
            return self.parse_chakra_creation()
        
        # Energy creation
        if token.type == TokenType.ENERGY:
            return self.parse_energy_creation()
        
        # Block
        if token.type == TokenType.LBRACE:
            return self.parse_block()
        
        # Expression statement (including assignments)
        return self.parse_expression_statement()
    
    def parse_function_declaration(self):
        """Parse function declaration"""
        self.expect(TokenType.FUNCTION)
        name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LPAREN)
        parameters = []
        
        if self.current_token().type != TokenType.RPAREN:
            parameters.append(self.expect(TokenType.IDENTIFIER).value)
            while self.current_token().type == TokenType.COMMA:
                self.advance()
                parameters.append(self.expect(TokenType.IDENTIFIER).value)
        
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        
        return FunctionDeclaration(name, parameters, body)
    
    def parse_if_statement(self):
        """Parse if statement"""
        self.expect(TokenType.IF)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        
        then_block = self.parse_block()
        else_block = None
        
        if self.current_token().type == TokenType.ELSE:
            self.advance()
            else_block = self.parse_block()
        
        return IfStatement(condition, then_block, else_block)
    
    def parse_while_statement(self):
        """Parse while loop"""
        self.expect(TokenType.WHILE)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        
        body = self.parse_block()
        return WhileStatement(condition, body)
    
    def parse_for_statement(self):
        """Parse for loop"""
        self.expect(TokenType.FOR)
        self.expect(TokenType.LPAREN)
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.IN)
        iterable = self.parse_expression()
        self.expect(TokenType.RPAREN)
        
        body = self.parse_block()
        return ForStatement(variable, iterable, body)
    
    def parse_return_statement(self):
        """Parse return statement"""
        self.expect(TokenType.RETURN)
        
        value = None
        if self.current_token().type not in [TokenType.NEWLINE, TokenType.SEMICOLON, TokenType.EOF]:
            value = self.parse_expression()
        
        return ReturnStatement(value)
    
    def parse_import_statement(self):
        """Parse import statement"""
        self.expect(TokenType.IMPORT)
        module = self.expect(TokenType.IDENTIFIER).value
        
        alias = None
        if self.current_token().type == TokenType.AS:
            self.advance()
            alias = self.expect(TokenType.IDENTIFIER).value
        
        return ImportStatement(module, alias)
    
    def parse_universe_creation(self):
        """Parse universe creation"""
        self.expect(TokenType.DIVINE_CREATOR)
        name = self.expect(TokenType.IDENTIFIER).value
        return ExpressionStatement(Assignment(name, UniverseCreation(name)))
    
    def parse_qubit_creation(self):
        """Parse qubit creation"""
        self.expect(TokenType.QUBIT)
        name = self.expect(TokenType.IDENTIFIER).value
        
        alpha = 1.0
        beta = 0.0
        
        if self.current_token().type == TokenType.LPAREN:
            self.advance()
            alpha = self.parse_expression()
            if self.current_token().type == TokenType.COMMA:
                self.advance()
                beta = self.parse_expression()
            self.expect(TokenType.RPAREN)
        
        return ExpressionStatement(Assignment(name, QubitCreation(name, alpha, beta)))
    
    def parse_chakra_creation(self):
        """Parse chakra creation"""
        self.expect(TokenType.CHAKRA)
        name = self.expect(TokenType.IDENTIFIER).value
        
        chakra_type = "root"
        level = 50
        
        if self.current_token().type == TokenType.LPAREN:
            self.advance()
            if self.current_token().type == TokenType.STRING:
                chakra_type = self.current_token().value
                self.advance()
            if self.current_token().type == TokenType.COMMA:
                self.advance()
                level = self.parse_expression()
            self.expect(TokenType.RPAREN)
        
        return ExpressionStatement(Assignment(name, ChakraCreation(name, chakra_type, level)))
    
    def parse_energy_creation(self):
        """Parse energy creation"""
        self.expect(TokenType.ENERGY)
        name = self.expect(TokenType.IDENTIFIER).value
        
        amount = 100
        frequency = 1.0
        vibration = 1.0
        
        if self.current_token().type == TokenType.LPAREN:
            self.advance()
            amount = self.parse_expression()
            if self.current_token().type == TokenType.COMMA:
                self.advance()
                frequency = self.parse_expression()
            if self.current_token().type == TokenType.COMMA:
                self.advance()
                vibration = self.parse_expression()
            self.expect(TokenType.RPAREN)
        
        return ExpressionStatement(Assignment(name, EnergyCreation(name, amount, frequency, vibration)))
    
    def parse_block(self):
        """Parse block of statements"""
        self.expect(TokenType.LBRACE)
        self.skip_newlines()
        
        statements = []
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        self.expect(TokenType.RBRACE)
        return Block(statements)
    
    def parse_expression_statement(self):
        """Parse expression as statement"""
        expr = self.parse_expression()
        return ExpressionStatement(expr)
    
    def parse_expression(self):
        """Parse expression"""
        return self.parse_assignment()
    
    def parse_assignment(self):
        """Parse assignment or logical OR"""
        expr = self.parse_logical_or()
        
        if self.current_token().type == TokenType.ASSIGN:
            if not isinstance(expr, Identifier):
                raise QBETSyntaxError("Invalid assignment target", self.current_token())
            self.advance()
            value = self.parse_assignment()
            return Assignment(expr.name, value)
        
        return expr
    
    def parse_logical_or(self):
        """Parse logical OR"""
        left = self.parse_logical_and()
        
        while self.current_token().type == TokenType.OR:
            op = self.current_token()
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_logical_and(self):
        """Parse logical AND"""
        left = self.parse_equality()
        
        while self.current_token().type == TokenType.AND:
            op = self.current_token()
            self.advance()
            right = self.parse_equality()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_equality(self):
        """Parse equality operators"""
        left = self.parse_comparison()
        
        while self.current_token().type in [TokenType.EQUAL, TokenType.NOT_EQUAL]:
            op = self.current_token()
            self.advance()
            right = self.parse_comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_comparison(self):
        """Parse comparison operators"""
        left = self.parse_addition()
        
        while self.current_token().type in [TokenType.LESS, TokenType.LESS_EQUAL, 
                                            TokenType.GREATER, TokenType.GREATER_EQUAL]:
            op = self.current_token()
            self.advance()
            right = self.parse_addition()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_addition(self):
        """Parse addition and subtraction"""
        left = self.parse_multiplication()
        
        while self.current_token().type in [TokenType.PLUS, TokenType.MINUS]:
            op = self.current_token()
            self.advance()
            right = self.parse_multiplication()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_multiplication(self):
        """Parse multiplication, division, modulo"""
        left = self.parse_power()
        
        while self.current_token().type in [TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO]:
            op = self.current_token()
            self.advance()
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_power(self):
        """Parse power operator"""
        left = self.parse_unary()
        
        if self.current_token().type == TokenType.POWER:
            op = self.current_token()
            self.advance()
            right = self.parse_power()  # Right associative
            return BinaryOp(left, op, right)
        
        return left
    
    def parse_unary(self):
        """Parse unary operators"""
        if self.current_token().type in [TokenType.MINUS, TokenType.NOT]:
            op = self.current_token()
            self.advance()
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        
        return self.parse_postfix()
    
    def parse_postfix(self):
        """Parse postfix expressions (calls, member access, indexing)"""
        expr = self.parse_primary()
        
        while True:
            token = self.current_token()
            
            # Function call
            if token.type == TokenType.LPAREN:
                self.advance()
                arguments = []
                
                if self.current_token().type != TokenType.RPAREN:
                    arguments.append(self.parse_expression())
                    while self.current_token().type == TokenType.COMMA:
                        self.advance()
                        arguments.append(self.parse_expression())
                
                self.expect(TokenType.RPAREN)
                
                if isinstance(expr, Identifier):
                    expr = FunctionCall(expr.name, arguments)
                elif isinstance(expr, MemberAccess):
                    expr = MethodCall(expr.object, expr.member, arguments)
                else:
                    raise QBETSyntaxError("Invalid function call", token)
            
            # Member access
            elif token.type == TokenType.DOT:
                self.advance()
                member = self.expect(TokenType.IDENTIFIER).value
                expr = MemberAccess(expr, member)
            
            # Index access
            elif token.type == TokenType.LBRACKET:
                self.advance()
                index = self.parse_expression()
                self.expect(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)
            
            else:
                break
        
        return expr
    
    def parse_primary(self):
        """Parse primary expressions"""
        token = self.current_token()
        
        # Numbers
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(token.value)
        
        # Strings
        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(token.value)
        
        # Booleans
        if token.type == TokenType.TRUE:
            self.advance()
            return BooleanLiteral(True)
        
        if token.type == TokenType.FALSE:
            self.advance()
            return BooleanLiteral(False)
        
        # Null
        if token.type == TokenType.NULL:
            self.advance()
            return NullLiteral()
        
        # Identifiers
        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(token.value)
        
        # Parenthesized expression
        if token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        # Array literal
        if token.type == TokenType.LBRACKET:
            self.advance()
            elements = []
            
            if self.current_token().type != TokenType.RBRACKET:
                elements.append(self.parse_expression())
                while self.current_token().type == TokenType.COMMA:
                    self.advance()
                    elements.append(self.parse_expression())
            
            self.expect(TokenType.RBRACKET)
            return ArrayLiteral(elements)
        
        raise QBETSyntaxError(f"Unexpected token: {token.type}", token)
