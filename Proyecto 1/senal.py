from lista_simple import ListaSimple

class Senal:
    def __init__(self, nombre, tiempo_maximo, amplitud_maxima):
        self.nombre = nombre
        self.tiempo_maximo = tiempo_maximo
        self.amplitud_maxima = amplitud_maxima
        self.lista_tiempos = ListaSimple()