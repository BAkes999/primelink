import os
import base64
from cryptography.fernet import Fernet

class PrimeLink:
    def __init__(self, key_file='key.key'):
        self.key_file = key_file
        self.key = self.load_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as keyfile:
            keyfile.write(key)
        return key

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as keyfile:
                key = keyfile.read()
        else:
            key = self.generate_key()
        return key

    def encrypt(self, data):
        encoded_data = data.encode()
        encrypted_data = self.cipher.encrypt(encoded_data)
        return base64.urlsafe_b64encode(encrypted_data).decode()

    def decrypt(self, encrypted_data):
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_data)
            decrypted_data = self.cipher.decrypt(decoded_data)
            return decrypted_data.decode()
        except Exception as e:
            return f"Decryption failed: {str(e)}"

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return f"File {file_path} encrypted successfully."

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
            return f"File {file_path} decrypted successfully."
        except Exception as e:
            return f"File decryption failed: {str(e)}"

# Example usage:
# prime_link = PrimeLink()
# encrypted_text = prime_link.encrypt("Sensitive information")
# print(encrypted_text)
# decrypted_text = prime_link.decrypt(encrypted_text)
# print(decrypted_text)

# prime_link.encrypt_file('sensitive_file.txt')
# prime_link.decrypt_file('sensitive_file.txt')