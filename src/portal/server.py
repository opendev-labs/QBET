import http.server
import socketserver
import os
from .renderer import render_portal

PORT = 1111

class PortalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Manifest the portal from index.qbet
            content = render_portal('index.qbet')
            self.wfile.write(content.encode('utf-8'))
        else:
            super().do_GET()

    def log_message(self, format, *args):
        # Suppress host logging to keep the UI sovereign
        pass

def manifest_portal():
    print(f"🌀 Manifesting universe from index.qbet...")
    print(f"✨ Portal stabilizing on http://localhost:{PORT}")
    
    try:
        with socketserver.TCPServer(("", PORT), PortalHandler) as httpd:
            print("🌟 Observer bound. Presence established.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🌙 Manifestation suspended. Returning to the void.")
        return 0
    except OSError as e:
        if e.errno == 98:
            print(f"❌ Error: Port {PORT} is already occupied by another reality.")
        else:
            print(f"❌ Portal error: {e}")
        return 1
