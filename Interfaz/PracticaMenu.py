from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root=Tk()
raiz=Tk()

def abreFichero():

    fichero=filedialog.askopenfilename(title= "Abrir", initialdir="c:", filetypes=(("Ficheros de Solidworks","*.stl"),("Ficheros de Solidworks","*.3mf"), ("Ficheros de Solidworks","*.amf"), ("Todos los ficheros","*.*")))
    print(fichero)
    Button (root, text="Abrir archivo", command=abreFichero).pack()

def infoAdicional():
    messagebox.showinfo("Impresora Cat 3D", "licencia")
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo LIcencia")

def salirAplicacion():
    #messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
#archivoMenu.add_separator()

archivoOpciones=Menu(barraMenu, tearoff=0)
archivoOpciones.add_command(label="Explorador de Archivos",command=abreFichero)
archivoOpciones.add_command(label="Impresion Remota")
archivoOpciones.add_command(label="Detener impresion")
archivoOpciones.add_command(label="Salir", command=salirAplicacion)

archivoEstatus=Menu(barraMenu, tearoff=0)
archivoEstatus.add_command(label="Temperatura...")
archivoEstatus.add_command(label="Filamento...")
archivoEstatus.add_command(label="Unidades mm/inch...")
archivoEstatus.add_command(label="Velocidad del Cabezal...")

archivoMonitoreo=Menu(barraMenu, tearoff=0)
archivoMonitoreo.add_command(label="Tiempo Estimado...")
archivoMonitoreo.add_command(label="Imepresion en tiempo real")
archivoMonitoreo.add_command(label="Caras")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Ayuda",command=avisoLicencia)

barraMenu.add_cascade(label="Nuevo", menu=archivoMenu)

barraMenu.add_cascade(label="Opciones", menu=archivoOpciones )

barraMenu.add_cascade(label="Estatus", menu=archivoEstatus)

barraMenu.add_cascade(label="Monitoreo", menu=archivoMonitoreo)

barraMenu.add_cascade(label="Acerca de...", menu=archivoAyuda)

#imagen y titulo
miFrame=Frame(root, width=600, height=500)

miFrame.pack()

miImagen=PhotoImage(file="sla.gif")

Label(miFrame, image=miImagen) .place(x=150, y=100)

miLabel=Label(miFrame, text="Impresora Cat 3D",fg="black", font=(16)).place(x=250, y=50)

#raiz


root.mainloop()
raiz.mainloop()