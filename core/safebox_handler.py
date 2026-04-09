from .crypto import CryptoEngine

class SafeBox:
    def __init__(self):
        self.crypto = CryptoEngine()

    def encrypt_file(self, file_path: str, password: str, output: str = None):
        return self.crypto.encrypt(file_in=file_path, password=password, file_out=output)
    
    def decrypt_file(self, file_path: str, password: str, output: str = None):
        return self.crypto.decrypt(file_in=file_path, password=password, file_out=output)