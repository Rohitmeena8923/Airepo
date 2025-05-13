import os

# Directory where downloads will be saved
DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', '/tmp/downloads')

# Ensure the download directory exists at import time
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# List of supported platforms
SUPPORTED_PLATFORMS = [
    'classplus', 'studyiq', 'pw', 'khangs', 'careerwill', 'vision', 'allen'
]

# Example for API credentials (set these in your Render environment variables)
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
