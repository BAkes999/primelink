# PrimeLink

PrimeLink is a Python program designed to protect sensitive information on Windows systems through advanced data encryption and security measures. It provides functionalities to encrypt and decrypt strings and files, ensuring the confidentiality of sensitive data.

## Features

- **String Encryption and Decryption**: Encrypt and decrypt strings with ease.
- **File Encryption and Decryption**: Secure your files by encrypting them and decrypt when needed.
- **Key Management**: Automatically generate and store encryption keys for secure operations.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone the repository or download the `PrimeLink.py` file.
2. Ensure you have the `cryptography` library installed. You can install it using pip:
   ```bash
   pip install cryptography
   ```

## Usage

1. Import the `PrimeLink` class from the `PrimeLink.py` file.

2. Create an instance of `PrimeLink`:
   ```python
   prime_link = PrimeLink()
   ```

3. Encrypt a string:
   ```python
   encrypted_text = prime_link.encrypt("Sensitive information")
   print(encrypted_text)
   ```

4. Decrypt a string:
   ```python
   decrypted_text = prime_link.decrypt(encrypted_text)
   print(decrypted_text)
   ```

5. Encrypt a file:
   ```python
   prime_link.encrypt_file('sensitive_file.txt')
   ```

6. Decrypt a file:
   ```python
   prime_link.decrypt_file('sensitive_file.txt')
   ```

## Security

PrimeLink uses the `cryptography` library to provide strong encryption using Fernet symmetric encryption. The encryption key is stored in a file named `key.key`, which should be kept secure.

## License

This project is licensed under the MIT License.