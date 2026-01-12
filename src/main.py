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
    print("Copyright (c) 2026 opendev-labs")
    print()
    print("A revolutionary language bridging quantum computing,")
    print("spiritual metaphysics, and traditional programming.")

def show_banner():
    """Show welcome banner"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║                    ██████  ██████  ███████ ████████           ║")
    print("║                   ██    ██ ██   ██ ██         ██              ║")
    print("║                   ██    ██ ██████  █████      ██              ║")
    print("║                   ██ ▄▄ ██ ██   ██ ██         ██              ║")
    print("║                    ██████  ██████  ███████    ██              ║")
    print("║                       ▀▀                                      ║")
    print("║                                                               ║")
    print("║             The Creation-Oriented Programming Language        ║")
    print(f"║                          Version {VERSION}                        ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='QBET - The Creation-Oriented Language',
        epilog='Governed by opendev-labs'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Manifestation commands')
    
    # Manifest command
    manifest_parser = subparsers.add_parser('manifest', help='Translate intention into reality')
    manifest_parser.add_argument('file', help='QBET source file (.qbet)')
    manifest_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')
    
    # Run command (alias)
    run_parser = subparsers.add_parser('run', help='Execute a QBET script')
    run_parser.add_argument('file', help='QBET source file (.qbet)')
    run_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')
    
    # Portal command
    portal_parser = subparsers.add_parser('portal', help='Manifest the local landing page')
    portal_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')
    
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show version information'
    )
    
    args = parser.parse_args()
    
    if args.version:
        show_version()
        return 0
    
    # Handle subcommands
    if args.command in ['manifest', 'run']:
        if not args.no_banner:
            show_banner()
        return run_file(args.file)
    
    if args.command == 'portal':
        if not args.no_banner:
            show_banner()
        from portal.server import manifest_portal
        return manifest_portal()
    
    # Default to REPL if no command or file and stdout is a terminal
    if sys.stdin.isatty():
        show_banner()
        return run_repl()
    
    parser.print_help()
    return 1

if __name__ == '__main__':
    sys.exit(main())
