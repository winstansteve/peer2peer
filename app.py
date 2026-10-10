"""
Peer-to-Peer File Transfer Application with Encryption
A user-friendly app for securely sending files between laptops over the internet.
"""

import streamlit as st
import os
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Secure File Transfer",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import components
from server import start_server, stop_server
from encryption import generate_key, save_key, load_key
from ngrok_handler import start_ngrok, stop_ngrok, get_public_url

def check_installed_packages():
    """Check which required packages are installed"""
    required_packages = {
        'streamlit': 'streamlit',
        'cryptography': 'cryptography',
        'flask': 'flask',
        'flask-cors': 'flask_cors',
        'pyngrok': 'pyngrok',
        'requests': 'requests'
    }
    
    missing_packages = []
    installed_packages = []
    
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            installed_packages.append(package_name)
        except ImportError:
            missing_packages.append(package_name)
    
    return {
        'missing': missing_packages,
        'installed': installed_packages,
        'all_installed': len(missing_packages) == 0
    }

def install_packages(packages):
    """Install a list of packages using pip"""
    import subprocess
    import sys
    
    try:
        # Upgrade pip first
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Install packages
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install"] + packages,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes timeout
        )
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr
        }
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': str(e)
        }

def check_ngrok_configured():
    """Check if ngrok is already configured with an auth token"""
    try:
        import subprocess
        result = subprocess.run(
            ["ngrok", "config", "check"],
            capture_output=True,
            text=True,
            timeout=5
        )
        # If ngrok is configured, this command should succeed
        return result.returncode == 0 or "valid" in result.stdout.lower()
    except:
        return False

