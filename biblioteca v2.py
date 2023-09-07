import os
import csv

# Definición de la clase Libro
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
    
    def actualizar_csv(self):
    # Abre el archivo CSV en modo escritura (borrando su contenido anterior)
        with open("biblioteca.csv", mode="w", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            for libro in self.libros:
                escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion, libro.estado])
    
    def modificar_libro(self, titulo_libro):
        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                opc = input("¿Qué deseas modificar?\n1. Título\n2. Autor\n3. Género\n4. Año de Publicación\n5. Estado\n0. Cancelar\nIngrese el número de la opción: ")
                if opc == "1":
                    nuevo_titulo = input("Nuevo título: ")
                    libro.titulo = nuevo_titulo
                elif opc == "2":
                    nuevo_autor = input("Nuevo autor: ")
                    libro.autor = nuevo_autor
                elif opc == "3":
                    nuevo_genero = input("Nuevo género: ")
                    libro.genero = nuevo_genero
                elif opc == "4":
                    nuevo_anio = input("Nuevo año de publicación: ")
                    libro.anio_publicacion = nuevo_anio
                elif opc == "5":
                    nuevo_estado = input("Nuevo estado (Disponible/Reservado): ")
                    libro.estado = nuevo_estado
                elif opc == "0":
                    print("Modificación cancelada.")
                    input("Presiona Enter para continuar...")
                    return
                else:
                    print("Opción no válida.")
                    input("Presiona Enter para continuar...")
                    return

                libro_encontrado = libro
                break

        if libro_encontrado is not None:
            print("Registro modificado con éxito!")

            # Ahora, actualiza el archivo CSV con los cambios
            self.actualizar_csv()

            input("Presiona Enter para continuar...")



    def mostrar_libros(self):
        if not self.libros:
            print("\n--------------------------")
            print("\nNO HAY LIBROS REGISTRADOS")
        else:
            print("\n-----------------------------------------")
            print("\nLIBROS REGISTRADOS: ")
            print("\n-----------------------------------------")
            for libro in self.libros:
                print(f"*TITULO: {libro.titulo}")
                print(f"*AUTOR: {libro.autor}")
                print(f"*GENERO: {libro.genero}")
                print(f"*AÑO DE PUBLICACION: {libro.anio_publicacion}")
                print(f"ESTADO: {libro.estado}")
                print("------------------------------------------")

    def buscar_libros(self, criterio_busqueda):
        libros_encontrados = []
        for libro in self.libros:
            if criterio_busqueda.lower() in libro.titulo.lower() or criterio_busqueda.lower() in libro.autor.lower() or criterio_busqueda.lower() in libro.genero.lower():
                libros_encontrados.append(libro)
        
        if not libros_encontrados:
            clear_screen()
            print("NO SE ENCONTRARON LIBROS QUE COINCIDAN CON EL CRITERIO DE BUSQUEDA")
        else:
            clear_screen()
            for libro in libros_encontrados:
                estado = "Disponible" if libro.estado == "Disponible" else "Reservado"
                print(f"*TITULO: {libro.titulo}")
                print(f"*AUTOR: {libro.autor}")
                print(f"*GENERO: {libro.genero}")
                print(f"*AÑO DE PUBLICACION: {libro.anio_publicacion}")
                print(f"ESTADO: {estado}")
                print("---------------------------")
    
    def eliminar_libro(self, titulo_libro):
        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                opc = input("¿Estás seguro de querer eliminar? S/N: ")
                if opc.lower() == "s":
                    libro_encontrado = libro
                    break
                elif opc.lower() == "n":
                    print("No se modificó ningún registro...")
                    input("Presiona Enter para continuar...")
                    return

        if libro_encontrado is not None:
            self.libros.remove(libro_encontrado)
            print("Libro eliminado con éxito!")

            # Ahora, actualiza el archivo CSV eliminando el libro
            self.actualizar_csv()

            input("Presiona Enter para continuar...")

        

    def reservar_libros(self, titulo_libro):
        if not self.libros:
            print("\n--------------------------")
            print("\nNO HAY LIBROS REGISTRADOS AUN")
        else:
            for libro in self.libros:
                if libro.titulo.lower() == titulo_libro.lower():
                    if libro.estado == "Disponible":
                        libro.estado = "Reservado"
                        print("-------------------")
                        print("EL LIBRO SE RESERVO")
                        print("-------------------")
                        break
                    else:
                        clear_screen()
                        print("----------------------------------")
                        print("EL LIBRO YA SE ENCUENTRA RESERVADO")
                        print("----------------------------------")
                        break
            else:
                clear_screen()
                print("-----------------------")
                print("NO SE ENCONTRO UN LIBRO")
                print("-----------------------")

    def cancelar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower():
                if libro.estado == "Reservado":
                    libro.estado = "Disponible"
                    print("------------------")
                    print("EL LIBRO SE LIBERO")
                    print("------------------")
                    break
                elif libro.estado == "Disponible":
                    clear_screen()
                    print("-----------------------------")
                    print("EL LIBRO YA ESTABA DISPONIBLE")
                    print("-----------------------------")
                    break
        else:
            clear_screen()
            print("-----------------------")
            print("NO SE ENCONTRO UN LIBRO")
            print("-----------------------")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

