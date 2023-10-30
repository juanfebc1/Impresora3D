from tkinter import*

raiz=Tk()

raiz.title("Ventana de Pruebas")

raiz.resizable(1,0)

raiz.iconbitmap("cat.ico")

#raiz.geometry("650x350")

raiz.config(bd=45)

#raiz.config(relief="groove")

raiz.config(relief="groove")

raiz.config(cursor="watch")

raiz.config(bg="grey")

miFrame=Frame()

#miFrame.pack(fill="Y",expond="true") par alargar el frame en Y
#miFrame.pack(fill="x") para alargar el frame en el eje x
#miFrame.pack(side="side" o left,right) para posicionar el frame a los lados arriba o abajo
#miFrame.pack(side="left", anchor="n") izquierda y norte saldra el recuadro, e=east, w=west, s=south
miFrame.pack()

miFrame.config(bg="black")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

#miFrame.config(relief="groove")

miFrame.config(relief="sunken")

miFrame.config(cursor="hand2")

raiz.mainloop()
