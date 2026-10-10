"""
Encryption Module
Handles file encryption and decryption using Fernet (symmetric encryption)
"""

from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A new encryption key
    """
    return Fernet.generate_key()

def save_key(key, key_path):
    """
    Save encryption key to a file.
    
    Args:
        key (bytes): The encryption key
        key_path (str): Path to save the key
    """
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def load_key(key_path):
    """
    Load encryption key from a file.
    
    Args:
        key_path (str): Path to the key file
        
    Returns:
        bytes: The encryption key
    """
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def encrypt_file(input_path, output_path, key):
    """
    Encrypt a file using the provided key.
    
    Args:
        input_path (str): Path to the file to encrypt
        output_path (str): Path to save the encrypted file
        key (bytes): Encryption key
    """
    fernet = Fernet(key)
    
    # Read the original file
    with open(input_path, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)
    
    # Write the encrypted file
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(input_path, output_path, key):
    """
    Decrypt a file using the provided key.
    
    Args:
        input_path (str): Path to the encrypted file
        output_path (str): Path to save the decrypted file
        key (bytes): Encryption key
    """
    fernet = Fernet(key)
    
    # Read the encrypted file
    with open(input_path, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError("Decryption failed. Please check the encryption key.")
    
    # Write the decrypted file
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_data(data, key):
    """
    Encrypt data (bytes) using the provided key.
    
    Args:
        data (bytes): Data to encrypt
        key (bytes): Encryption key
        
    Returns:
        bytes: Encrypted data
    """
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(encrypted_data, key):
    """
    Decrypt data (bytes) using the provided key.
    
    Args:
        encrypted_data (bytes): Encrypted data
        key (bytes): Encryption key
        
    Returns:
        bytes: Decrypted data
    """
    fernet = Fernet(key)
    try:
        return fernet.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError("Decryption failed. Please check the encryption key.")
