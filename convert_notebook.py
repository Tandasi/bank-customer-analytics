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
        
    
        import re
    
        body = re.sub(r'<h1[^>]*>.*?Bank Marketing Predictor .*?</h1>', '', body, flags=re.IGNORECASE | re.DOTALL)
        
        # Custom CSS styling - Modern Professional Theme
        custom_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #334155 50%, #475569 75%, #64748b 100%);
            background-attachment: fixed;
            color: #f1f5f9;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.7;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(15, 23, 42, 0.8);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            margin-top: 20px;
            margin-bottom: 20px;
        }
        
        .logo-container {
            text-align: center;
            margin-bottom: 3rem;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .logo {
            max-width: 200px;
            height: auto;
            margin-bottom: 1rem;
            filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.3));
        }
        
        .company-branding {
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            color: #94a3b8;
            margin-top: 0.5rem;
            font-weight: 400;
            letter-spacing: 0.05em;
        }
        
        .header-container {
            background: rgba(30, 41, 59, 0.6);
            border-radius: 16px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 3rem 2rem;
            margin-bottom: 3rem;
            text-align: center;
            backdrop-filter: blur(10px);
        }
        
        h1 {
            font-family: 'Inter', sans-serif;
            font-size: 3rem;
            font-weight: 700;
            color: #f8fafc;
            text-align: center;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        h2 {
            font-family: 'Inter', sans-serif;
            font-size: 1.25rem;
            font-weight: 500;
            color: #94a3b8;
            text-align: center;
            margin: 0;
            letter-spacing: 0.05em;
        }
        
        h3 {
            font-family: 'Inter', sans-serif;
            font-size: 1.5rem;
            font-weight: 600;
            color: #e2e8f0;
            margin: 2rem 0 1rem 0;
            text-transform: none;
            letter-spacing: -0.01em;
        }
        
        p, li, div, .text_cell_render, .markdown_text, * {
            color: #cbd5e1 !important;
        }
        
        .cell {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 12px;
            margin: 2rem 0;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
        }
        
        .input {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            color: #f1f5f9;
        }
        
        .output {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            color: #f1f5f9;
        }
        
        pre, code, .highlight, .highlight * {
            color: #f1f5f9 !important;
            background: rgba(15, 23, 42, 0.9) !important;
            font-family: 'JetBrains Mono', monospace;
        }
        
        pre {
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            padding: 1.5rem;
            overflow-x: auto;
            font-size: 0.9rem;
            line-height: 1.6;
        }
        
        code {
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        
        table, table *, td, th {
            color: #f1f5f9 !important;
            background: rgba(30, 41, 59, 0.6) !important;
        }
        
        table {
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            margin: 1.5rem 0;
            width: 100%;
            border-collapse: collapse;
            overflow: hidden;
        }
        
        th {
            background: rgba(15, 23, 42, 0.8) !important;
            color: #e2e8f0 !important;
            padding: 1rem;
            font-weight: 600;
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
        }
        
        td {
            padding: 1rem;
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
        }
        
        .jp-Cell-inputWrapper, .jp-Cell-outputWrapper, .jp-InputArea, .jp-OutputArea {
            background: rgba(30, 41, 59, 0.4) !important;
            border: 1px solid rgba(148, 163, 184, 0.1) !important;
            border-radius: 8px;
        }
        
        .header-container {
            background: rgba(202, 213, 221, 0.05);
            border-radius: 10px;
            border: 1px solid #7d95b1;
            padding: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(125, 149, 177, 0.2);
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
        
        .navigation {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin: 3rem 0;
        }
        
        .nav-button {
            display: inline-block;
            background: linear-gradient(135deg, #1e293b, #334155);
            color: #f8fafc;
            padding: 14px 28px;
            margin: 0;
            text-decoration: none;
            border-radius: 12px;
            border: 1px solid rgba(148, 163, 184, 0.3);
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            text-transform: none;
            letter-spacing: 0.02em;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        .nav-button:hover {
            background: linear-gradient(135deg, #334155, #475569);
            border-color: rgba(148, 163, 184, 0.5);
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
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
            <link rel="icon" type="image/png" href="angatech-high-resolution-logo.png">
            <link rel="shortcut icon" type="image/png" href="angatech-high-resolution-logo.png">
            {custom_css}
        </head>
        <body>
            <div class="retro-grid"></div>
            <div class="container">
                <div class="logo-container">
                    <img src="angatech-high-resolution-logo.png" alt="AngaTech Logo" class="logo">
                    <div class="company-branding">Powered by AngaTech - Innovative Technology Solutions</div>
                </div>
                
                <div class="header-container">
                    <h1 class="glitch">Bank Marketing Predictor</h1>
                    <h2>Machine Learning Pipeline</h2>
                </div>
                
                <div class="navigation">
                    <a href="https://bank-customer-analytics.streamlit.app/" class="nav-button" target="_blank">Launch Streamlit App</a>
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
