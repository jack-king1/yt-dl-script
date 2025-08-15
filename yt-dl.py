import sys
import yt_dlp
import os

if len(sys.argv) < 2:
    print("Usage: python ytmp3.py <YouTube_URL>")
    sys.exit(1)

url = sys.argv[1]

# Get user's Downloads folder path
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),  # Save to Downloads
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