objBiblioteca = Biblioteca()
print("BIENVENIDO A LA BIBLIOTECA")

while True:
    clear_screen()
    print("---------------------------")
    print("\n¿QUÉ DESEAS REALIZAR?")
    print("1. AGREGAR LIBRO")
    print("2. MOSTRAR LIBROS")
    print("3. BUSCAR LIBRO")
    print("4. RESERVAR LIBRO")
    print("5. CANCELAR RESERVACIÓN")
    print("6. Eliminar")
    print("7. Modificar")
    print("0. SALIR")
    
    opc = input("INGRESA EL NÚMERO DE LA OPCIÓN: ")
    
    if opc == "1":
        clear_screen()
        tit = input('INGRESA EL TÍTULO DEL LIBRO: ')
        aut = input("INGRESA EL AUTOR DEL LIBRO: ")
        gen = input("INGRESA EL GÉNERO DEL LIBRO: ")
        ani = input("INGRESA EL AÑO DEL LIBRO: ")
        estado = "Disponible"
        libro = Libro(tit, aut, gen, ani, estado)
        objBiblioteca.agregar_libro(libro)
        input("PRESIONA ENTER PARA VOLVER AL MENÚ...") 
        
    elif opc == "2":
        clear_screen()
        objBiblioteca.mostrar_libros()
        input("PRESIONA ENTER PARA VOLVER AL MENÚ...")
    
    elif opc == "3":
        clear_screen()
        criterio = input("INGRESA EL CRITERIO DE BÚSQUEDA (Título, Autor o Género): ")
        objBiblioteca.buscar_libros(criterio)
        input("PRESIONA ENTER PARA VOLVER AL MENÚ...")

    elif opc == "4":
        clear_screen()
        titulo = input("INGRESA EL TÍTULO DEL LIBRO A RESERVAR: ")
        objBiblioteca.reservar_libros(titulo)
        input("PRESIONA ENTER PARA VOLVER AL MENÚ...")
        
    elif opc == "5":
        clear_screen()
        titulo = input("INGRESA EL TÍTULO DEL LIBRO PARA CANCELAR LA RESERVACIÓN: ")
        objBiblioteca.cancelar_libro(titulo)
        input("PRESIONA ENTER PARA VOLVER AL MENÚ...")
    
    elif opc=="6":
        clear_screen()
        titulo = input("INGRESA EL TÍTULO DEL LIBRO PARA ELIMINAR: ")
        objBiblioteca.eliminar_libro(titulo)
    
    elif opc=="7":
        clear_screen()
        titulo = input("INGRESA EL TÍTULO DEL LIBRO PARA MODIFICAR: ")
        objBiblioteca.modificar_libro(titulo)


    elif opc == "0":
        input("PRESIONA ENTER PARA SALIR...") 
        break
    

