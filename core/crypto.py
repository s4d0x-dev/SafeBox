import pyAesCrypt
import io
import os
from .metadata_handler import MetadataHandler


class CryptoEngine:
    BUFFER_SIZE = 64 * 1024

    def encrypt(self, file_in: str, password: str, file_out: str = None) -> str:
        if not file_out:
            file_out = file_in + ".ssb"

        with open(file_in, "rb") as f_in:
            encrypted_stream = io.BytesIO()
            pyAesCrypt.encryptStream(f_in, encrypted_stream, password, self.BUFFER_SIZE)

            original_filename = os.path.basename(file_in)
            encrypted_data_with_metadata = MetadataHandler.attach(encrypted_stream.getvalue(), original_filename)

            with open(file_out, "wb") as f_out:
                f_out.write(encrypted_data_with_metadata)
            
        return f"[+] File Encrypted as {file_out}"

    def decrypt(self, file_in: str, password: str, file_out: str = None) -> str:
        with open(file_in, "rb") as f_in:
            full_data = f_in.read()

        encrypted_part, Original_name = MetadataHandler.detach(full_data)

        output = file_out or Original_name
        encrypted_stream = io.BytesIO(encrypted_part)

        with open(output, "wb") as f_out:
            pyAesCrypt.decryptStream(encrypted_stream, f_out, password, self.BUFFER_SIZE, len(encrypted_part))
        
        return f"[+] Decrypted to {output}"
