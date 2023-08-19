import tkinter as tk
from tkinter import filedialog
from procesar_xml import ProcesarXML
from lista_simple import ListaSimple

class metodos:

    def __init__(self):
        self.ruta_archivo = ""
        self.lista_senales_general = ListaSimple()
    
    def menu(self):
        print("╔══════════════════════════════════╗")
        print("║             Menú inicial         ║")
        print("╠══════════════════════════════════╣")
        print("║ 1. Cargar archivo                ║")
        print("║ 2. Procesar archivo              ║")
        print("║ 3. Imprimir tablas señales (tmp) ║")
        print("║ 4. Mostrar datos estudiante      ║")
        print("║ 5. Generar gráfica               ║")
        print("║ 6. Inicializar sistema           ║")
        print("║ 7. Salida                        ║")
        print("╚══════════════════════════════════╝")

        print("Ingrese una opción: ", end="")
        opcion = input()
        self.seleccionar_opcion(opcion)

    def seleccionar_opcion(self, opcion):

        if opcion.isnumeric():

            opcion = int(opcion)

            if opcion == 1:
                #Obtener la ruta del archivo
                direccion_archivo = ""
                root = tk.Tk()
                direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos de Senales", "*.xml")])
                root.destroy()

                if direccion_archivo == "" or direccion_archivo == None:
                    print("\nNo se seleccionó ningún archivo...")
                    print("Volviendo al menú inicial...\n")
                    self.menu()
                    return
                
                else:
                    self.ruta_archivo = direccion_archivo
                    print("\nArchivo cargado con éxito...")
                    print("Volviendo al menú inicial...\n")
                self.menu()
                return


            elif opcion == 2:

                if self.ruta_archivo == "" or self.ruta_archivo == None:
                    print("\nPrimero cargue el archivo XML...")
                    print("Volviendo al menú inicial...\n")
                    self.menu()
                    return

                procesar = ProcesarXML(self.ruta_archivo, self.lista_senales_general)
                print("\n> El archivo se está procesando, por favor espere...")
                procesar.procesar_archivo()
                print("> El archivo se ha procesado con éxito...\n")
                self.menu()
                return  


            elif opcion == 3:

                if self.lista_senales_general.listaVacia():
                    print("\nPrimero procese el archivo XML...")
                    print("Volviendo al menú inicial...\n")
                    self.menu()
                    return
                
                senal_actual = self.lista_senales_general.getInicio()

                while senal_actual != None:
                    print("\nNombre senal actual:", senal_actual.getDato().nombre)
                    print("Tiempo maximo senal actual:", senal_actual.getDato().tiempo_maximo)
                    print("Amplitud maxima senal actual:", senal_actual.getDato().amplitud_maxima,"\n")
                    
                    tiempo_actual = senal_actual.getDato().lista_tiempos.getInicio()

                    while tiempo_actual != None:
                        print("Tiempo:", tiempo_actual.getDato().tiempo)
                        amplitud_actual = tiempo_actual.getDato().lista_amplitudes.getInicio()

                        while amplitud_actual != None:
                            print(f"   Amplitud {amplitud_actual.getDato().amplitud} - Dato: {amplitud_actual.getDato().dato}")
                            amplitud_actual = amplitud_actual.getSiguiente()
                        
                        tiempo_actual = tiempo_actual.getSiguiente()
                    
                    senal_actual = senal_actual.getSiguiente()
                    print("\n")
                    

                self.menu()
                return

                
            elif opcion == 4:

                print("\nDatos del estudiante:")
                print("> Nombre: Irving Fernando Alvarado Asensio")
                print("> Carné: 202200349")
                print("> Curso: Introducción a la Programación y Computación 2 Sección N")
                print("> Carrera: Ingeniería en Ciencias y Sistemas")
                print("> Semestre: 4to\n")
                self.menu()
                return


            elif opcion == 5:

                print("\nGenerar gráfica")
                self.menu()
                return


            elif opcion == 6:

                print("\nInicializar sistema")
                self.menu()
                return


            elif opcion == 7:

                print("\nGracias por usar el programa, Saliendo...")
                exit()


            else:

                print("\nOpción inválida... Ingrese una opción correcta\n")
                self.menu()
                return


        else:

            print("\nOpción inválida... Ingrese una opción correcta\n\n")
            self.menu()
            return

        
if __name__ == "__main__":
    inicio = metodos()
    inicio.menu()