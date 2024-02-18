import base64
import io
import hashlib

#this may not be needed
def calculate_md5_for_base64(base64_content):
    # Decode the Base64 content into bytes
    binary_content = base64.b64decode(base64_content)
    md5_hash = hashlib.md5()
    md5_hash.update(binary_content)
    return md5_hash.hexdigest()


def rebuild_file_from_base64(base64_string, filename):
    try:
        file_bytes = base64.b64decode(base64_string)
        file_io = io.BytesIO(file_bytes)
        file_info = {"file": (filename, file_io, "application/octet-stream")}
        return file_info
    except Exception as e:
        print(f"Error rebuilding file from base64: {e}")
        return None