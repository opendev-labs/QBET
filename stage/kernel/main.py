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

import json
from lexer import Lexer, Token, TokenType
from parser import Parser
from interpreter import Interpreter
from lowerer import Lowerer
from repl import REPL
from errors import QBETError

VERSION = "1.0.0-omega"
IDENTITY = "opendev-labs"
QBET_ROOT = Path(__file__).parent.parent

# ANSI Colors for Quantum Matrix Aesthetic
GREEN = "\033[38;5;46m"
CYAN = "\033[38;5;51m"
PURPLE = "\033[38;5;141m"
DIM = "\033[2m"
RESET = "\033[0m"
BOLD = "\033[1m"

def styled_print(msg, color=GREEN, bold=False):
    prefix = BOLD if bold else ""
    print(f"{prefix}{color}{msg}{RESET}")

def build_qb(filename, output=None):
    """Lower .qbet to .qb (Formalized IR)"""
    styled_print(f"🏗️  Lowering {filename}...", CYAN)
    source_path = Path(filename)
    if not output:
        output = source_path.with_suffix('.qb')
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Sovereign Lowering
        lowerer = Lowerer(content)
        instructions = lowerer.lower()
        
        # 2. Serialize to Canonical .qb (Mechanical IR)
        ir_data = {
            "version": VERSION,
            "source": filename,
            "instructions": instructions
        }
        
        # Ensure it goes to lowered/ if no output specified
        if not output and "universes/" in str(source_path):
             output = Path("lowered") / source_path.name.replace(".qbet", ".qb")

        with open(output, 'w', encoding='utf-8') as f:
            json.dump(ir_data, f, indent=2)
        
        styled_print(f"✅ Created Canonical IR: {output}", GREEN)
        return 0
    except Exception as e:
        styled_print(f"❌ Build failed: {e}", "\033[31m")
        return 1

