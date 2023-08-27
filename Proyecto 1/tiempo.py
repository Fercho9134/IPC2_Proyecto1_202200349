from lista_simple import ListaSimple

class Tiempo:
    def __init__(self, tiempo):
        self.tiempo = tiempo
        self.grupo = False
        self.binario = ""
        self.grupo_asociado = None
        self.lista_amplitudes = ListaSimple()
