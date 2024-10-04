class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f'{self.titulo} de {self.autor}, publicado en {self.año}'

class Biblioteca:
    def __init__(self):
        self.libros = [
            Libro('Don Quijote', 'Miguel de Cervantes', 1605),
            Libro('La Odisea', 'Homero', 1800),
            Libro('El Señor de los Anillos', 'J.R.R. Tolkien', 1954)
        ]

    def imprimir_biblioteca(self):
        for libro in self.libros:
            print(libro)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def añadir_libro(self, titulo, autor, año):
        self.libros.append(Libro(titulo, autor, año))

    def eliminar_libro(self, autor):
        self.libros = [libro for libro in self.libros if libro.autor != autor]

def main():
    biblioteca = Biblioteca()
    while True:
        print('\nMenú de la biblioteca:')
        print('1. Imprimir biblioteca')
        print('2. Buscar libro por título')
        print('3. Añadir libro')
        print('4. Eliminar libro')
        print('5. Salir')
        opción = input('Ingrese su opción: ')
        if opción == '1':
            biblioteca.imprimir_biblioteca()
        elif opción == '2':
            título = input('Ingrese el título del libro: ')
            libro = biblioteca.buscar_libro_por_titulo(título)
            if libro:
                print(libro)
            else:
                print('Libro no encontrado')
        elif opción == '3':
            título = input('Ingrese el título del libro: ')
            autor = input('Ingrese el autor del libro: ')
            año = int(input('Ingrese el año de publicación del libro: '))
            biblioteca.añadir_libro(título, autor, año)
        elif opción == '4':
            autor = input('Ingrese el autor del libro a eliminar: ')
            biblioteca.eliminar_libro(autor)
        elif opción == '5':
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    main()
