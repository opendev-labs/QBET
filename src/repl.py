"""
QBET REPL (Read-Eval-Print Loop)
Interactive shell for QBET language.
"""

import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from errors import QBETError

class REPL:
    """Interactive QBET shell"""
    
    def __init__(self):
        self.interpreter = Interpreter()
        self.history = []
    
    def run(self):
        """Start REPL"""
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║           QBET Interactive Shell v1.0                     ║")
        print("║   Quantum-Spiritual Programming Language                  ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print()
        print("Type 'exit' or 'quit' to leave, 'help' for assistance")
        print()
        
        while True:
            try:
                # Read input
                line = input("qbet> ")
                
                # Handle special commands
                if line.strip() in ['exit', 'quit']:
                    print("Namaste! 🙏 May your code be enlightened.")
                    break
                
                if line.strip() == 'help':
                    self.show_help()
                    continue
                
                if line.strip() == 'clear':
                    print("\033[2J\033[H")  # Clear screen
                    continue
                
                if line.strip() == '':
                    continue
                
                # Add to history
                self.history.append(line)
                
                # Execute
                result = self.execute(line)
                
                # Print result if not null
                if result and hasattr(result, 'value') and result.value is not None:
                    if hasattr(result, 'type'):
                        print(f"=> {result.value} ({result.type.name})")
                    else:
                        print(f"=> {result.value}")
            
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                continue
            
            except EOFError:
                print("\nGoodbye!")
                break
            
            except QBETError as e:
                print(f"❌ {e}")
            
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
    
    def execute(self, source):
        """Execute QBET code"""
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Interpretation
        result = self.interpreter.interpret(ast)
        
        return result
    
    def show_help(self):
        """Show help message"""
        print()
        print("═══════════════════════════════════════════════════════════")
        print("                    QBET Quick Help")
        print("═══════════════════════════════════════════════════════════")
        print()
        print("BASIC SYNTAX:")
        print("  x = 42                    # Variable assignment")
        print("  print(x)                  # Print value")
        print("  function add(a, b) { return a + b }")
        print()
        print("QUANTUM OPERATIONS:")
        print("  qubit q1                  # Create qubit")
        print("  hadamard(q1)              # Apply Hadamard gate")
        print("  measure(q1)               # Measure qubit")
        print("  entangle(q1, q2)          # Entangle qubits")
        print()
        print("SPIRITUAL FUNCTIONS:")
        print("  chakra root_chakra        # Create chakra")
        print("  balance_chakra(root_chakra)")
        print("  energy life_force         # Create energy")
        print("  manifest(\"abundance\")     # Law of Attraction")
        print("  golden_ratio()            # Sacred geometry")
        print()
        print("SPECIAL COMMANDS:")
        print("  help                      # Show this help")
        print("  clear                     # Clear screen")
        print("  exit / quit               # Exit REPL")
        print()
        print("═══════════════════════════════════════════════════════════")
        print()

if __name__ == '__main__':
    repl = REPL()
    repl.run()
