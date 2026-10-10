"""
Server Module
Flask server for handling file uploads and downloads
"""

from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
import os
import threading
from encryption import encrypt_file

app = Flask(__name__)
CORS(app)

# Global variables
current_file = None
encryption_key = None
server_thread = None

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "status": "online",
        "message": "File transfer server is running"
    })

@app.route('/download')
def download():
    """Download endpoint for encrypted file"""
    global current_file, encryption_key
    
    if not current_file or not os.path.exists(current_file):
        return jsonify({"error": "No file available"}), 404
    
    try:
        # Create encrypted version
        encrypted_path = current_file + ".enc"
        encrypt_file(current_file, encrypted_path, encryption_key)
        
        # Get original filename
        filename = os.path.basename(current_file)
        
        # Send encrypted file
        response = send_file(
            encrypted_path,
            as_attachment=True,
            download_name=f"encrypted_{filename}",
            mimetype='application/octet-stream'
        )
        
        # Add custom header with original filename
        response.headers['X-Original-Filename'] = filename
        
        # Cleanup encrypted file after sending
        @response.call_on_close
        def cleanup():
            if os.path.exists(encrypted_path):
                try:
                    os.remove(encrypted_path)
                except:
                    pass
        
        return response
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status')
def status():
    """Status endpoint"""
    global current_file
    
    return jsonify({
        "status": "online",
        "file_available": current_file is not None and os.path.exists(current_file),
        "filename": os.path.basename(current_file) if current_file else None
    })

def run_flask_app():
    """Run Flask app in production mode"""
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def start_server(file_path, key):
    """
    Start the Flask server with a file to share.
    
    Args:
        file_path (str): Path to the file to share
        key (bytes): Encryption key
    """
    global current_file, encryption_key, server_thread
    
    current_file = file_path
    encryption_key = key
    
    # Start server in a separate thread
    if server_thread is None or not server_thread.is_alive():
        server_thread = threading.Thread(target=run_flask_app, daemon=True)
        server_thread.start()

def stop_server():
    """Stop the Flask server"""
    global current_file, encryption_key
    
    current_file = None
    encryption_key = None
    # Note: Flask server will continue running but won't serve files
