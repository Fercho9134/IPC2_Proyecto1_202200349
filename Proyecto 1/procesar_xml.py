import xml.etree.ElementTree as ET
from senal import Senal
from tiempo import Tiempo
from amplitud import Amplitud
from grupo import Grupo

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

            print(f"> Generando la matriz de frecuencias de la senal {nombre}...")

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
                tiempo_nuevo_patrones = Tiempo(i)
                senal_nueva.lista_tiempos.insertar(tiempo_nuevo)
                senal_nueva.matriz_patrones_tiempos.insertar(tiempo_nuevo_patrones)

                for y in range(1, min(amplitud_maxima+1, 131)):


                    existe = False  
                    
                     
                    for dato in senal.findall("dato"):

                        tiempo_dato = int(dato.get("t"))
                        amplitud_dato = int(dato.get("A"))
                        
                        if tiempo_dato == i and amplitud_dato == y:
                            existe = True
                            valor_dato = int(dato.text)
                            amplitud_nueva = Amplitud(amplitud_dato, valor_dato)

                            if valor_dato == 0:
                                tiempo_nuevo.binario += "0"
                                amplitud_nueva_patrones = Amplitud(amplitud_dato, 0)
                            else:
                                tiempo_nuevo.binario += "1"
                                amplitud_nueva_patrones = Amplitud(amplitud_dato, 1)

                            tiempo_nuevo.lista_amplitudes.insertar(amplitud_nueva)
                            tiempo_nuevo_patrones.lista_amplitudes.insertar(amplitud_nueva_patrones)
                            break
                        
                        elif tiempo_dato > tiempo_maximo or amplitud_dato > amplitud_maxima:
                            dato_supera_maximo = True



                    if existe == False:
                        amplitud_nueva = Amplitud(y, 0)
                        tiempo_nuevo.lista_amplitudes.insertar(amplitud_nueva)
                        tiempo_nuevo.binario += "0"
                        amplitud_nueva_patrones = Amplitud(y, 0)
                        tiempo_nuevo_patrones.lista_amplitudes.insertar(amplitud_nueva_patrones)

        

            if dato_supera_maximo:
                print(f"> Se encontraron datos que superan los valores máximos de tiempo o amplitud en la senal {nombre} por lo que se omitieron")

            print(f"> Generando la matriz de patrones de la senal {nombre}...")                
            print(f"> Se ha procesado la señal {nombre} con éxito")
    

    def crear_matriz_reducida(self):
        if self.lista_senales_general.listaVacia():
            print("\nNo hay señales almacenadas...")
            print("Volviendo al menú inicial...\n")
            return
        
        senal_actual = self.lista_senales_general.getInicio()

        #Creando grupos
        while senal_actual != None:
            print("> Creando grupos de la senal", senal_actual.getDato().nombre, "...")
            numero_grupo = 1
            tiempo_actual = senal_actual.getDato().lista_tiempos.getInicio()
            print("> Sumando tuplas de la senal", senal_actual.getDato().nombre, "...")
            while tiempo_actual != None:
                

                if tiempo_actual.getDato().grupo == False:

                    grupo_nuevo = Grupo(numero_grupo)
                    senal_actual.getDato().matriz_reducida_grupos.insertar(grupo_nuevo)
                    grupo_nuevo.tiempos = grupo_nuevo.tiempos + str(tiempo_actual.getDato().tiempo) + " "
                    self.llenar_amplitudes(grupo_nuevo, tiempo_actual.getDato().lista_amplitudes.getInicio(), True)

                    tiempo_temporal = tiempo_actual.getSiguiente()

                    while tiempo_temporal != None:

                        if tiempo_temporal.getDato().grupo == False:

                            if tiempo_actual.getDato().binario == tiempo_temporal.getDato().binario:
                                tiempo_temporal.getDato().grupo = True
                                tiempo_actual.getDato().grupo = True
                                tiempo_actual.getDato().grupo_asociado = numero_grupo
                                tiempo_temporal.getDato().grupo_asociado = numero_grupo
                                self.llenar_amplitudes(grupo_nuevo, tiempo_temporal.getDato().lista_amplitudes.getInicio(), False)
                                grupo_nuevo.tiempos = grupo_nuevo.tiempos + str(tiempo_temporal.getDato().tiempo) + " "
                        
                        tiempo_temporal = tiempo_temporal.getSiguiente()

                    if tiempo_actual.getDato().grupo == False:
                        tiempo_actual.getDato().grupo = True
                        tiempo_actual.getDato().grupo_asociado = numero_grupo
                    
                    numero_grupo += 1

                tiempo_actual = tiempo_actual.getSiguiente()

            print("> Se han creado los grupos de la senal", senal_actual.getDato().nombre, "con éxito...")
            print("> Se han sumado las tuplas de la senal", senal_actual.getDato().nombre, "con éxito...")
            senal_actual = senal_actual.getSiguiente()
        

    #Mando la primera aplpitud de cada tiempo a llenar_amplitudes
    def llenar_amplitudes(self, grupo, amplitud, primera_llamada):
        amplitud_actual = amplitud
        amplitud_actual_grupo = grupo.lista_amplitudes.getInicio()

        if primera_llamada:
            while amplitud_actual != None:
                amplitud_nueva = Amplitud(amplitud_actual.getDato().amplitud, amplitud_actual.getDato().dato)
                grupo.lista_amplitudes.insertar(amplitud_nueva)
                amplitud_actual = amplitud_actual.getSiguiente()
        else:
            while amplitud_actual != None:
                amplitud_actual_grupo.getDato().dato = amplitud_actual_grupo.getDato().dato + amplitud_actual.getDato().dato
                amplitud_actual_grupo = amplitud_actual_grupo.getSiguiente()
                amplitud_actual = amplitud_actual.getSiguiente()

            

            

                
