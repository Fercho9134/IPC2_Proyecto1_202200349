class Nodo:
    
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
    
    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente