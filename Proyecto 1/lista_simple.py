from nodo import Nodo

class ListaSimple:

    def __init__(self):
        self.primero = None
    
    def insertar(self, dato):
        
        if self.primero is None:
            self.primero = Nodo(dato)
            return

        actual = self.primero

        while actual.getSiguiente() != None:
            actual = actual.getSiguiente()
        
        actual.setSiguiente(Nodo(dato))
    

    def eliminar(self, nombre):
        actual = self.primero
        anterior = None

        while actual != None and actual.dato.nombre != nombre:
            anterior = actual
            actual = actual.siguiente
        
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual != None:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
    
    def buscar(self, nombre):
        actual = self.primero

        while actual != None and actual.dato.nombre != nombre:
            actual = actual.siguiente
        
        if actual != None:
            #Se devuelve el objeto Senal
            return actual.dato
        else:
            return None

    def imprimir(self):
        actual = self.primero

        while actual != None:
            print(actual.getDato())
            actual = actual.getSiguiente()

    def getInicio(self):
        return self.primero
    
    def listaVacia(self):
        return self.primero == None
    