import yt_dlp
import os

def main():
        url = input("Ingrese una url:\n")
        preference = input("Prefieres mp3 o mp4?\n")
        rute_option = input(f"La ruta por defecto es {os.getcwd()}, ¿Desea cambiarla? y/n \n")
        if rute_option == 'y':
            rute = input("Introduce la nueva ruta: ").strip()
        if rute_option == 'n':
            rute = os.getcwd()

        if preference == "mp3":
            ydl_opts = {
                "format": "bestaudio/best",
               "outtmpl": f"{rute}/%(title)s.%(ext)s",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": preference,
                        "preferredquality": "192",
                    }
                ],
                "playlist": False,
                "playlist_items": "1",
            }
        if preference == "mp4":
            ydl_opts.update({"format": "best[ext=mp4]"})
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"{preference} descargado exitosamente")
        except Exception as e:
            print(f"Error durante la descarga: {str(e)}")
if __name__ == "__main__":
    main()
