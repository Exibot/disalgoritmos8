def main():
    pass
    class Libro: #Esto es un nodo del arbol
        def __init__(self, id=None, titulo=None, autor=None, anio=None, izq=None, der=None):
            self.id = id
            self.titulo = titulo
            self.autor = autor
            self.anio = anio
            self.izq = izq #Nodo a la izquierda
            self.der = der #Nodo a la derecha
        
        def insertar(self, id, titulo, autor, anio):
            self.id = id
            self.titulo = titulo
            self.autor = autor
            self.anio = anio
            
    class BusquedaBinaria:
        def __init__(self, datos):
            self.raiz = Libro(datos)
        
        def recursivo(self, libro, datos):
            if id < libro:
                if libro.izq is None:
                    libro.izq = Libro(datos)
                else:
                    self.recursivo(libro.izq, datos)
            else:
                if libro.der is None:
                    libro.der = Libro(datos)
                else:
                    self.recursivo(libro.der, datos)


if __name__ == '__main__':
    main()