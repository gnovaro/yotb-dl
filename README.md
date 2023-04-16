# Yotb-dl

Python GUI wrapper for download audio and video

## Requirements
* Python 3
* pip
* ffmpeg (https://ffmpeg.org)
* yt-dlp (https://github.com/yt-dlp/yt-dlp)

## Generate binary
Install pyinstaller
```
pip install pyinstaller
```

Generate the binary
```
pyinstaller --onefile --noconsole yotb-dl.py
```