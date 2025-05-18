import base64
from typing import Tuple

def attach_metadata(file_stream: bytes, file_name: str) -> bytes:
    """
    Append metadata with the original filename to encrypted binary data.
    """
    encoded_name = base64.b64encode(file_name.encode("utf-8")).decode("ascii")
    metadata = f'\n==b-ssb_metadata=[{encoded_name}]'.encode("utf-8")
    return file_stream + metadata

def extract_metadata(file_in: bytes) -> Tuple[bytes, str]:
    """
    Splits encrypted data and metadata from input file (encrypted) data. 
    """
    metadata = b'\n==b-ssb_metadata=['
    if metadata not in file_in:
        raise ValueError("The SafeBox metadata not found in the file.")
    
    encrypted_data, meta_part = file_in.split(metadata, 1)
    end_index = meta_part.find(b']')
    original_filename_encoded_bytes = meta_part[:end_index]
    original_filename = base64.b64decode(original_filename_encoded_bytes).decode("utf-8")
    
    return encrypted_data, original_filename
