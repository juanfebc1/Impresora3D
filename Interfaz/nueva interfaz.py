import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import RPi.GPIO as GPIO
#import time

def abreFichero():
    fichero=filedialog.askopenfilename(title= "Abrir", initialdir="c:", filetypes=(("Ficheros de Solidworks","*.stl",),("Ficheros de Solidworks","*.3mf"), ("Ficheros de Solidworks","*.amf"), ("Todos los ficheros","*.*")))
    print(fichero)

def salirAplicacion():
    #messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo LIcencia")
def popup_menu(e):
    print (e.x_root, e.y_root)
    menu.tk_popup(x=e.x_root, y=e.y_root)

def popup_menu1(e):
    print(e.x_root, e.y_root)
    menu1.tk_popup(x=e.x_root, y=e.y_root)

def popup_menu2(e):
    print(e.x_root, e.y_root)
    menu2.tk_popup(x=e.x_root, y=e.y_root)

def popup_menu3(e):
    print(e.x_root, e.y_root)
    menu3.tk_popup(x=e.x_root, y=e.y_root)

def popup_menu4(e):
    print(e.x_root, e.y_root)
    menu4.tk_popup(x=e.x_root, y=e.y_root)


root=tk.Tk()

#imagen y titulo
root.title("Interfaz Grafica: Impresora 3D")
root.iconbitmap("cat.ico")


miFrame=Frame(root, width=904, height=508)

miFrame.pack()

Fondo=PhotoImage(file="3d.gif")
Fondo1= Label(root, image=Fondo).place(x=0, y=0, relwidth=1, relheight=1)

boton1= Button (root, text= "Opciones", command=root.iconify,bg="white",bd=5, fg="black", activebackground="white", relief= "sunken")
boton1.place(x=30, y=40)

boton2= Button (root, text= "Estatus", command=root.iconify,bg="white", bd=5, fg="black", activebackground="white", relief= "sunken")
boton2.place(x=30, y=90)

boton3= Button (root, text= "Monitoreo", command=root.iconify, bg="white", bd=5, fg="black", activebackground="white", relief= "sunken")
boton3.place(x=30, y=140)

boton4= Button (root, text= "Ajustes", command=root.iconify,bg="white", bd=5, fg="black", activebackground="white", relief= "sunken")
boton4.place(x=30, y=190)

boton5= Button (root, text= "Acerca de...", command=root.iconify,bg="white", bd=5, fg="black", activebackground="white", relief= "sunken")
boton5.place(x=30, y=240)




menu = tk.Menu(root, tearoff=0)

menu.add_command(label="Explorador de Archivos",command=abreFichero)
menu.add_command(label="Impresion Remota")
menu.add_command(label="Detener impresion")
menu.add_separator()
menu.add_command(label="Salir", command=salirAplicacion)

boton1.bind("<Button-1>", popup_menu)

menu1 = tk.Menu(root, tearoff=0)

menu1.add_command(label="Calentar Extrusora")
menu1.add_command(label="Test de Ventilador")
menu1.add_command (label="Retirar Material")
menu1.add_command (label="Cargar Material")
menu1.add_command (label="Calentamiento de la Extrusora...")

boton2.bind("<Button-1>", popup_menu1)

menu2 = tk.Menu(root,tearoff=0)

menu2.add_command(label="Tiempo Estimado...")
menu2.add_command(label="Imepresion en tiempo real")
menu2.add_command(label="Caras")

boton3.bind("<Button-1>", popup_menu2)

menu3 = tk.Menu(root, tearoff=0)

menu3.add_command (label="Iluminacion Dinamica")
menu3.add_command (label="Luz Blanca")
menu3.add_command (label="Apagar")

boton4.bind("<Button-1>", popup_menu3)

menu4 = tk.Menu(root, tearoff=0)

menu4.add_command(label="Ayuda",command=avisoLicencia)
menu4.add_command(label="Firmware")
menu4.add_command(label="Informacion de Impresora")

boton5.bind("<Button-1>", popup_menu4)

root.mainloop()