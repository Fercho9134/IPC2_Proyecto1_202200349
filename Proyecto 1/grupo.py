from lista_simple import ListaSimple

class Grupo:

    def __init__(self, numero):
        self.nombre = "Grupo " + str(numero)
        self.tiempos = ""
        self.lista_amplitudes = ListaSimple()