#!/usr/bin/env python3
"""
Convert Jupyter Notebook to HTML with custom styling
"""

import nbconvert
import os
from pathlib import Path

def convert_notebook_to_html():
    """Convert the Jupyter notebook to HTML with custom styling"""
    
    # Input and output file paths
    notebook_path = "bank_marketing_complete.ipynb"
    html_path = "bank_marketing_http.html"
    
    try:
        # Create HTML exporter with custom template
        exporter = nbconvert.HTMLExporter()
        
        # Convert notebook to HTML
        (body, resources) = exporter.from_filename(notebook_path)
        
        # Remove duplicate headers from notebook content
        import re
        # Remove the first h1 header from notebook content to avoid duplication
        body = re.sub(r'<h1[^>]*>.*?Bank Marketing Predictor.*?</h1>', '', body, flags=re.IGNORECASE | re.DOTALL)
        
        # Custom CSS styling - Retro Futurism Theme
        custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Press+Start+2P&family=Rajdhani:wght@300;400;500;600;700&display=swap');
        
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            background-attachment: fixed;
            color: #00ffff;
            font-family: 'Rajdhani', sans-serif;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(10px);
            border: 2px solid #00ffff;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
        }
        
        h1 {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.5rem;
            font-weight: 600;
            color: #00ffff;
            text-align: center;
            margin-bottom: 1rem;
            letter-spacing: 0.05em;
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
        }
        
        h2 {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.4rem;
            font-weight: 500;
            color: #ff00ff;
            text-align: center;
            margin: 0 0 2rem 0;
            letter-spacing: 0.1em;
            text-shadow: 0 0 5px rgba(255, 0, 255, 0.3);
        }
        
        h3 {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.5rem;
            font-weight: 600;
            color: #ff00ff;
            margin: 1.5rem 0 0.5rem 0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .cell {
            background: linear-gradient(145deg, rgba(0, 0, 0, 0.8), rgba(26, 26, 46, 0.9));
            border: 2px solid #00ffff;
            border-radius: 15px;
            margin: 1rem 0;
            padding: 1rem;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
            backdrop-filter: blur(5px);
        }
        
        .input {
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid #ff00ff;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            color: #00ffff;
        }
        
        .output {
            background: rgba(26, 26, 46, 0.9);
            border: 2px solid #ffff00;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            color: #ffffff;
        }
        
        pre {
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid #00ffff;
            border-radius: 8px;
            padding: 1rem;
            color: #00ff00;
            font-family: 'Press Start 2P', monospace;
            overflow-x: auto;
        }
        
        code {
            background: rgba(0, 0, 0, 0.8);
            color: #00ff00;
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-family: 'Press Start 2P', monospace;
        }
        
        table {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #00ffff;
            border-radius: 8px;
            color: #ffffff;
            margin: 1rem 0;
        }
        
        th {
            background: rgba(0, 255, 255, 0.3);
            color: #000000;
            padding: 0.5rem;
            border-bottom: 2px solid #00ffff;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        td {
            padding: 0.5rem;
            border-bottom: 1px solid rgba(0, 255, 255, 0.3);
        }
        
        p, li, div, .text_cell_render, .markdown_text, * {
            color: #00ffff !important;
        }
        
        pre, code, .highlight, .highlight * {
            color: #00ff00 !important;
            background: rgba(0, 0, 0, 0.9) !important;
        }
        
        table, table *, td, th {
            color: #ffffff !important;
            background: rgba(0, 0, 0, 0.8) !important;
        }
        
        th {
            background: rgba(0, 255, 255, 0.3) !important;
            color: #000000 !important;
        }
        
        .jp-Cell-inputWrapper, .jp-Cell-outputWrapper, .jp-InputArea, .jp-OutputArea {
            background: rgba(0, 0, 0, 0.8) !important;
            border: 2px solid #00ffff !important;
        }
        
        .logo-container {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
        }
        
        .logo {
            max-height: 80px;
            width: auto;
            margin-bottom: 1rem;
            filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.3));
        }
        
        .company-branding {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1rem;
            color: #7d95b1;
            margin-top: 0.5rem;
            font-style: italic;
        }
        
        .nav-button {
            display: inline-block;
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            color: #000000;
            padding: 12px 24px;
            margin: 0 10px;
            text-decoration: none;
            border-radius: 8px;
            border: 2px solid #ffff00;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(255, 0, 255, 0.5);
        }
        
        .nav-button:hover {
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            border-color: #00ff00;
            transform: translateY(-2px);
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.7);
        }
        
        /* Retro Grid Background */
        .retro-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 255, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 255, 0.1) 1px, transparent 1px);
            background-size: 20px 20px;
            pointer-events: none;
            z-index: -1;
        }
        
        /* Glitch Effect */
        .glitch {
            animation: glitch 2s infinite;
        }
        
        @keyframes glitch {
            0%, 100% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(-2px, -2px); }
            60% { transform: translate(2px, 2px); }
            80% { transform: translate(2px, -2px); }
        }
        </style>
        """
        
        # Create complete HTML document
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bank Marketing Predictor - ML Pipeline</title>
            {custom_css}
        </head>
        <body>
            <div class="retro-grid"></div>
            <div class="container">
                <div class="logo-container">
                    <img src="angatech-high-resolution-logo.png" alt="AngaTech Logo" class="logo">
                    <div class="company-branding">Powered by AngaTech - Innovative Technology Solutions</div>
                </div>
                
                <h1 class="glitch">Bank Marketing Predictor</h1>
                <h2>Machine Learning Pipeline</h2>
                
                <div class="navigation">
                    <a href="streamlit_deploy.py" class="nav-button" target="_blank">Launch Streamlit App</a>
                    <a href="data/bank_marketing_complete.csv" class="nav-button" download>Download Dataset</a>
                    <a href="bank_marketing_complete.ipynb" class="nav-button" download>Download Notebook</a>
                </div>
                
                <div class="notebook-content">
                    {body}
                </div>
            </div>
        </body>
        </html>
        """
        
        # Write HTML file
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Successfully converted notebook to HTML: {html_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting notebook: {str(e)}")
        return False

if __name__ == "__main__":
    convert_notebook_to_html()
