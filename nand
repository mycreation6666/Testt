from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Encryption key same as used during encryption
encryption_key = "Join - @creativeydv Channel ON TG".encode('utf-8')

# Path to the encrypted file
encrypted_file_path = 'nand.py.enc'

# Read the encrypted file content
with open(encrypted_file_path, 'rb') as f:
    encrypted_data = base64.b64decode(f.read())

# Prepare decryption
cipher = AES.new(encryption_key[:16], AES.MODE_ECB)  # Using same key for decryption
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# Save the decrypted file
decrypted_file_path = 'z.py'
with open(decrypted_file_path, 'wb') as f_decrypted:
    f_decrypted.write(decrypted_data)

print(f'Decrypted file saved as: {decrypted_file_p
                                  ath}')
