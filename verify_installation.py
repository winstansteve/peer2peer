"""
Installation Verification Script
Run this to check if your system is ready to use the Secure File Transfer App
"""

import sys
import subprocess

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_python_version():
    """Check if Python version is adequate"""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is compatible!")
        return True
    else:
        print("❌ Python 3.8 or higher is required!")
        print("   Please upgrade Python from https://www.python.org/downloads/")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✅ {package_name} is installed")
        return True
    except ImportError:
        print(f"❌ {package_name} is NOT installed")
        return False

def check_all_packages():
    """Check all required packages"""
    print_header("Checking Required Packages")
    
    packages = [
        ("streamlit", "streamlit"),
        ("cryptography", "cryptography"),
        ("flask", "flask"),
        ("flask-cors", "flask_cors"),
        ("pyngrok", "pyngrok"),
        ("requests", "requests"),
    ]
    
    all_installed = True
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_installed = False
    
    return all_installed

def check_ngrok():
    """Check if ngrok is configured"""
    print_header("Checking Ngrok Configuration")
    
    try:
        result = subprocess.run(
            ["ngrok", "config", "check"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 or "valid" in result.stdout.lower():
            print("✅ Ngrok is configured!")
            return True
        else:
            print("⚠️  Ngrok might not be configured properly")
            print("   Run: ngrok config add-authtoken YOUR_TOKEN")
            return False
    except FileNotFoundError:
        print("⚠️  Ngrok command not found")
        print("   Download from https://ngrok.com/download")
        return False
    except Exception as e:
        print(f"⚠️  Could not verify ngrok: {str(e)}")
        return False

def check_ports():
    """Check if required ports are available"""
    print_header("Checking Port Availability")
    
    import socket
    
    def is_port_available(port):
        """Check if a port is available"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            return result != 0  # Port is available if connection fails
        except:
            return False
    
    ports = [5000, 8501]  # Flask and Streamlit ports
    all_available = True
    
    for port in ports:
        if is_port_available(port):
            print(f"✅ Port {port} is available")
        else:
            print(f"⚠️  Port {port} might be in use")
            all_available = False
    
    return all_available

def check_internet():
    """Check internet connectivity"""
    print_header("Checking Internet Connection")
    
    try:
        import requests
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("✅ Internet connection is working!")
            return True
        else:
            print("⚠️  Internet connection might be slow")
            return False
    except:
        print("❌ No internet connection detected")
        print("   Internet connection is required for file transfer")
        return False

def provide_recommendations(results):
    """Provide recommendations based on check results"""
    print_header("Recommendations")
    
    if all(results.values()):
        print("🎉 All checks passed! You're ready to use the app!")
        print("\nTo start the app, run:")
        print("   streamlit run app.py")
        print("\nOr double-click: START_APP.bat")
    else:
        print("⚠️  Some issues were found. Please fix them:")
        
        if not results['python']:
            print("\n1. Update Python:")
            print("   Visit: https://www.python.org/downloads/")
        
        if not results['packages']:
            print("\n2. Install required packages:")
            print("   Run: pip install -r requirements.txt")
        
        if not results['ngrok']:
            print("\n3. Configure ngrok:")
            print("   a. Sign up at: https://ngrok.com/")
            print("   b. Get your auth token")
            print("   c. Run: ngrok config add-authtoken YOUR_TOKEN")
        
        if not results['ports']:
            print("\n4. Free up required ports:")
            print("   Close other applications using ports 5000 or 8501")
        
        if not results['internet']:
            print("\n5. Check your internet connection:")
            print("   Make sure you're connected to the internet")

def main():
    """Main verification function"""
    print("\n" + "🔐 SECURE FILE TRANSFER APP - INSTALLATION CHECKER 🔐".center(60))
    
    results = {
        'python': check_python_version(),
        'packages': check_all_packages(),
        'ngrok': check_ngrok(),
        'ports': check_ports(),
        'internet': check_internet()
    }
    
    provide_recommendations(results)
    
    print_header("Verification Complete")
    
    # Return exit code based on results
    return 0 if all(results.values()) else 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nVerification cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
