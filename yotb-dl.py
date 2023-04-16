"""
Yotb-dl
 GUI
"""
import os
import subprocess
import tkinter as tk

VERSION = "1.1.0"


def download_video(url):
    # Get file name from video
    file_name_command = "yt-dlp --get-filename " + url
    print(file_name_command)
    file_name = subprocess.getoutput(file_name_command)

    # Descargar el video en formato mp4
    command = "yt-dlp " + url + " -f 22"
    os.system(command)

    return file_name


def download_audio(url):
    file_name_command = "yt-dlp  -f 140 --get-filename " + url
    print(file_name_command)
    file_name = subprocess.getoutput(file_name_command)

    command = "yt-dlp " + url + " -f 140"
    os.system(command)

    file_name_destination = file_name.replace('.m4a', '.mp3')

    command_convert = "ffmpeg -i " + '"' + file_name + '"' + " -f mp3 " + '"' + file_name_destination + '"'
    print(command_convert)
    os.system(command_convert)

    os.remove(file_name)
    # Actualizar la etiqueta de texto de descarga completada
    return file_name_destination


def download_media(url, media_type):
    if media_type == 'audio':
        return download_audio(url)
    else:
        return download_video(url)


def download():
    url = url_entry.get()
    media_type = media_type_var.get()

    file_name_destination = download_media(url, media_type)

    result_label.config(text=f"{file_name_destination} downloaded successfully")


# Main window
window = tk.Tk()
window.title("Download audio/video from YouTube " + VERSION)

# Main frame
main_frame = tk.Frame(window, padx=10, pady=10)

# Text box for video URL
url_label = tk.Label(main_frame, text="Youtube URL:")
url_label.pack()

url_entry = tk.Entry(main_frame, width=80)
url_entry.pack()

# Crear menú desplegable para elegir el tipo de medio a descargar
media_type_var = tk.StringVar()
media_type_var.set('audio')  # Valor predeterminado del menú desplegable
media_type_label = tk.Label(main_frame, text="Tipo de medio:")
media_type_label.pack()
media_type_dropdown = tk.OptionMenu(main_frame, media_type_var, 'audio', 'video')
media_type_dropdown.pack()

# Crear un botón para iniciar la descarga
download_button = tk.Button(main_frame, text="Download", command=download)
download_button.pack(side=tk.LEFT)

# Label for download complete message
result_label = tk.Label(window, text="")
result_label.pack()

# Alinear el marco en el centro de la ventana
main_frame.pack(pady=10)

# Iniciar el bucle principal de la GUI
window.mainloop()
