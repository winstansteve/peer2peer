"""
Configuration file for advanced settings
Modify these values if you need to customize the application
"""

# Server Configuration
SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 5000        # Default Flask port

# Ngrok Configuration
NGROK_REGION = 'us'       # Options: us, eu, ap, au, sa, jp, in
NGROK_AUTH_TOKEN = None   # Set your ngrok auth token here (optional)

# File Storage
TEMP_DIR = 'temp'         # Directory for temporary files
KEYS_DIR = 'keys'         # Directory for encryption keys

# Security Settings
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB max file size
ALLOWED_EXTENSIONS = None  # None = all files allowed, or set to {'pdf', 'png', 'jpg', 'docx'}

# Cleanup Settings
AUTO_CLEANUP = True       # Automatically cleanup temp files after transfer
CLEANUP_DELAY = 5         # Seconds to wait before cleanup (if needed)

# UI Settings
STREAMLIT_THEME = {
    'primaryColor': '#FF4B4B',
    'backgroundColor': '#FFFFFF',
    'secondaryBackgroundColor': '#F0F2F6',
    'textColor': '#262730',
    'font': 'sans serif'
}

# Advanced: Timeout Settings
SERVER_TIMEOUT = 300      # Server timeout in seconds (5 minutes)
NGROK_TIMEOUT = 30        # Ngrok connection timeout in seconds

# Debug Mode
DEBUG_MODE = False        # Set to True for detailed error messages

# Advanced: Encryption Settings
ENCRYPTION_ALGORITHM = 'Fernet'  # Default: Fernet (AES-128)
KEY_ROTATION = False      # Advanced: Enable automatic key rotation

# Logging
ENABLE_LOGGING = True     # Enable application logging
LOG_FILE = 'transfer.log' # Log file name
LOG_LEVEL = 'INFO'        # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Notes for Advanced Users:
# ------------------------
# 1. NGROK_REGION: Choose closest region for better performance
# 2. MAX_FILE_SIZE: Adjust based on your ngrok plan and internet speed
# 3. ALLOWED_EXTENSIONS: Restrict file types for security if needed
# 4. DEBUG_MODE: Only enable when troubleshooting issues
# 5. This file is optional - app works with defaults if not configured
