from ast_nodes import *
from lexer import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self, offset=0):
        if self.pos + offset >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.pos + offset]

    def consume(self, expected_type=None):
        token = self.peek()
        if expected_type and token.type != expected_type:
            raise Exception(f"Expected {expected_type}, got {token.type} at line {token.line}")
        self.pos += 1
        return token

    def match(self, *types):
        for type in types:
            if self.peek().type == type:
                self.consume()
                return True
        return False

    def parse(self):
        statements = []
        while self.peek().type != TokenType.EOF:
            statements.append(self.parse_declaration())
        return Program(statements)

    def parse_declaration(self):
        if self.match(TokenType.USE):
            module_token = self.consume() # Can be IDENTIFIER or a keyword like QUANTUM
            return ImportStatement(module_token.value)
        if self.match(TokenType.FUNCTION):
            return self.parse_function()
        return self.parse_statement()

    def parse_function(self):
        name = self.consume(TokenType.IDENTIFIER).value
        self.consume(TokenType.LPAREN)
        # Parameters could go here
        self.consume(TokenType.RPAREN)
        self.consume(TokenType.LBRACE)
        body = self.parse_block()
        return FunctionDeclaration(name, [], body)

    def parse_block(self):
        statements = []
        while self.peek().type != TokenType.RBRACE and self.peek().type != TokenType.EOF:
            statements.append(self.parse_statement())
        self.consume(TokenType.RBRACE)
        return Block(statements)

    def parse_statement(self):
        if self.match(TokenType.PRINT):
            expr = self.parse_expression()
            return ExpressionStatement(FunctionCall("print", [expr]))
        if self.match(TokenType.STATE):
            name = self.consume(TokenType.IDENTIFIER).value
            self.consume(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(name, value)
        if self.match(TokenType.OBSERVE):
            name = self.consume(TokenType.IDENTIFIER).value
            return ExpressionStatement(Measurement(name))
        if self.match(TokenType.QUANTUM):
            name = self.consume(TokenType.IDENTIFIER).value
            self.consume(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(name, QubitCreation(name, value))
        if self.match(TokenType.LINK):
            q1 = self.consume(TokenType.IDENTIFIER).value
            q2 = self.consume(TokenType.IDENTIFIER).value
            return ExpressionStatement(Entanglement(q1, q2))
        
        expr = self.parse_expression()
        return ExpressionStatement(expr)

    def parse_expression(self):
        token = self.peek()
        if self.match(TokenType.STRING):
            return StringLiteral(token.value)
        if self.match(TokenType.NUMBER):
            return NumberLiteral(float(token.value))
        if self.match(TokenType.IDENTIFIER):
            if self.peek().type == TokenType.LPAREN:
                self.consume() # (
                # Handle arguments
                self.consume(TokenType.RPAREN)
                return FunctionCall(token.value, [])
            return Identifier(token.value)
        if self.match(TokenType.TRUE):
            return BooleanLiteral(True)
        if self.match(TokenType.FALSE):
            return BooleanLiteral(False)
        if self.match(TokenType.NULL):
            return NullLiteral()
        
        raise Exception(f"Unexpected expression start: {token.type} at line {token.line}")
