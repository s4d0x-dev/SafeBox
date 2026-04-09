import base64
from typing import Tuple

class MetadataHandler:
    METADATA_FLAG = b'\n==b-ssb_metadata=['

    @staticmethod
    def attach(file_stream: bytes, file_name: str) -> bytes:
        encoded_name = base64.b64encode(file_name.encode("utf-8")).decode("ascii")
        metadata = f'\n==b-ssb_metadata=[{encoded_name}]'.encode("utf-8")
        return file_stream + metadata

    @staticmethod
    def detach(file_in: bytes) -> Tuple[bytes, str]:
        if MetadataHandler.METADATA_FLAG not in file_in:
            raise ValueError("Safebox metadata not found in the file.")
        
        encrypted_data, meta_part = file_in.split(MetadataHandler.METADATA_FLAG, 1)
        ending_index = meta_part.find(b']')

        original_file_name_encoded_bytes = meta_part[:ending_index]
        original_filename = base64.b64decode(original_file_name_encoded_bytes).decode("utf-8")

        return encrypted_data, original_filename

