import yt_dlp
import os



def downloadMedia():
    url = input("Ingrese una url:\n")
    preference = input("Prefieres mp3 o mp4?\n")

    if preference == "mp4":
        ydl_opts = {}

    if preference == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": preference,
                    "preferredquality": "192",
                }
            
            ],
            "playlist":False,
            "playlist_items":"1"
        }
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if preference == "mp4":
            ydl_opts.update({
                "format": "best[ext=mp4]"
            })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"{preference} descargado exitosamente")
    except Exception as e:
            print(f"Error durante la descarga: {str(e)}")
if __name__ == "__main__":
    downloadMedia()