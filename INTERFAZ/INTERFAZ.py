import tkinter as tk
from tkinter import *
import csv
from tkinter import messagebox, ttk

#CLASE LIBRO
class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.estado = estado

# Definición de la clase Biblioteca
class Biblioteca: 
    def __init__(self):
        self.libros = []
        self.cargar_csv()

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_en_csv(libro)
        print("\nLibro registrado con éxito.")

    def cargar_csv(self):
        try:
            with open('biblioteca.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 5:
                        libro = Libro(row[0], row[1], row[2], row[3], row[4])
                        self.libros.append(libro)
        except FileNotFoundError:
            pass

    def guardar_en_csv(self, libro):
        with open("biblioteca.csv", mode="a", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion, libro.estado])

    def reservar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                if libro.estado == "Disponible":
                    libro.estado = "Reservado"
                    self.actualizar_csv()
                    print(f"Libro '{libro.titulo}' reservado con éxito.")
                    return
        print(f"El libro '{titulo_libro}' no se encuentra disponible para reserva.")

    def actualizar_csv(self):
        with open("biblioteca.csv", mode="w", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            for libro in self.libros:
                escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion, libro.estado])

    def buscar_libros(self, criterio_busqueda):
        libros_encontrados = []
        for libro in self.libros:
            if criterio_busqueda.lower() in libro.titulo.lower() or criterio_busqueda.lower() in libro.autor.lower() or criterio_busqueda.lower() in libro.genero.lower():
                libros_encontrados.append(libro)

        if not libros_encontrados:
            messagebox.showinfo("Búsqueda sin Resultados", "No se encontraron libros que coincidan con el criterio de búsqueda.")
        
        else:

            ventana_resultados = tk.Toplevel()
            ventana_resultados.title("Resultados de Búsqueda")

        for libro in libros_encontrados:
            estado = "Disponible" if libro.estado == "Disponible" else "Reservado"

            etiqueta_titulo = tk.Label(ventana_resultados, text=f"Título: {libro.titulo}")
            etiqueta_titulo.pack()

            etiqueta_autor = tk.Label(ventana_resultados, text=f"Autor: {libro.autor}")
            etiqueta_autor.pack()

            etiqueta_genero = tk.Label(ventana_resultados, text=f"Género: {libro.genero}")
            etiqueta_genero.pack()

            etiqueta_anio = tk.Label(ventana_resultados, text=f"Año de Publicación: {libro.anio_publicacion}")
            etiqueta_anio.pack()

            etiqueta_estado = tk.Label(ventana_resultados, text=f"Estado: {estado}")
            etiqueta_estado.pack()

            separador = ttk.Separator(ventana_resultados, orient="horizontal")
            separador.pack(fill="x", padx=10, pady=5) 

    def cancelar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                if libro.estado == "Reservado":
                    libro.estado = "Disponible"
                    self.actualizar_csv()
                    print(f"Libro '{libro.titulo}' Cancelado con éxito.")
                    return
        print(f"El libro '{titulo_libro}' esta disponible.")

    
    def eliminar_libro(self, titulo_libro):

        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                opc = messagebox.askquestion("Eliminar Libro", "¿Estás seguro de querer eliminar este libro?", icon='warning')
                if opc == "yes":
                    libro_encontrado = libro
                    break
                elif opc == "no":
                    messagebox.showinfo("Eliminación Cancelada", "No se modificó ningún registro.")
                    return

        if libro_encontrado is not None:
            self.libros.remove(libro_encontrado)
            messagebox.showinfo("Libro Eliminado", "El libro ha sido eliminado con éxito.")
            self.actualizar_csv()
        
                
                    
             
           
    

