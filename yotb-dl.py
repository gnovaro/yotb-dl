"""
Yotb-dl
 GUI
"""
import os
import subprocess
import tkinter as tk


def download_video(url):
    # Obtener el nombre del archivo de video
    file_name_command = "yt-dlp --get-filename -o '%(title)s.%(ext)s' " + url
    print(file_name_command)
    file_name = subprocess.getoutput(file_name_command)

    # Descargar el video en formato mp4
    command = "yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' " + url
    os.system(command)

    # Cambiar el nombre del archivo a formato mp4
    file_name_destination = file_name.replace('.webm', '.mp4').replace('.mkv', '.mp4').replace('.mp4', '.mp4')

    # Renombrar el archivo descargado a formato mp4
    os.rename(file_name, file_name_destination)

    # Imprimir el nombre del archivo y la ruta de acceso
    print('Archivo guardado como:', file_name_destination)


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
    download_label.config(text="Descarga completada: " + file_name_destination)
    window.update()


def on_click():
    url = url_entry.get()
    download_audio(url)

# Crear la ventana principal
window = tk.Tk()
window.title("Descargar audio de YouTube")

# Crear un marco para el cuadro de texto y el botón
frame = tk.Frame(window)

# Crear un cuadro de texto para pegar la URL
url_entry = tk.Entry(frame, width=50)
url_entry.pack(side=tk.LEFT)

# Crear un botón para iniciar la descarga
download_button = tk.Button(frame, text="Descargar", command=on_click)
download_button.pack(side=tk.LEFT)


download_label = tk.Label(window, text="")
download_label.pack()

# Alinear el marco en el centro de la ventana
frame.pack(pady=10)

# Iniciar el bucle principal de la GUI
window.mainloop()
