from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()


def popup():
    MessageBox.showinfo("Sobre mi", "Visita mi GitHub: https://github.com/lordlez")


root = Tk()
root.config(bd=15)
root.title("Descargar Videos")


#seccion de la imagen de la app
imagen = PhotoImage(file="yt_logo.png")
foto = Label(root, image=imagen, bd=9)
foto.grid(row=0, column=0)

#seccion de pestañas de la app
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

#seccion del cuerpo de la app
instrucciones = Label(root, text="Ingresa el link y descarga cualquier video que desees de YouTube")
instrucciones.grid(row=0, column=1)

videos = Entry(root, width=50)
videos.grid(row=1, column=1, pady=10)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()



