"""
Ngrok Handler Module
Manages ngrok tunneling for public URL generation
"""

from pyngrok import ngrok, conf
import os
import subprocess

# Global variable to store tunnel
active_tunnel = None

def is_ngrok_installed():
    """Check if ngrok is installed and accessible"""
    try:
        result = subprocess.run(
            ["ngrok", "version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except:
        return False

def is_ngrok_configured():
    """Check if ngrok has an auth token configured"""
    try:
        result = subprocess.run(
            ["ngrok", "config", "check"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0 or "valid" in result.stdout.lower()
    except:
        return False

def start_ngrok(port=5000):
    """
    Start ngrok tunnel to expose local server.
    
    Args:
        port (int): Local port to expose
        
    Returns:
        str: Public URL
    """
    global active_tunnel
    
    try:
        # Check if ngrok is configured
        if not is_ngrok_configured():
            raise Exception("Ngrok is not configured. Please configure your auth token first.")
        
        # Set ngrok configuration
        conf.get_default().monitor_thread = False
        
        # Close any existing tunnels
        try:
            ngrok.kill()
        except:
            pass
        
        # Start new tunnel
        active_tunnel = ngrok.connect(port, bind_tls=True)
        public_url = active_tunnel.public_url
        
        return public_url
        
    except Exception as e:
        raise Exception(f"Failed to start ngrok: {str(e)}")

def stop_ngrok():
    """Stop ngrok tunnel"""
    global active_tunnel
    
    try:
        if active_tunnel:
            ngrok.disconnect(active_tunnel.public_url)
            active_tunnel = None
        ngrok.kill()
    except:
        pass

def get_public_url():
    """
    Get the current public URL.
    
    Returns:
        str: Public URL or None
    """
    global active_tunnel
    return active_tunnel.public_url if active_tunnel else None

def get_tunnels():
    """
    Get all active tunnels.
    
    Returns:
        list: List of active tunnels
    """
    try:
        return ngrok.get_tunnels()
    except:
        return []
