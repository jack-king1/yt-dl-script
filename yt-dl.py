import sys
import yt_dlp

if len(sys.argv) < 2:
    print("Usage: python ytmp3.py <YouTube_URL>")
    sys.exit(1)

url = sys.argv[1]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',  # Saves file as video title
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # kbps
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
