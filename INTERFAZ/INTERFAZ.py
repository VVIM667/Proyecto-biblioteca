import tkinter as tk
from tkinter import *
import os
import csv


#COLORES
fondo_agregar="#e9d9d9"

ventana = Tk()
ventana.title("Biblioteca")
ventana.geometry("800x800+800+80")
ventana.resizable(width=False, height = False)
fondo = tk.PhotoImage(file="Fondo.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)



#VENTANAS

def Addbook():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("Agregar")
    window.geometry("800x800+800+80")
    window.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="Addb.png")
    fondo1 = tk.Label(window,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window.mainloop()

def showbk():
    ventana.withdraw()
    window1 = tk.Toplevel()
    window1.title("Agregar")
    window1.geometry("800x800+800+80")
    window1.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="showb.png")
    fondo1 = tk.Label(window1,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window1.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window1,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window1.mainloop()

def searchb():
    ventana.withdraw()
    window2 = tk.Toplevel()
    window2.title("Agregar")
    window2.geometry("800x800+800+80")
    window2.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="srch.png")
    fondo1 = tk.Label(window2,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window2.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window2,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window2.mainloop()

def reservb():
    ventana.withdraw()
    window2 = tk.Toplevel()
    window2.title("Agregar")
    window2.geometry("800x800+800+80")
    window2.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="reser.png")
    fondo1 = tk.Label(window2,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window2.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window2,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window2.mainloop()

def cancelb():
    ventana.withdraw()
    window2 = tk.Toplevel()
    window2.title("Agregar")
    window2.geometry("800x800+800+80")
    window2.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="cancel.png")
    fondo1 = tk.Label(window2,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window2.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window2,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window2.mainloop()

def deleteb():
    ventana.withdraw()
    window2 = tk.Toplevel()
    window2.title("Agregar")
    window2.geometry("800x800+800+80")
    window2.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="delet.png")
    fondo1 = tk.Label(window2,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window2.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window2,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window2.mainloop()

def modifyb():
    ventana.withdraw()
    window2 = tk.Toplevel()
    window2.title("Agregar")
    window2.geometry("800x800+800+80")
    window2.resizable(width=False, height = False)
    fondo = tk.PhotoImage(file="mod.png")
    fondo1 = tk.Label(window2,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
    

    def regreso():
        window2.withdraw()
        ventana.deiconify()

    btnre = tk.Button(window2,text="Regresar",relief="flat",command=regreso, bg=fondo_agregar,font=("Comic Sans MS", 12, "bold"))
    btnre.place(x=350,y=600)
    window2.mainloop()







Boton1 = tk.Button(ventana, text="Agregar libro",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=Addbook)
Boton1.place(x=350, y=200)
Boton2 = tk.Button(ventana, text="Mostrar Libro",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=showbk)
Boton2.place(x=350, y=250)
Boton3 = tk.Button(ventana, text="Buscar Libro",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=searchb)
Boton3.place(x=350, y=300)
Boton4 = tk.Button(ventana, text="Reservar Libro",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=reservb)
Boton4.place(x=350, y=350)
Boton5 = tk.Button(ventana, text="Cancelar reservacion",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=cancelb)
Boton5.place(x=350, y=400)
Boton6 = tk.Button(ventana, text="Eliminar",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=deleteb)
Boton6.place(x=350, y=450)
Boton7 = tk.Button(ventana, text="Modificar",relief="flat",bg=fondo_agregar, font=("Comic Sans MS", 12, "bold"),command=modifyb)
Boton7.place(x=350, y=500)



ventana.mainloop()