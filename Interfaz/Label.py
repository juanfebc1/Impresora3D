from tkinter import *

root=Tk()

miFrame=Frame(root, width=600, height=500)

miFrame.pack()

miImagen=PhotoImage(file="sla.gif")

Label(miFrame, image=miImagen) .place(x=150, y=100)

miLabel=Label(miFrame, text="Impresora Cat 3D",fg="black", font=(16)).place(x=250, y=50)
#miLabel.pack()
#miLabel.place(x=250, y=300)
#Label(miFrame, text= "Impresora Cat 3D").place(x=250, y=300)



root.mainloop()