def configure_ngrok_token(token):
    """Configure ngrok with the provided auth token"""
    try:
        import subprocess
        result = subprocess.run(
            ["ngrok", "config", "add-authtoken", token],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except Exception as e:
        return False

def show_ngrok_setup_screen():
    """Display ngrok setup screen for first-time configuration"""
    st.markdown("---")
    
    # Header with icon
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🚇 Ngrok Setup Required")
    
    st.info("👋 Welcome! Before you can transfer files, we need to set up ngrok for secure tunneling.")
    
    # Expandable instructions
    with st.expander("📖 What is ngrok and why do I need it?", expanded=True):
        st.markdown("""
        **Ngrok** creates a secure tunnel so that files can be transferred over the internet between two laptops.
        
        Think of it as creating a temporary bridge between your computer and the internet that only works for this app.
        
        **It's safe, free, and takes just 2 minutes to set up!**
        """)
    
    # Step-by-step setup instructions
    st.markdown("### 📝 Setup Steps:")
    
    st.markdown("""
    **Step 1:** Create a free ngrok account
    - Go to: [ngrok.com](https://ngrok.com/)
    - Click "Sign up" (it's free!)
    - Use Google/GitHub or email to sign up
    """)
    
    st.markdown("""
    **Step 2:** Get your authentication token
    - After signing up, you'll see your dashboard
    - Look for "Your Authtoken" section
    - Click "Copy" to copy your token
    """)
    
    st.image("https://ngrok.com/static/img/docs/agent-token.png", caption="Find your token in the ngrok dashboard", use_container_width=True)
    
    st.markdown("**Step 3:** Paste your token below")
    
    # Token input
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        ngrok_token = st.text_input(
            "Paste your ngrok auth token here:",
            type="password",
            placeholder="2a_very_long_string_of_characters_here",
            help="Your token should be a long string of letters and numbers. Keep it secret!"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        configure_button = st.button("🚀 Configure", type="primary", use_container_width=True)
    
    # Configuration action
    if configure_button:
        if not ngrok_token or len(ngrok_token) < 20:
            st.error("❌ Please enter a valid ngrok token. It should be a long string of characters.")
        else:
            with st.spinner("⏳ Configuring ngrok..."):
                success = configure_ngrok_token(ngrok_token)
                
                if success:
                    st.session_state.ngrok_configured = True
                    st.success("✅ Ngrok configured successfully!")
                    st.balloons()
                    st.info("🎉 You're all set! Click the button below to start using the app.")
                    
                    if st.button("🚀 Start Using App", type="primary"):
                        st.rerun()
                else:
                    st.error("❌ Failed to configure ngrok. Please check your token and try again.")
                    st.info("Make sure you copied the complete token from your ngrok dashboard.")
    
    # Additional help
    st.markdown("---")
    with st.expander("❓ Need Help?"):
        st.markdown("""
        **Common Issues:**
        
        1. **"Invalid token" error:**
           - Make sure you copied the ENTIRE token
           - Check for any extra spaces at the beginning or end
           - Get a fresh token from your ngrok dashboard
        
        2. **"Ngrok command not found":**
           - Download ngrok from: https://ngrok.com/download
           - Install it on your computer
           - Restart this app
        
        3. **Still having trouble?**
           - Make sure you're logged in to ngrok.com
           - Try copying the token again
           - Check your internet connection
        
        **Video Tutorial:** [How to get ngrok token](https://www.youtube.com/results?search_query=ngrok+get+auth+token)
        """)
    
    # Skip option for advanced users
    with st.expander("⚙️ Advanced: Already configured ngrok via command line?"):
        st.markdown("""
        If you've already configured ngrok using the command line:
        ```
        ngrok config add-authtoken YOUR_TOKEN
        ```
        
        Click the button below to skip this setup:
        """)
        
        if st.button("✓ I've already configured ngrok"):
            st.session_state.ngrok_configured = True
            st.rerun()

# Initialize session state
if 'server_running' not in st.session_state:
    st.session_state.server_running = False
if 'public_url' not in st.session_state:
    st.session_state.public_url = None
if 'encryption_key' not in st.session_state:
    st.session_state.encryption_key = None
if 'mode' not in st.session_state:
    st.session_state.mode = None
if 'ngrok_configured' not in st.session_state:
    st.session_state.ngrok_configured = check_ngrok_configured()
if 'show_ngrok_setup' not in st.session_state:
    st.session_state.show_ngrok_setup = False

def main():
    st.title("🔐 Secure File Transfer")
    st.markdown("Send files securely between laptops over the internet")
    
    # Check for missing packages first
    pkg_status = check_installed_packages()
    if not pkg_status['all_installed']:
        st.warning(f"⚠️ {len(pkg_status['missing'])} required package(s) are missing!")
        
        st.markdown("### 📦 Missing Dependencies")
        st.markdown("The following packages need to be installed:")
        for pkg in pkg_status['missing']:
            st.text(f"✗ {pkg}")
        
        st.markdown("---")
        st.markdown("**Option 1: Install via UI (Recommended)**")
        if st.button("📥 Install Missing Packages Now", type="primary", key="install_startup"):
            with st.spinner(f"Installing {len(pkg_status['missing'])} package(s)... Please wait."):
                result = install_packages(pkg_status['missing'])
                
                if result['success']:
                    st.success("✅ Packages installed successfully!")
                    st.balloons()
                    st.info("🔄 Please restart the app to continue.")
                    st.stop()
                else:
                    st.error("❌ Installation failed.")
                    if result['error']:
                        st.markdown("**Error Details:**")
                        st.code(result['error'], language='text')
        
        st.markdown("---")
        st.markdown("**Option 2: Install via Command Line**")
        st.code("pip install -r requirements.txt", language='bash')
        st.caption("Run this command in PowerShell or Command Prompt")
        
        st.stop()
    
    # Check ngrok configuration
    if not st.session_state.ngrok_configured:
        show_ngrok_setup_screen()
        return
    
    # Sidebar for mode selection
    with st.sidebar:
        st.header("Choose Your Action")
        mode = st.radio(
            "What would you like to do?",
            ["📤 Send a File", "📥 Receive a File"],
            help="Select whether you want to send or receive a file"
        )
        
        st.markdown("---")
        st.markdown("### How it works:")
        st.markdown("""
        **To Send:**
        1. Click 'Send a File'
        2. Upload your file
        3. Click 'Start Sharing'
        4. Share the URL and key with receiver
        
        **To Receive:**
        1. Click 'Receive a File'
        2. Enter the URL and key from sender
        3. Click 'Download File'
        4. Save your file
        """)
        
        st.markdown("---")
        
        # Settings section
        with st.expander("⚙️ Settings"):
            st.markdown("**📦 Dependencies**")
            
            # Check package status
            pkg_status = check_installed_packages()
            
            if pkg_status['all_installed']:
                st.caption("✅ All required packages are installed")
            else:
                st.warning(f"⚠️ {len(pkg_status['missing'])} package(s) missing")
            
            if st.button("🔍 Check Dependencies", key="check_deps"):
                with st.spinner("Checking installed packages..."):
                    pkg_status = check_installed_packages()
                    
                    if pkg_status['all_installed']:
                        st.success(f"✅ All {len(pkg_status['installed'])} required packages are installed!")
                        st.markdown("**📋 Installed Packages:**")
                        for pkg in pkg_status['installed']:
                            st.text(f"✓ {pkg}")
                    else:
                        st.error(f"❌ {len(pkg_status['missing'])} package(s) missing")
                        
                        st.markdown("**📋 Package Status:**")
                        st.markdown("**✅ Installed:**")
                        for pkg in pkg_status['installed']:
                            st.text(f"✓ {pkg}")
                        
                        st.markdown("**❌ Missing:**")
                        for pkg in pkg_status['missing']:
                            st.text(f"✗ {pkg}")
                        
                        st.markdown("---")
                        if st.button("📥 Install Missing Packages", type="primary", key="install_deps"):
                            with st.spinner(f"Installing {len(pkg_status['missing'])} package(s)... This may take a few minutes."):
                                result = install_packages(pkg_status['missing'])
                                
                                if result['success']:
                                    st.success("✅ Packages installed successfully!")
                                    st.balloons()
                                    st.info("🔄 Please restart the app to use the newly installed packages.")
                                    
                                    if result['output']:
                                        st.markdown("**📄 Installation Log:**")
                                        st.code(result['output'], language='text')
                                else:
                                    st.error("❌ Installation failed. Please try manually.")
                                    if result['error']:
                                        st.markdown("**❌ Error Details:**")
                                        st.code(result['error'], language='text')
                                    st.info("💡 Try running: `pip install -r requirements.txt` in your terminal")
            
            st.markdown("---")
            st.markdown("**🚇 Ngrok Configuration**")
            st.caption("✅ Ngrok is configured and ready")
            
            if st.button("🔄 Reconfigure Ngrok Token"):
                st.session_state.ngrok_configured = False
                st.rerun()
            
            st.markdown("---")
            st.markdown("**ℹ️ About**")
            st.caption("Secure File Transfer v1.1")
            st.caption("Encrypted peer-to-peer file sharing")
    
    if mode == "📤 Send a File":
        send_file_mode()
    else:
        receive_file_mode()

def send_file_mode():
    st.header("📤 Send a File")
    st.markdown("Upload a file to securely share with another person")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a file to send",
        help="Select any file from your computer"
    )
    
    if uploaded_file is not None:
        st.success(f"✓ File ready: {uploaded_file.name}")
        st.info(f"File size: {uploaded_file.size / 1024:.2f} KB")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🚀 Start Sharing", type="primary", disabled=st.session_state.server_running):
                with st.spinner("Setting up secure connection..."):
                    try:
                        # Create directories
                        os.makedirs("temp", exist_ok=True)
                        os.makedirs("keys", exist_ok=True)
                        
                        # Save uploaded file temporarily
                        file_path = os.path.join("temp", uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        
                        # Generate encryption key
                        key = generate_key()
                        st.session_state.encryption_key = key
                        save_key(key, "keys/sender_key.key")
                        
                        # Start server
                        start_server(file_path, key)
                        st.session_state.server_running = True
                        
                        # Start ngrok tunnel
                        public_url = start_ngrok(5000)
                        st.session_state.public_url = public_url
                        
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        with col2:
            if st.button("🛑 Stop Sharing", disabled=not st.session_state.server_running):
                stop_server()
                stop_ngrok()
                st.session_state.server_running = False
                st.session_state.public_url = None
                st.session_state.encryption_key = None
                st.rerun()
    
    # Display sharing information
    if st.session_state.server_running and st.session_state.public_url:
        st.success("🎉 Your file is now being shared!")
        
        st.markdown("---")
        st.markdown("### 📋 Share these details with the receiver:")
        
        # URL
        st.markdown("**Download URL:**")
        st.code(st.session_state.public_url, language=None)
        
        # Encryption Key
        st.markdown("**Encryption Key:**")
        key_str = st.session_state.encryption_key.decode('utf-8')
        st.code(key_str, language=None)
        
        st.warning("⚠️ Keep this window open while the receiver downloads the file!")
        st.info("💡 Send both the URL and the key to the receiver through a secure channel (e.g., different messaging apps)")

def receive_file_mode():
    st.header("📥 Receive a File")
    st.markdown("Download a file that someone is sharing with you")
    
    # Input fields
    download_url = st.text_input(
        "Enter the Download URL",
        placeholder="https://xxxx.ngrok.io",
        help="Paste the URL you received from the sender"
    )
    
    encryption_key = st.text_area(
        "Enter the Encryption Key",
        placeholder="Paste the encryption key here",
        help="Paste the encryption key you received from the sender"
    )
    
    if st.button("📥 Download File", type="primary"):
        if not download_url or not encryption_key:
            st.error("Please enter both the URL and the encryption key")
        else:
            with st.spinner("Downloading and decrypting file..."):
                try:
                    import requests
                    from encryption import decrypt_file
                    
                    # Download encrypted file
                    response = requests.get(f"{download_url}/download")
                    
                    if response.status_code == 200:
                        # Save encrypted file
                        os.makedirs("temp", exist_ok=True)
                        encrypted_path = "temp/encrypted_download.enc"
                        
                        with open(encrypted_path, "wb") as f:
                            f.write(response.content)
                        
                        # Get original filename from headers
                        filename = response.headers.get('X-Original-Filename', 'downloaded_file')
                        
                        # Decrypt file
                        decrypted_path = f"temp/decrypted_{filename}"
                        decrypt_file(encrypted_path, decrypted_path, encryption_key.encode())
                        
                        # Offer download
                        with open(decrypted_path, "rb") as f:
                            st.download_button(
                                label="💾 Save File",
                                data=f.read(),
                                file_name=filename,
                                mime="application/octet-stream"
                            )
                        
                        st.success(f"✓ File decrypted successfully: {filename}")
                        
                        # Cleanup
                        os.remove(encrypted_path)
                        os.remove(decrypted_path)
                    else:
                        st.error("Failed to download file. Please check the URL and try again.")
                        
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Make sure the URL is correct and the sender is still sharing the file")

if __name__ == "__main__":
    main()
