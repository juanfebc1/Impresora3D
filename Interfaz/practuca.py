from tkinter import *
root=Tk()


barraMenu=Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

root.mainloop ()