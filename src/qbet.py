#!/usr/bin/env python3
"""
QBET - Quantum-Spiritual Programming Language
Main entry point for the QBET interpreter.
"""

import sys
import argparse
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from repl import REPL
from errors import QBETError

VERSION = "1.0.0"

def run_file(filename):
    """Execute a QBET source file"""
    try:
        # Read source file
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Interpretation
        interpreter = Interpreter()
        result = interpreter.interpret(ast)
        
        return 0
    
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return 1
    
    except QBETError as e:
        print(f"❌ {e}")
        return 1
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

def run_repl():
    """Start interactive REPL"""
    repl = REPL()
    repl.run()
    return 0

def show_version():
    """Show version information"""
    print(f"QBET v{VERSION}")
    print("Quantum-Spiritual Programming Language")
    print("Copyright (c) 2026 OpenDev Labs")
    print()
    print("A revolutionary language bridging quantum computing,")
    print("spiritual metaphysics, and traditional programming.")

def show_banner():
    """Show welcome banner"""
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                                                           ║")
    print("║                    ██████  ██████  ███████ ████████      ║")
    print("║                   ██    ██ ██   ██ ██         ██         ║")
    print("║                   ██    ██ ██████  █████      ██         ║")
    print("║                   ██ ▄▄ ██ ██   ██ ██         ██         ║")
    print("║                    ██████  ██████  ███████    ██         ║")
    print("║                       ▀▀                                 ║")
    print("║                                                           ║")
    print("║          Quantum-Spiritual Programming Language          ║")
    print(f"║                      Version {VERSION}                       ║")
    print("║                                                           ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='QBET - Quantum-Spiritual Programming Language',
        epilog='For more information, visit: https://github.com/opendev-labs/QBET'
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='QBET source file to execute (.qbet)'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show version information'
    )
    
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Start interactive REPL (default if no file specified)'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Suppress welcome banner'
    )
    
    args = parser.parse_args()
    
    # Show version
    if args.version:
        show_version()
        return 0
    
    # Execute file
    if args.file:
        if not args.no_banner:
            show_banner()
        return run_file(args.file)
    
    # Start REPL (default)
    if not args.no_banner:
        show_banner()
    return run_repl()

if __name__ == '__main__':
    sys.exit(main())
