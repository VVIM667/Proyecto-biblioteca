import os  # Importamos la biblioteca 'os' para poder limpiar la pantalla
import csv  # Importamos la biblioteca 'csv' para trabajar con archivos CSV

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista para almacenar los objetos Libro
        self.cargar_csv()  # Llamamos al método para cargar los datos desde el CSV al iniciar

    def agregar_libro(self, libro):
        self.libros.append(libro)  # Agregamos un libro a la lista
        self.guardar_en_csv(libro)  # Guardamos el libro en el archivo CSV
        print("\nLIBRO REGISTRADO CON EXITO.")

    def cargar_csv(self):
        try:
            with open('biblioteca.csv', mode='r', newline='', encoding='utf-8') as file:
                # Abrir el archivo CSV 'biblioteca.csv' en modo de lectura ('r') con la codificación UTF-8.
                # Utilizar la instrucción 'with' para asegurar el cierre adecuado del archivo.
                # 'newline=' se usa para manejar saltos de línea en el archivo CSV.
                # 'as file' asigna el archivo abierto a la variable 'file' para su uso en el bloque 'with'.
                reader = csv.reader(file)
                # Crear un objeto 'reader' utilizando el módulo 'csv' de Python.
                # El objeto 'reader' se utiliza para leer las filas del archivo CSV.
                # Se pasa el archivo 'file' como argumento para que el objeto 'reader' pueda operar sobre él.

                for row in reader:
                    if len(row) == 4: #Lo compara con 4 porque es (titulo,autor,genero y anio)
                        libro = Libro(row[0], row[1], row[2], row[3])
                        self.libros.append(libro)  # Agregamos el libro a la lista de la biblioteca
        except FileNotFoundError:
            pass  # Si el archivo no existe, simplemente continuamos sin cargar nada

    def guardar_en_csv(self, libro):
        with open("biblioteca.csv", mode="a", newline='', encoding='utf-8') as file:
            escribir = csv.writer(file)
            escribir.writerow([libro.titulo, libro.autor, libro.genero, libro.anio_publicacion])

    def mostrar_libros(self):
        if not self.libros:
            print("\n--------------------------")
            print("\nNO HAY LIBROS REGISTRADOS")
        else:
            print("\n--------------------------")
            print("\nLIBROS REGISTRADOS: ")
            print("\n--------------------------")
            for libro in self.libros:
                print(f"*TITULO: {libro.titulo}")
                print(f"*AUTOR: {libro.autor}")
                print(f"*GENERO: {libro.genero}")
                print(f"*AÑO DE PUBLICACION: {libro.anio_publicacion}")
                print("---------------------------")
               

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla de acuerdo al sistema operativo

biblioteca = Biblioteca()
print("BIENVENIDO A LA BIBLIOTECA")

while True:
    clear_screen()
    print("---------------------------")
    print("\n¿QUE DESEAS REALIZAR?")
    print("1. AGREGAR LIBRO")
    print("2. MOSTRAR LIBROS")
    print("3. SALIR")
    
    opc = input("INGRESA EL NUMERO DE LA OPCION: ")
    
    if opc == "1":
        clear_screen()
        tit = input('INGRESA EL TITULO DEL LIBRO: ')
        aut = input("INGRESA EL AUTOR DEL LIBRO: ")
        gen = input("INGRESA EL GENERO DEL LIBRO: ")
        ani = input("INGRESA EL AÑO DEL LIBRO: ")
        libro = Libro(tit, aut, gen, ani)
        biblioteca.agregar_libro(libro)
        input("PRESIONA ENTER PARA VOLVER AL MENU...") 
        
    elif opc == "2":
        clear_screen()
        biblioteca.mostrar_libros()
        input("PRESIONA ENTER PARA VOLVER AL MENU...") 
        
        
    elif opc == "3":
        input("PRESIONA ENTER PARA SALIR...") 
        break
