import os
from config import DOWNLOAD_DIR, SUPPORTED_PLATFORMS

def download_content(url, platform):
    # Dummy implementation for demonstration.
    # Replace this with actual download logic per platform.
    if platform not in SUPPORTED_PLATFORMS:
        raise ValueError(f"Platform '{platform}' not supported.")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, 'dummy.txt')
    with open(file_path, 'w') as f:
        f.write(f"Downloaded from {url} on platform {platform}")
    return file_path
