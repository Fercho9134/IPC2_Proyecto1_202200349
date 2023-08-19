import xml.etree.ElementTree as ET
from senal import Senal
from tiempo import Tiempo
from amplitud import Amplitud

class ProcesarXML:

    def __init__(self, ruta_archivo, lista_senales_general):
        self.ruta_archivo = ruta_archivo
        self.lista_senales_general = lista_senales_general
        try:
            self.arbol = ET.parse(self.ruta_archivo)
            self.raiz = self.arbol.getroot()
        except:
            print("Error al abrir el archivo")
            return
    
    def procesar_archivo(self):
         dato_supera_maximo = False
         
         for senal in self.raiz.findall("senal"):

            nombre = senal.get("nombre")
            tiempo_maximo = int(senal.get("t"))
            amplitud_maxima = int(senal.get("A"))

            senal_actual = self.lista_senales_general.buscar(nombre)

            if senal_actual:
                print(f">La señal {nombre} ya existe, se eliminará la almacenada anteriormente y se sobreescribirá")
                self.lista_senales_general.eliminar(nombre)

            senal_nueva = Senal(nombre, tiempo_maximo, amplitud_maxima)

            self.lista_senales_general.insertar(senal_nueva)

            if tiempo_maximo > 3600 or tiempo_maximo < 1:
                print(f"> Se ecncontraron valores de tiempo que no cumplen con el rango de 1 a 3600 en la señal {nombre} por lo que se omitieron")

            if amplitud_maxima > 130 or amplitud_maxima < 1:
                print(f"> Se ecncontraron valores de amplitud que no cumplen con el rango de 1 a 130 en la señal {nombre} por lo que se omitieron")    

            for i in range(1, min(tiempo_maximo + 1, 3601)):

                tiempo_nuevo = Tiempo(i)
                senal_nueva.lista_tiempos.insertar(tiempo_nuevo)

                for y in range(1, min(amplitud_maxima+1, 131)):


                    existe = False  
                    
                     
                    for dato in senal.findall("dato"):
                        tiempo_dato = int(dato.get("t"))
                        amplitud_dato = int(dato.get("A"))
                        
                        

                        if tiempo_dato == i and amplitud_dato == y:
                            existe = True
                            valor_dato = int(dato.text)
                            amplitud_nueva = Amplitud(amplitud_dato, valor_dato)
                            tiempo_nuevo.lista_amplitudes.insertar(amplitud_nueva)
                            break
                        
                        elif tiempo_dato > tiempo_maximo or amplitud_dato > amplitud_maxima:
                            dato_supera_maximo = True



                    if existe == False:
                        amplitud_nueva = Amplitud(y, 0)
                        tiempo_nuevo.lista_amplitudes.insertar(amplitud_nueva)

        

            if dato_supera_maximo:
                print(f"> Se encontraron datos que superan los valores máximos de tiempo o amplitud en la senal {nombre} por lo que se omitieron")

                            
            print(f"> Se ha procesado la señal {nombre} con éxito")
            

                
