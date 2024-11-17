import tkinter as tk
from pytube import YouTube
import customtkinter
import os

def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_by_itag(137)
        elif option == "lq":
            video = ytObject.streams.get_by_itag(22)
        elif option == "audio":
            video = ytObject.streams.get_by_itag(140)
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download('C:\Youtube_downloader')
        finishLabel.configure(text="Downloaded !!", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perecentage_of_completion = bytes_download / total_size * 100
    per = str(int(perecentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()


    progressbar.set(float(perecentage_of_completion) / 100)


newpath = r'C:\Youtube_downloader'
if not os.path.exists(newpath):
    os.makedirs(newpath)


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")



app = customtkinter.CTk()
app.geometry("720x480")
app.title("YoutubeLink downloader")





title = customtkinter.CTkLabel(app, text="Insert a YouTube Link", width=200, height=50, font=("cursive", 26))
title.pack(padx=10, pady=10)

#

link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()


progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)



download_hq = customtkinter.CTkButton(app, text="Download High Quality-Mp4", command=lambda: startDownload("hq"))
download_hq.pack(padx=10, pady=10)


download_lq = customtkinter.CTkButton(app, text="Download Low Quality-Mp4", command=lambda: startDownload("lq"))
download_lq.pack(padx=10, pady=10)


download_a = customtkinter.CTkButton(app, text="Download Mp3", command=lambda: startDownload("audio"))
download_a.pack(padx=10, pady=10)



app.mainloop()
