class Libro:
    def __init__(self, disponible):
        self.disponible = disponible

class Biblioteca:
    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            print("prestamo confirmado")
        
        else:
            print("libro no disponible")

class Cliente:
    def solicitar_prestamo(self, biblioteca, libro):
        biblioteca.prestar_libro(libro)


libro = Libro(disponible= True)
biblioteca = Biblioteca()
cliente = Cliente()
cliente.solicitar_prestamo(biblioteca, libro)