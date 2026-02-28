import http.server
import socketserver
import os
import subprocess
import time
import threading
from .renderer import render_portal
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table
from rich import box

PORT = 1111
console = Console()

class PortalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Manifest the portal from universes/index.qbet and siblings
            from .renderer import render_sovereign_portal
            content = render_sovereign_portal('universes')
            self.wfile.write(content.encode('utf-8'))
        elif self.path == '/gui.qbet':
             # Return raw or parsed content if needed, but usually index handles it
             pass
        else:
            super().do_GET()

    def log_message(self, format, *args):
        pass

def clear_port(port):
    try:
        subprocess.run(['fuser', '-k', f'{port}/tcp'], capture_output=True, check=False)
    except Exception:
        pass

def make_dashboard():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3)
    )
    
    # Header
    header_content = Panel(
        "🌀 [bold #5fff00]QBET SOVEREIGN PORTAL MANIFESTATION[/] 🌀",
        style="white on black",
        box=box.DOUBLE_EDGE
    )
    layout["header"].update(header_content)
    
    # Main View (Telemetry)
    table = Table(box=box.SIMPLE, expand=True, border_style="#5fff00")
    table.add_column("METRIC", style="white bold")
    table.add_column("VALUE", style="#5fff00")
    table.add_row("Port Status", f"Bound to {PORT}")
    table.add_row("Dimensional Sync", "100% (STABLE)")
    table.add_row("Observer Count", "1 Active")
    table.add_row("Law Enforcement", "Active (c.qb)")
    table.add_row("Reality Version", "1.0.0-omega")
    
    layout["main"].update(Panel(table, title="[#5fff00]LIVE TELEMETRY[/]", border_style="#5fff00"))
    
    # Footer
    footer_content = Panel(
        f"✨ [bold white]PORTAL STABILIZED AT:[/] [link=http://localhost:{PORT}]http://localhost:{PORT}[/]  [dim](Press Ctrl+C to collapse)[/]",
        style="white on black",
        box=box.SIMPLE
    )
    layout["footer"].update(footer_content)
    
    return layout

def manifest_portal():
    console.print(f"🌀 [#5fff00]Clearing dimensional interference on port {PORT}...[/]")
    clear_port(PORT)
    
    server_started = threading.Event()
    
    def run_server():
        try:
            socketserver.TCPServer.allow_reuse_address = True
            with socketserver.TCPServer(("", PORT), PortalHandler) as httpd:
                server_started.set()
                httpd.serve_forever()
        except OSError as e:
            console.print(f"❌ [#ffaf00]Portal error: {e}[/]")

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start before showing live dashboard
    time.sleep(1)
    
    try:
        with Live(make_dashboard(), refresh_per_second=4, screen=True):
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n🌙 [#ffaf00]Manifestation suspended. Returning to the void.[/]")
        return 0