# Crea una instancia de la biblioteca
biblioteca = Biblioteca()
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

    def escribir_datos():
      
    # Obtén los datos ingresados por el usuario
         titulo = entry_titulo.get()
         autor = entry_autor.get()
         genero = entry_genero.get()
         anio_publicacion = entry_anio.get()
         estado = "Disponible"

    # Crea una instancia de la clase Libro
         nuevo_libro = Libro(titulo, autor, genero, anio_publicacion, estado)

    # Agrega el libro a la biblioteca y escribe los datos en el archivo CSV
         biblioteca.agregar_libro(nuevo_libro)

    # Limpia los campos de entrada después de escribir los datos
         entry_titulo.delete(0, 'end')
         entry_autor.delete(0, 'end')
         entry_genero.delete(0, 'end')
         entry_anio.delete(0, 'end')
         

    etiqueta_titulo = tk.Label(window, text="Título:")
    etiqueta_titulo.place(x=350,y=200)
    entry_titulo = tk.Entry(window)
    entry_titulo.place(x=350,y=220)

    etiqueta_autor = tk.Label(window, text="Autor:")
    etiqueta_autor.place(x=350,y=250)
    entry_autor = tk.Entry(window)
    entry_autor.place(x=350,y=270)

    etiqueta_genero = tk.Label(window, text="Género:")
    etiqueta_genero.place(x=350,y=300)
    entry_genero = tk.Entry(window)
    entry_genero.place(x=350,y=320)

    etiqueta_anio = tk.Label(window, text="Año de Publicación:")
    etiqueta_anio.place(x=350,y=350)
    entry_anio = tk.Entry(window)
    entry_anio.place(x=350,y=370)

    boton_escribir = tk.Button(window,text="Guardar datos", command=escribir_datos)
    boton_escribir.place(x=350,y=410)



    
    

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


    lst = []
    for libro in biblioteca.libros:
        titulo = libro.titulo
        autor = libro.autor
        genero = libro.genero
        anio = libro.anio_publicacion
        estado = libro.estado

        tupla = (titulo,autor,genero,anio,estado)
        lst.append(tupla)

  
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
  
    # create root window
    
    for i in range(total_rows):
            for j in range(total_columns):
                 
                e = Entry(window1, width=16, fg='black',
                               font=('Arial',11,'bold'))
                 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])

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

    def buscar():
        criterio_busqueda = entry_buscar.get().strip()
        biblioteca.buscar_libros(criterio_busqueda)

    etiqueta_busqueda = tk.Label(window2,text="Busqueda por Libro,Autor")
    etiqueta_busqueda.place(x=350,y=200)
    entry_buscar = tk.Entry(window2)
    entry_buscar.place(x=350,y=230)

    boton_buscar = tk.Button(window2,text="Buscar",command=buscar)
    boton_buscar.place(x=350, y=260)

    


    

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

    def reservar():

        titulo_libro = entry_reservar.get()
        biblioteca.reservar_libro(titulo_libro)

        entry_reservar.delete(0, 'end')
    
    etiqueta_reservar = tk.Label(window2,text="Titulo del Libro a reservar")
    etiqueta_reservar.place(x=350,y=200)
    entry_reservar = tk.Entry(window2)
    entry_reservar.place(x=350,y=230)

    boton_reservar = tk.Button(window2,text="Reservar Libro",command=reservar)
    boton_reservar.place(x=350, y=260)

    
    


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

    def cancelar():

        titulo_libro = entry_cancelar.get()
        biblioteca.cancelar_libro(titulo_libro)

        entry_cancelar.delete(0, 'end')
    
    etiqueta_cancelar = tk.Label(window2,text="Titulo del Libro a cancelar")
    etiqueta_cancelar.place(x=350,y=200)
    entry_cancelar = tk.Entry(window2)
    entry_cancelar.place(x=350,y=230)

    boton_reservar = tk.Button(window2,text="Cancelar Libro",command=cancelar)
    boton_reservar.place(x=350, y=260)
    

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


    def eliminar():
        
        titulo_libro = entry_delete.get()
        biblioteca.eliminar_libro(titulo_libro)
        
        entry_delete.delete(0,'end')

    etiqueta_eliminar = tk.Label(window2,text="Titulo a eliminar")
    etiqueta_eliminar.place(x=350,y=200)
    entry_delete = tk.Entry(window2)
    entry_delete.place(x=350,y=230)

    boton_eliminar = tk.Button(window2, text="Eliminar", command=eliminar)
    boton_eliminar.place(x=350,y=260)
    

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
