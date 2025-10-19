# Bank Marketing ML Pipeline - HTTP Version

## 🌐 Shareable HTML Notebook

This repository includes an HTTP version of the Bank Marketing ML Pipeline that can be easily shared and accessed via web browser.

## 🚀 Quick Start

### Option 1: Use the Batch File (Windows)
```bash
start_http_server.bat
```

### Option 2: Run Python Server Directly
```bash
python http_server.py
```

### Option 3: Specify Custom Port
```bash
python http_server.py 8081
```

## 📊 Access Points

Once the server is running, you can access:

- **📓 HTML Notebook**: `http://localhost:8080/bank_marketing_http.html`
- **🎮 Streamlit App**: `http://localhost:8080/streamlit_deploy.py`
- **📊 Dataset**: `http://localhost:8080/data/bank_marketing_complete.csv`
- **📋 Requirements**: `http://localhost:8080/requirements.txt`

## 🎨 Features

- **Professional Dark Theme**: Blue-gray color scheme matching the Streamlit app
- **Interactive Navigation**: Direct links to Streamlit app and dataset
- **Responsive Design**: Works on desktop and mobile devices
- **Clean Typography**: Professional fonts and styling
- **Easy Sharing**: Share the localhost URL with others on your network

## 🔗 Sharing

To share with others on your network:
1. Find your local IP address
2. Replace `localhost` with your IP address
3. Share the URL: `http://YOUR_IP:8080/bank_marketing_http.html`

## 📁 Files Included

- `bank_marketing_http.html` - The HTML notebook
- `http_server.py` - Python HTTP server
- `start_http_server.bat` - Windows batch file for easy startup
- `convert_notebook.py` - Script to regenerate HTML from notebook

## 🛠️ Customization

To regenerate the HTML with updated notebook:
```bash
python convert_notebook.py
```

## 📝 Notes

- The server automatically opens your browser to the notebook
- Press `Ctrl+C` to stop the server
- The HTML version maintains all the professional styling and navigation
- Perfect for presentations, sharing, or offline viewing
