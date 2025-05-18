import pyAesCrypt
from .meta_process import attach_metadata, extract_metadata
import io
import os

BUFFER_SIZE = 64 * 1024

def encryptor(file_in, password, file_out=None):
    if not file_out:
        file_out = file_in + ".ssb"
    
    with open(file_in, "rb") as f_in:
        encrypted_stream = io.BytesIO()
        pyAesCrypt.encryptStream(f_in, encrypted_stream, password, BUFFER_SIZE)

        original_filename = os.path.basename(file_in)
        enc_data_with_meta = attach_metadata(encrypted_stream.getvalue(), original_filename)

        with open(file_out, "wb") as f_out:
            f_out.write(enc_data_with_meta)
    print(f"[+] File Encrypted as: {file_out}")


def decryptor(file_in, password, file_out=None):
    with open(file_in, "rb") as f_in:
        full_data = f_in.read()

    try:
        enc_part, original_name = extract_metadata(full_data)
    except ValueError as e:
        print(f"[-] Wrong Encrypted Data.", e)
        return
    output = file_out or original_name

    encrypted_stream = io.BytesIO(enc_part)
    with open(output, "wb") as f_out:
        try:
            pyAesCrypt.decryptStream(encrypted_stream, f_out, password, BUFFER_SIZE ,len(enc_part))
            print(f"[+] Decrypted to: {output}")
        except ValueError:
            f_out.close()
            # os.remove(output)
            print(f"[-] Incorrect Password or curropted file.")
        
