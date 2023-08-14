class metodos:
    
    def menu(self):
        print("########## Menu Principal ##########")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar grafica")
        print("6. Inicializar sistema")
        print("7. Salida")

        print("Ingrese una opcion: ")
        opcion = input()

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                print("Cargar archivo")
            elif opcion == 2:
                print("Procesar archivo")
            elif opcion == 3:
                print("Escribir archivo salida")
            elif opcion == 4:
                print("Mostrar datos del estudiante")
            elif opcion == 5:
                print("Generar grafica")
            elif opcion == 6:
                print("Inicializar sistema")
            elif opcion == 7:
                print("Gracias por utilizar el sistema")
            else:
                print("Opcion no valida\n\n")
                self.menu()
        else:
            print("Opcion no valida\n\n")
            self.menu()

        
             