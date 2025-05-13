import os

# Directory where downloads will be saved
DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', '/tmp/downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# List of supported platforms
SUPPORTED_PLATFORMS = [
    'classplus', 'studyiq', 'pw', 'khangs', 'careerwill', 'vision', 'allen'
]

# Example for API credentials (set these in your Render environment variables)
API_ID = os.environ.get('27775431')
API_HASH = os.environ.get('b70bb1d45a1d05236671d4cc615e40f9')
BOT_TOKEN = os.environ.get('7710884267:AAFwceEWEXk62mueTA_QzXcwP4NrO88uMOM')
