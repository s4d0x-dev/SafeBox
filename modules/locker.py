import pyAesCrypt

def encryptor(file_in, password, file_out):
    buffer_size = 64 * 1024  # 64KB buffer
    print(f"Encrypting '{file_in}' to '{file_out}'...")
    try:
        pyAesCrypt.encryptFile(file_in, file_out, password, buffer_size)
        print("Encryption complete!")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decryptor(file_in, password, file_out):
    buffer_size = 64 * 1024  # 64KB buffer
    print(f"Decrypting '{file_in}' to '{file_out}'...")
    try:
        pyAesCrypt.decryptFile(file_in, file_out, password, buffer_size)
        print("Decryption complete!")
    except Exception as e:
        print(f"Decryption failed: {e}")
