import xml.etree.ElementTree as ET
import xml.dom.minidom
class EscribirXML:

    def __init__(self, lista_senales_general):
        self.lista_senales_general = lista_senales_general
    
    def escribir(self):

        if self.lista_senales_general.listaVacia():
            print("\nPrimero procese el archivo XML...")
            print("Volviendo al menú inicial...\n")
            return
        
        print("> Generando el archivo de salida...")
        senales_reducidas = ET.Element("senalesReducidas")
        senal_actual = self.lista_senales_general.getInicio()

        while senal_actual != None:

            senal = ET.SubElement(senales_reducidas, "senal")
            senal.set("nombre", senal_actual.getDato().nombre)
            senal.set("A", str(senal_actual.getDato().amplitud_maxima))    
            grupo_actual = senal_actual.getDato().matriz_reducida_grupos.getInicio()

            #Para cada grupo
            for i in range(1, int(senal_actual.getDato().matriz_reducida_grupos.contar()) + 1):
                grupo = ET.SubElement(senal, "grupo")
                grupo.set("g", str(i))

                tiempos = ET.SubElement(grupo, "tiempos")
                dato_tiempos = grupo_actual.getDato().tiempos.rstrip()
                tiempos.text = str(",".join(dato_tiempos.split()))

                datos_grupo = ET.SubElement(grupo, "datosGrupo")

                amplitud_actual = grupo_actual.getDato().lista_amplitudes.getInicio()

                for j in range(1, int(senal_actual.getDato().amplitud_maxima) + 1):
                    dato = ET.SubElement(datos_grupo, "dato")
                    dato.set("A", str(j))
                    dato.text = str(amplitud_actual.getDato().dato)
                    amplitud_actual = amplitud_actual.getSiguiente()
                
                grupo_actual = grupo_actual.getSiguiente()
            
            senal_actual = senal_actual.getSiguiente()
        
        tree = ET.ElementTree(senales_reducidas)

        xmlstr = ET.tostring(senales_reducidas, encoding="utf-8")
        dom = xml.dom.minidom.parseString(xmlstr)

        with open("SenalesReducidas.xml", "wb") as archivo:
            archivo.write(dom.toprettyxml(indent="   ").encode("utf-8"))


        print("> Archivo XML generado exitosamente en la carpeta raiz del proyecto\n")
