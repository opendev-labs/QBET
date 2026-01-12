from lexer import Lexer, TokenType

class Lowerer:
    def __init__(self, source):
        self.lexer = Lexer(source)
        self.tokens = self.lexer.tokenize()
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type=None):
        token = self.peek()
        if expected_type and token and token.type != expected_type:
            raise Exception(f"Expected {expected_type}, got {token.type}")
        self.pos += 1
        return token

    def lower(self):
        instructions = []
        while self.peek():
            token = self.peek()
            if token.value == "universe":
                instructions.extend(self.lower_universe())
            elif token.value == "entity":
                instructions.extend(self.lower_entity())
            elif token.value == "manifest":
                instructions.extend(self.lower_manifest())
            elif token.value == "flow":
                instructions.extend(self.lower_flow())
            elif token.value == "observe":
                instructions.extend(self.lower_observe())
            else:
                self.consume() # Skip unknown
        return instructions

    def lower_universe(self):
        self.consume() # universe
        name = self.consume(TokenType.IDENTIFIER).value
        self.consume(TokenType.LBRACE)
        properties = {}
        while self.peek() and self.peek().type != TokenType.RBRACE:
            prop_name = self.consume(TokenType.IDENTIFIER).value
            self.consume(TokenType.COLON)
            vals = []
            while self.peek() and self.peek().type not in [TokenType.RBRACE, TokenType.IDENTIFIER]:
                 token = self.consume()
                 if token.type != TokenType.COMMA:
                      vals.append(token.value)
                 # If we see another ident, it might be the next property, so we check peek
            
            # If next is ident but we haven't hit a new property yet, it's part of the list
            while self.peek() and self.peek().type == TokenType.IDENTIFIER:
                 # Is this a new property? (followed by colon)
                 if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == TokenType.COLON:
                      break
                 vals.append(self.consume().value)
                 if self.peek() and self.peek().type == TokenType.COMMA:
                      self.consume()

            properties[prop_name] = vals if len(vals) > 1 else vals[0] if vals else None
        self.consume(TokenType.RBRACE)
        return [{"t": "UNIVERSE", "v": [name, properties]}]

    def lower_entity(self):
        self.consume() # entity
        name = self.consume(TokenType.IDENTIFIER).value
        self.consume(TokenType.LBRACE)
        properties = {}
        while self.peek() and self.peek().type != TokenType.RBRACE:
            prop_name = self.consume(TokenType.IDENTIFIER).value
            self.consume(TokenType.COLON)
            prop_value = self.consume().value
            properties[prop_name] = prop_value
        self.consume(TokenType.RBRACE)
        return [{"t": "ENTITY", "v": [name, properties]}]

    def lower_manifest(self):
        self.consume() # manifest
        u_name = self.consume(TokenType.IDENTIFIER).value
        self.consume() # with
        e_name = self.consume(TokenType.IDENTIFIER).value
        return [{"t": "MANIFEST", "v": [u_name, e_name]}]

    def lower_flow(self):
        self.consume() # flow
        self.consume() # time
        dir = self.consume().value # forward/backward
        return [{"t": "FLOW_TIME", "v": dir}]

    def lower_observe(self):
        self.consume() # observe
        target = self.consume(TokenType.IDENTIFIER).value
        return [{"t": "OBSERVE", "v": target}]
