# 🔐 Secure File Transfer App

A user-friendly application to securely send files from one laptop to another over the internet using encryption and ngrok tunneling.

## ✨ Features

- **🔒 End-to-End Encryption**: Files are encrypted before transfer using industry-standard encryption
- **🌐 Internet Transfer**: Send files over the internet using ngrok tunneling
- **👥 User-Friendly**: Simple, self-explanatory interface for non-technical users
- **🚀 Easy Setup**: Just a few steps to start sending or receiving files
- **💾 Any File Type**: Send documents, images, videos, or any other file type

## 📋 Prerequisites

- Python 3.8 or higher installed on your computer
- Internet connection on both laptops
- Ngrok account (free tier works fine)

## 🚀 Installation Guide (For Non-Technical Users)

### Step 1: Download Python

1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or higher
3. Run the installer and **check the box that says "Add Python to PATH"**
4. Click "Install Now"

### Step 2: Set Up Ngrok

1. Go to [ngrok.com](https://ngrok.com/)
2. Sign up for a free account
3. Download ngrok for Windows

**✨ NEW! Easy In-App Configuration:**
The app now has a built-in ngrok setup wizard! Just run the app and follow the on-screen instructions to configure ngrok directly in the UI.

**OR** use the command line method (traditional):
4. After downloading, open Command Prompt (search for "cmd" in Windows)
5. Log in to ngrok with your auth token:
   ```
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```
   (Replace YOUR_AUTH_TOKEN with the token from your ngrok dashboard)

### Step 3: Install the Application

1. Download all the application files to a folder on your computer
2. Open Command Prompt or PowerShell
3. Navigate to the folder where you saved the files:
   ```powershell
   cd "path\to\peer2peer\folder"
   ```
4. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```

## 💻 How to Use

### Starting the Application

1. Open Command Prompt or PowerShell
2. Navigate to the application folder
3. Run the command:
   ```powershell
   streamlit run app.py
   ```
4. Your web browser will automatically open with the application

### Sending a File

1. **Select "Send a File"** from the sidebar
2. **Click "Browse files"** and choose the file you want to send
3. **Click "Start Sharing"** button
4. Wait a few seconds for the connection to set up
5. **Copy both the URL and the Encryption Key** that appear on screen
6. **Send these to the person** who will receive the file (use email, chat, etc.)
   - 💡 **Important**: Send the URL and key separately for better security (e.g., URL via email, key via WhatsApp)
7. **Keep the window open** until the receiver has downloaded the file
8. **Click "Stop Sharing"** when done

### Receiving a File

1. **Select "Receive a File"** from the sidebar
2. **Paste the URL** you received in the "Download URL" box
3. **Paste the Encryption Key** in the "Encryption Key" box
4. **Click "Download File"** button
5. Wait for the file to download and decrypt
6. **Click "Save File"** to save it to your computer
7. Choose where to save the file and you're done! ✅

## 🔒 Security Features

- **File Encryption**: All files are encrypted using Fernet (symmetric encryption) before transfer
- **Unique Keys**: Each file transfer uses a unique encryption key
- **Secure Tunneling**: Ngrok provides HTTPS encrypted tunnels
- **No Storage**: Files are not stored on any server - direct transfer only

## ⚠️ Important Notes

- **Keep the sender's window open** while the receiver downloads the file
- **Both laptops need internet connection**
- **The free ngrok tier has usage limits** - suitable for occasional file transfers
- **Don't share your encryption key publicly** - only share it with the intended recipient
- **Files are automatically cleaned up** after transfer

## 🆘 Troubleshooting

### "Failed to start ngrok"
- Make sure you've set up your ngrok auth token
- Check your internet connection
- Try running: `ngrok config add-authtoken YOUR_AUTH_TOKEN`

### "Failed to download file"
- Make sure the sender is still sharing (window is open)
- Check that you copied the full URL and key correctly
- Verify both laptops have internet connection

### "Decryption failed"
- Double-check that you copied the complete encryption key
- Make sure there are no extra spaces in the key
- Ask the sender to share the key again

### "Port already in use"
- Close any other instances of the application
- Restart your computer if needed

## 📁 File Structure

```
peer2peer/
├── app.py                 # Main Streamlit application
├── encryption.py          # Encryption/decryption functions
├── server.py             # Flask server for file serving
├── ngrok_handler.py      # Ngrok tunnel management
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── temp/                # Temporary files (auto-created)
└── keys/                # Encryption keys (auto-created)
```

## 🔧 Technical Details

- **Frontend**: Streamlit
- **Backend**: Flask
- **Encryption**: Fernet (symmetric encryption from cryptography library)
- **Tunneling**: Ngrok
- **Language**: Python 3.8+

## 📝 License

This project is provided as-is for personal and educational use.

## 🤝 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Make sure all prerequisites are installed correctly
3. Verify your internet connection
4. Ensure ngrok is properly configured

---

**Enjoy secure file transfers! 🎉**

