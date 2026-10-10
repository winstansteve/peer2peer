"""
Simple Demo Script
Tests the encryption module to ensure it's working correctly
"""

from encryption import generate_key, encrypt_file, decrypt_file
import os

def test_encryption():
    """Test the encryption and decryption functionality"""
    
    print("="*60)
    print("  TESTING ENCRYPTION MODULE")
    print("="*60)
    
    # Create test directories
    os.makedirs("temp", exist_ok=True)
    os.makedirs("keys", exist_ok=True)
    
    # Create a test file
    test_content = "This is a secret message! [ENCRYPTED]\nTesting file encryption and decryption."
    test_file = "temp/test_original.txt"
    encrypted_file = "temp/test_encrypted.enc"
    decrypted_file = "temp/test_decrypted.txt"
    
    print("\n1. Creating test file...")
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    print(f"   ✅ Created: {test_file}")
    print(f"   Content: '{test_content[:30]}...'")
    
    # Generate encryption key
    print("\n2. Generating encryption key...")
    key = generate_key()
    print(f"   ✅ Key generated: {key[:20]}...")
    
    # Encrypt the file
    print("\n3. Encrypting file...")
    encrypt_file(test_file, encrypted_file, key)
    print(f"   ✅ File encrypted: {encrypted_file}")
    
    # Show encrypted content (gibberish)
    with open(encrypted_file, 'rb') as f:
        encrypted_content = f.read()
    print(f"   Encrypted content (first 50 bytes): {encrypted_content[:50]}")
    
    # Decrypt the file
    print("\n4. Decrypting file...")
    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"   ✅ File decrypted: {decrypted_file}")
    
    # Verify decryption
    print("\n5. Verifying decryption...")
    with open(decrypted_file, 'r', encoding='utf-8') as f:
        decrypted_content = f.read()
    
    if decrypted_content == test_content:
        print("   ✅ SUCCESS! Content matches original!")
        print(f"   Decrypted: '{decrypted_content[:30]}...'")
    else:
        print("   ❌ ERROR! Content doesn't match!")
        return False
    
    # Test with wrong key
    print("\n6. Testing with wrong key...")
    wrong_key = generate_key()
    try:
        decrypt_file(encrypted_file, "temp/test_wrong.txt", wrong_key)
        print("   ❌ ERROR! Should have failed with wrong key!")
        return False
    except ValueError:
        print("   ✅ Correctly rejected wrong encryption key!")
    
    # Cleanup
    print("\n7. Cleaning up test files...")
    for file in [test_file, encrypted_file, decrypted_file]:
        if os.path.exists(file):
            os.remove(file)
    print("   ✅ Cleanup complete!")
    
    print("\n" + "="*60)
    print("  ALL TESTS PASSED! ✅")
    print("  Encryption module is working correctly!")
    print("="*60)
    
    return True

if __name__ == "__main__":
    try:
        success = test_encryption()
        if success:
            print("\n🎉 The app is ready to use!")
            print("\nTo start the application:")
            print("   1. Double-click START_APP.bat, OR")
            print("   2. Run: streamlit run app.py")
        else:
            print("\n⚠️  Some tests failed. Please check the installation.")
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        print("   Please run: pip install -r requirements.txt")
