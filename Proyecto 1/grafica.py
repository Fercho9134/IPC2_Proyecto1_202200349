from graphviz import Digraph

class Grafica:
    def __init__(self, lista_senales_general):
        self.lista_senales_general = lista_senales_general

    def graficar_frecuencias(self, senal_graficar):
        if self.lista_senales_general.listaVacia():
            print("\nNo hay senales para graficar...")
            print("Volviendo al menú inicial...\n")
            return
        
        senal_actual = self.lista_senales_general.getInicio()
        encontro_senal = False

        while senal_actual != None:
                    
            if senal_actual.getDato().nombre == senal_graficar:
                encontro_senal = True
                print("> Generando grafica de la matriz de frecuencias...")
                graph = Digraph(str(senal_actual.getDato().nombre + "- Matriz de frecuencias"), filename=str(senal_actual.getDato().nombre) + "- Matriz de frecuencias" + ".gv", format="png")
                graph.node(str(senal_actual.codigo), str(senal_actual.getDato().nombre))
                graph.node(str(senal_actual.codigo) + "t", ("t = " + str(senal_actual.getDato().tiempo_maximo)))
                graph.node(str(senal_actual.codigo) + "A", ("A = " + str(senal_actual.getDato().amplitud_maxima)))
                
                graph.edge(str(senal_actual.codigo), str(senal_actual.codigo) + "t")
                graph.edge(str(senal_actual.codigo), str(senal_actual.codigo) + "A")    

                tiempo_actual = senal_actual.getDato().lista_tiempos.getInicio()

                primer_tiempo = True

                for i in range(1, senal_actual.getDato().tiempo_maximo + 1):
                    
                    amplitud_actual = tiempo_actual.getDato().lista_amplitudes.getInicio()

                    for j in range(1, senal_actual.getDato().amplitud_maxima + 1):

                        graph.node(str(tiempo_actual.getDato().tiempo) + str(amplitud_actual.getDato().amplitud), str(amplitud_actual.getDato().dato))
                        
                        if primer_tiempo:
                            graph.edge(str(senal_actual.codigo), str(tiempo_actual.getDato().tiempo) + str(amplitud_actual.getDato().amplitud))
                        else:
                            graph.edge(str(tiempo_actual.getDato().tiempo-1) + str(amplitud_actual.getDato().amplitud), str(tiempo_actual.getDato().tiempo) + str(amplitud_actual.getDato().amplitud))
                        
                                                        
                        amplitud_actual = amplitud_actual.getSiguiente()
                    
                    primer_tiempo = False
                    tiempo_actual = tiempo_actual.getSiguiente()

                senal_actual = senal_actual.getSiguiente()
                graph.render(view=True)
   
            else:
                senal_actual = senal_actual.getSiguiente()
        
        if not encontro_senal:
            return
                   
        


    def graficar_matriz_reducida(self, senal_graficar):

        if self.lista_senales_general.listaVacia():
            print("\nNo hay senales para graficar...")
            print("Volviendo al menú inicial...\n")
            return
        
        encontro_senal = False
        senal_actual = self.lista_senales_general.getInicio()

        while senal_actual != None:
                    
            if senal_actual.getDato().nombre == senal_graficar:
                encontro_senal = True
                print("> Generando grafica de la matriz reducida...")
                graph = Digraph(str(senal_actual.getDato().nombre) + " - Matriz reducida", filename=str(senal_actual.getDato().nombre) + "- Matriz reducida"+".gv", format="png")
                
                graph.node(str(senal_actual.codigo), str(senal_actual.getDato().nombre) + " reducida")
                graph.node(str(senal_actual.codigo) + "A", ("A = " + str(senal_actual.getDato().amplitud_maxima)))
                
                graph.edge(str(senal_actual.codigo), str(senal_actual.codigo) + "A")    

                
                grupo_actual = senal_actual.getDato().matriz_reducida_grupos.getInicio()

                primer_grupo = True


                for i in range(1, int(senal_actual.getDato().matriz_reducida_grupos.contar()) + 1):
                    
                    amplitud_actual = grupo_actual.getDato().lista_amplitudes.getInicio()

                    for j in range(0, senal_actual.getDato().amplitud_maxima + 1):

                        if j == 0:
                            graph.node(str(i) + str(j), str(grupo_actual.getDato().nombre) + " t =(" + str(grupo_actual.getDato().tiempos) + ")")
                        else:
                            graph.node(str(i) + str(j), str(amplitud_actual.getDato().dato))
                        
                        if primer_grupo:
                            graph.edge(str(senal_actual.codigo), str(i) + str(j))
                        else:
                            graph.edge(str(i-1) + str(j), str(i) + str(j))
                        
                        if j != 0:                                
                            amplitud_actual = amplitud_actual.getSiguiente()
                    
                    primer_grupo = False
                    grupo_actual = grupo_actual.getSiguiente()

                senal_actual = senal_actual.getSiguiente()
                graph.render(view=True)
                print("> Graficas generadas con éxito...\n")
   
            else:
                senal_actual = senal_actual.getSiguiente() 
            
        if not encontro_senal:
            print("a")
            print("> No se encontró la señal...")
            print("> Volviendo al menú inicial...\n")
            return
                   
       

