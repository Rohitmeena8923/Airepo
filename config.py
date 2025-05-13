import os

# Directory where downloads will be saved
DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', '/tmp/downloads')

# List of supported platforms
SUPPORTED_PLATFORMS = [
    'classplus', 'studyiq', 'pw', 'khangs', 'careerwill', 'vision', 'allen'
]