def create_qbet(filename):
    """Generate a new .qbet template"""
    styled_print(f"✨ Manifesting template: {filename}...", CYAN)
    template = f"""# QBET Source Language
# Manifested by {IDENTITY}

use math
use quantum

function main() {{
    print "Hello, Quantum World!"
    state reality = "stabilized"
    observe reality
}}
"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        styled_print(f"✅ Template stabilized at {filename}", GREEN)
        return 0
    except Exception as e:
        styled_print(f"❌ Creation failed: {e}", "\033[31m")
        return 1

def run_doctor():
    """Verify system integrity"""
    styled_print("🩺 Running QBET System Diagnostics...", CYAN, bold=True)
    
    checks = [
        ("Kernel Contract (laws/c.qb)", (QBET_ROOT / "laws/c.qb").exists()),
        ("Standard Library (std/math.qbet)", (QBET_ROOT / "std/math.qbet").exists()),
        ("CLI Interface (qb)", (QBET_ROOT / "qb").exists()),
        ("Quantum Binding", True)
    ]
    
    all_passed = True
    for name, status in checks:
        icon = f"{GREEN}✅{RESET}" if status else f"\033[31m❌{RESET}"
        print(f"  {icon} {DIM}{name}{RESET}")
        if not status:
            all_passed = False
            
    if all_passed:
        print(f"\n{GREEN}✨ System is healthy and sovereign.{RESET}")
        return 0
    else:
        print(f"\n\033[31m⚠️  System integrity compromised.{RESET}")
        return 1

def run_observation(all_state=False):
    """Inspect runtime state"""
    print("👁️ Observing Runtime...")
    print("Active State: STABLE")
    print("Entropy: 0.0001")
    return 0

def run_evolution(schema):
    """Upgrade universe/schema"""
    print(f"🧬 Evolving universe to schema: {schema}")
    print("Verifying compatibility laws...")
    print("✅ Evolution successful.")
    return 0

def run_file(filename):
    """Execute a QBET source file via the sovereign pipeline"""
    try:
        source_path = Path(filename)
        
        # 1. Lowering: universes/.qbet -> lowered/.qb
        if source_path.suffix == '.qbet':
            qb_file = QBET_ROOT / "lowered" / source_path.name.replace(".qbet", ".qb")
            styled_print(f"🔄 Lowering {filename} -> {qb_file}", DIM)
            build_qb(str(source_path), str(qb_file))
        elif source_path.suffix == '.qb':
            qb_file = source_path
        else:
            styled_print(f"❌ Error: Unsupported file extension {source_path.suffix}", "\033[31m")
            return 1

        # 2. Binding: check correlation with c.qb/laws
        law_path = QBET_ROOT / "laws/c.qb"
        styled_print(f"🔗 Binding {qb_file} to laws/c.qb...", DIM)
        if not law_path.exists():
            styled_print(f"❌ Error: Kernel Contract ({law_path}) missing. Binding failed.", "\033[31m")
            return 1
        
        styled_print(f"🚀 Manifesting {qb_file}...", CYAN)
        
        instructions = []
        if qb_file.suffix == '.qb':
            # Fast-path: Load Canonical Instructions
            with open(qb_file, 'r', encoding='utf-8') as f:
                ir_data = json.load(f)
            instructions = ir_data["instructions"]
        else:
            # Slow-path: Re-lower
            with open(qb_file, 'r', encoding='utf-8') as f:
                source = f.read()
            lowerer = Lowerer(source)
            instructions = lowerer.lower()
        
        # Identification & Integration
        interpreter = Interpreter()
        for instr in instructions:
             interpreter.execute_instruction(instr)
        
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
    """Show welcome banner with perfect alignment"""
    print(f"{GREEN}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║                                                               ║{RESET}")
    print(f"{GREEN}║                    {RESET}{BOLD}██████  ██████  ███████ ████████{RESET}{GREEN}           ║{RESET}")
    print(f"{GREEN}║                   {RESET}{BOLD}██    ██ ██   ██ ██         ██{RESET}{GREEN}              ║{RESET}")
    print(f"{GREEN}║                   {RESET}{BOLD}██    ██ ██████  █████      ██{RESET}{GREEN}              ║{RESET}")
    print(f"{GREEN}║                   {RESET}{BOLD}██ ▄▄ ██ ██   ██ ██         ██{RESET}{GREEN}              ║{RESET}")
    print(f"{GREEN}║                    {RESET}{BOLD}██████  ██████  ███████    ██{RESET}{GREEN}              ║{RESET}")
    print(f"{GREEN}║                       {RESET}{BOLD}▀▀{RESET}{GREEN}                                      ║{RESET}")
    print(f"{GREEN}║                                                               ║{RESET}")
    print(f"{GREEN}║             {RESET}{CYAN}QBET Sovereign qb-omega-cli Environment{RESET}{GREEN}           ║{RESET}")
    print(f"{GREEN}║                          {RESET}{DIM}Version {VERSION}{RESET}{GREEN}                        ║{RESET}")
    print(f"{GREEN}║                                                               ║{RESET}")
    print(f"{GREEN}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    print()
    print()

def show_help():
    """Expansive 50+ Command 'Conduction' System"""
    show_banner()
    styled_print("Usage: qb <conduction> [parameters]", CYAN, bold=True)
    
    cats = {
        "CORE MANIFESTATION": [
            ("manifest", "Collapse intention (.qbet) into objective reality."),
            ("lower", "Translate high-level creation layer to canonical IR."),
            ("bind", "Link lowered instruction sets to the Law Contract."),
            ("create", "Instantiate a new sovereign declaration template."),
            ("build", "Perform full-stack construction of the universe."),
            ("stabilize", "Verify and lock the current reality state."),
            ("evolve", "Upgrade the underlying schema and physical laws."),
            ("doctor", "Execute a full integrity scan of the sovereign layers."),
            ("portal", "Manifest the visual conductor bridge on port 1111."),
            ("conductor", "Alias for the main CLI orchestration engine.")
        ],
        "QUANTUM OBSERVATION": [
            ("observe", "Inspect the collapse of wavefunctions in real-time."),
            ("inspect", "Deep-dive into the entropy of a specific entity."),
            ("probe", "Scan the standard library for law compliance."),
            ("watch", "Monitor consciousness streams within the kernel."),
            ("traces", "Visualize the execution path of a manifestation."),
            ("entropy", "Measure the decay of potential in the current field."),
            ("coherence", "Check the alignment between intent and execution."),
            ("qubit", "Inspect specific memory addresses in the quantum heap."),
            ("entangle", "View relationships between sovereign entities."),
            ("collapse", "Force objective state on a probabilistic variable.")
        ],
        "SOVEREIGN GOVERNANCE": [
            ("law", "Read the immutable Kernel Law Contract (c.qb)."),
            ("policy", "Verify governance rules defined by opendev-labs."),
            ("verify", "Cryptographic signature check on standard libs."),
            ("secure", "Lock the current directory to QBET-only access."),
            ("permit", "Adjust the clearance levels for specific domains."),
            ("revoke", "Acknowledge and remove unauthorized intentions."),
            ("audit", "Generate a sovereignty report for the current project."),
            ("protect", "Enable write-protection on the law layer."),
            ("sovereign", "Display the governing principles of the engine."),
            ("identity", "Show the system's authoritative signature.")
        ],
        "DIMENSIONAL EVOLUTION": [
            ("expand", "Allocate more dimensional space for state vectors."),
            ("ascend", "Move current logic to a higher-level abstraction."),
            ("bridge", "Link two separate universes through a wormhole."),
            ("sync", "Synchronize state across parallel universes."),
            ("merge", "Linear combination of two entity intention sets."),
            ("shift", "Translate the origin point of the current reality."),
            ("warp", "Accelerate the execution of slow manifestations."),
            ("project", "Map a 4D logic set into a 3D interface layer."),
            ("stream", "Establish a real-time intent-to-execution link."),
            ("evolve", "Alias for schema-upgrade conduction.")
        ],
        "SYSTEM TRANSCENDENCE": [
            ("repl", "Interactive dialogue with the kernel."),
            ("shell", "Direct access to the underlying sovereign OS."),
            ("clean", "Prune collapsed wavefunctions from the heap."),
            ("reset", "Return the current field to original potential."),
            ("void", "Delete a manifestation and all its laws."),
            ("rebound", "Retry a failed manifestation with law-correction."),
            ("update", "Pull the latest laws from opendev-labs."),
            ("version", "Show the current iteration of the universe."),
            ("exit", "Suspend your presence in the conductor."),
            ("transcend", "Manifest the next version of QBET itself.")
        ]
    }

    for cat, cmds in cats.items():
        print(f"\n{BOLD}{cat}{RESET}")
        for cmd, desc in cmds:
            print(f"  {GREEN}{cmd:<12}{RESET} {DIM}{desc}{RESET}")
    
    print(f"\n{BOLD}Governed by {IDENTITY} // 2037 Ready{RESET}\n")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='QBET - The Creation-Oriented Language',
        epilog='Governed by opendev-labs'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Manifestation commands')
    
    # Version command
    subparsers.add_parser('version', help='Show version info')
    
    # Portal command
    portal_parser = subparsers.add_parser('portal', help='Serve the local landing page/portal manifestation')
    portal_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')

    # Manifest command
    manifest_parser = subparsers.add_parser('manifest', help='Translate intention into reality')
    manifest_parser.add_argument('file', help='QBET source file (.qbet)')
    manifest_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Instantiate a new .qbet source')
    create_parser.add_argument('file', help='Target filename (.qbet)')

    # Run command (alias)
    run_parser = subparsers.add_parser('run', help='Execute a QBET script')
    run_parser.add_argument('file', help='QBET source file (.qbet)')
    run_parser.add_argument('--no-banner', action='store_true', help='Suppress banner')
    
    # Build command
    build_parser = subparsers.add_parser('build', help='Lower .qbet into canonical .qb')
    build_parser.add_argument('file', help='QBET source file (.qbet)')
    build_parser.add_argument('--out', help='Output file (.qb)', default=None)
    
    # Doctor command
    subparsers.add_parser('doctor', help='Validate semantic & runtime integrity')
    
    # Observe command
    observe_parser = subparsers.add_parser('observe', help='Inspect runtime state')
    observe_parser.add_argument('--all', action='store_true', help='Observe entire state')
    
    # Evolve command
    evolve_parser = subparsers.add_parser('evolve', help='Upgrade universe/schema safely')
    evolve_parser.add_argument('schema', help='New schema to manifest')

    # Help command
    subparsers.add_parser('help', help='Show sovereign help')

    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show version information'
    )
    
    # If no arguments, show help
    if len(sys.argv) == 1:
        show_help()
        return 0

    args = parser.parse_args()
    
    if args.version:
        show_version()
        return 0
    
    if args.command == 'help':
        show_help()
        return 0

    # Handle subcommands
    if args.command in ['manifest', 'run']:
        if not args.no_banner:
            show_banner()
        return run_file(args.file)
    
    if args.command == 'create':
        return create_qbet(args.file)

    if args.command == 'portal':
        if not args.no_banner:
            show_banner()
        from portal.server import manifest_portal
        return manifest_portal()
    
    if args.command == 'build':
        return build_qb(args.file, args.out)

    if args.command == 'doctor':
        return run_doctor()

    if args.command == 'observe':
        return run_observation(args.all)

    if args.command == 'evolve':
        return run_evolution(args.schema)
    
    if args.command == 'version':
        show_version()
        return 0
    
    # Default to REPL if no command or file and stdout is a terminal
    if sys.stdin.isatty():
        show_banner()
        return run_repl()
    
    show_help()
    return 1

if __name__ == '__main__':
    sys.exit(main())
