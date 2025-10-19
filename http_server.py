#!/usr/bin/env python3
"""
Simple HTTP Server for Bank Marketing ML Pipeline
Serves the HTML notebook and related files
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def start_server(port=8080):
    """Start HTTP server to serve the notebook and files"""
    
    # Change to the directory containing the files
    os.chdir(Path(__file__).parent)
    
    # Create HTTP server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🚀 Server starting on port {port}")
            print(f"📊 Serving Bank Marketing ML Pipeline")
            print(f"🌐 Open your browser to: http://localhost:{port}")
            print(f"📓 Notebook: http://localhost:{port}/bank_marketing_http.html")
            print(f"🎮 Streamlit App: http://localhost:{port}/streamlit_deploy.py")
            print(f"📊 Dataset: http://localhost:{port}/data/bank_marketing_complete.csv")
            print(f"\n⏹️  Press Ctrl+C to stop the server")
            
            # Auto-open browser
            webbrowser.open(f"http://localhost:{port}/bank_marketing_http.html")
            
            # Start serving
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {port} is already in use. Trying port {port + 1}")
            start_server(port + 1)
        else:
            print(f"❌ Error starting server: {e}")
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Get port from command line argument or use default
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    start_server(port)
