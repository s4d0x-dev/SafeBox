# import base64 - for the next update
from typing import Tuple

def attach_metadata(file_stream: bytes, file_name: str) -> bytes:
    """
    Append metadata with the original filename to encrypted binary data.
    """
    metadata = f'\n==b-ssb_metadata="{file_name}"'.encode("utf-8")
    return file_stream + metadata

def extract_metadata(file_in: bytes) -> Tuple[bytes, str]:
    """
    Splits encrypted data and metadata from input file(encrypted) data. 
    """
    metadata = b'\n==b-ssb_metadata="'
    if metadata not in file_in:
        raise ValueError("The SafeBox metadata not found in the file.")
    
    encrypted_data, meta_part = file_in.split(metadata, 1)
    original_filename = meta_part.decode(errors="ignore").split('"', 1)[0].strip()
    return encrypted_data, original_filename
