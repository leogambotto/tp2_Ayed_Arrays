cupos = ["", "", "", "", "", "", "", ""] 
productoCamion = ["", "", "", "", "", "", "", ""]
estado = ['', '', '', '', '', '', '', '']

auxProductoCamion = ""
auxEstado = ''
auxPatente = ""
auxPeso = 0

productos = ["", "", ""]

tara = [0, 0, 0, 0, 0, 0, 0, 0]
pesoBruto = [0, 0, 0, 0, 0, 0, 0, 0]
pesoNeto = [0, 0, 0, 0, 0, 0, 0, 0]

totalNeto = [0, 0, 0] 
promedioNeto = [0, 0, 0] 

menorPeso = [0, 0, 0]
mayorPeso = [0, 0, 0]
menorPatente = ["", "", ""]
mayorPatente = ["", "", ""]

camion = [0, 0, 0]
contadorCamiones = [0, 0, 0]

posicion = 0
punteroCamion = 0
camionesRecibidos = 0

def menuPrincipal():
    print("\n\tPROGRAMA PRINCIPAL\n")
    print("1- Administraciones")
    print("2- Entrega de Cupos")
    print("3- Recepcion")
    print("4- Registrar Calidad")
    print("5- Registrar Peso Bruto")
    print("6- Registrar Descarga")
    print("7- Registrar Tara")
    print("8- Reportes")
    print("0- FIN DEL PROGRAMA") 

def administraciones():
    opcion = ''
    
    while(opcion != 'V'):
        print("\n\tAdministraciones\n")
        print("A- Titulares")
        print("B- Productos")
        print("C- Rubros")
        print("D- Rubros x Producto")
        print("E- Silos")
        print("F- Sucursales")
        print("G- Producto Por Titular")
        print("V- Volver al Menu Principal")

        opcion = input("Ingrese una opción: ")
                
        if opcion == 'A':
            print("Esta funcionalidad está en construcción")
        elif opcion == 'B':
            menuDeAdministraciones()
        elif opcion == 'C':
            print("Esta funcionalidad está en construcción")
        elif opcion == 'D':
            print("Esta funcionalidad está en construcción")
        elif opcion == 'E':
            print("Esta funcionalidad está en construcción")
        elif opcion == 'F':
            print("Esta funcionalidad está en construcción")
        elif opcion == 'G':
            print("Esta funcionalidad está en construcción")

def menuDeAdministraciones():
    opcion = ''

    while(opcion != 'V'):

        print("\n")

        print("A. Alta")
        print("B. Baja")
        print("C. Consulta")
        print("M. Modificiación")
        print("V. Volver al menú anterior")

        opcion = input("Ingrese una opción: ")

        if(opcion == 'A'):
            print("Productos sugeridos trigo, soja, maiz, girasol y/o cebada\n")

            for i in range(0,3):
                if(productos[i] == ""):
                    print(i+1)
                    productos[i] = input("Producto: ")
                else:
                    print("La posición", (i + 1), "esta ocupada con: ")
                    print(productos[i])          
        elif(opcion == 'B'):
            print("Lista de productos\n")
            print("A. ", productos[0], "\n")
            print("B. ", productos[1], "\n")
            print("C. ", productos[2], "\n")

            opcion = input("¿Qué producto deseas eliminar?: ")
            
            if(opcion == "A"):
                productos[0] = ""
                print("producto eliminado")
            elif(opcion == "B"):
                productos[1] = ""
                print("producto eliminado")
            elif(opcion == "C"):
                productos[2] = ""
                print("producto eliminado")
            else:
                print("Opción inválida")         
        elif(opcion == 'C'):
            print("Lista de productos\n")
           
            print("A. ", productos[0], "\n")
            print("B. ", productos[1], "\n")
            print("C. ", productos[2], "\n")
        elif(opcion == 'M'):
            print("Lista de productos\n")
           
            print("A. ", productos[0], "\n")
            print("B. ", productos[1], "\n")
            print("C. ", productos[2], "\n")

            opcion = input("¿Qué numero deseas modificar?: ")
            
            if(opcion == "A"):
                productos[0] = input("Ingrese el nuevo producto: ")
                print("producto registrado")
            elif(opcion == "B"):
                productos[1] = input("Ingrese el nuevo producto: ")
                print("producto registrado")
            elif(opcion == "C"):
                productos[2] = input("Ingrese el nuevo producto: ")
                print("producto registrado")
            else:
                print("Opción inválida")  

def entregaCupos():
    print("\n\tEntrega de Cupos\n")

    patente = ""
    global posicion

    while(patente != "V"):    
        patente = input("Ingese la patente (ó V. Volver): ")

        if(largoPatente(patente) == True):
            if(cupoLibre() == True):
                if(cupoDuplicado(patente) == False):
                    cupos[posicion] = patente
                    estado[posicion] = 'P'

                    posicion = posicion + 1
                    
                    print("\nSe asignadó exitosamente un cupo al camión #", patente, " y se actualizó su estado a Pendiente")
                    print("Cupos restantes ", (8 - posicion), "\n")
                else:
                    print("Ésta patente ya posee un cupo")           
            else:
                print("No quedan más cupos disponibles")
        else:
            print("Patente inválida, la patente debe estar compuesta por 6 ó 7 caracteres")

def cupoDuplicado(patente):
    i = 0 
    busqueda = False
    
    while(busqueda == False and i < 8):
        if(patente == cupos[i]):
            busqueda = True
        i += 1

    return busqueda
    
def cupoLibre():
    if(posicion < 8 and cupos[posicion] == ""):
        return True
    else:
        return False

def largoPatente(patente):
    contador = 0
    
    while(patente[contador:]):
        contador += 1
    
    if(contador >= 6 and contador <= 7):
        return True
    else:
        return False
    
def recepcion():
    print("\n\tRecepción\n")

    patente = ""
    global camionesRecibidos

    while(patente != "V"):        
        patente = input("Ingrese la patente (ó V. para volver): ")
        
        if(patente != "V"):
            if(largoPatente(patente) == True):
                if(cupoDuplicado(patente) == True): 
                    if(estadoPendiente(patente) == True):
                        estado[punteroCamion] = 'E'
                        print("Se actualizó el estado de Pendiente a En Proceso")

                        camionesRecibidos += 1 
                    else:
                        print("Éste camión no posee un cupo en estado Pendiente")         
                else:
                    print("Ésta patente no posee un cupo, vuelva a intenarlo ó adquiera un cupo")     
            else:
                print("Patente inválida, la patente debe estar compuesta por 6 ó 7 caracteres")

def estadoPendiente(patente):
    global punteroCamion

    i = 0 
    punteroCamion = 0
    
    while(i < 8):
        if(patente == cupos[i]):
            punteroCamion = i
        
            if(estado[punteroCamion] == 'P'):
                return True
        i += 1
    
    return False

def registrarCalidad():
    print("Esta funcionalidad está en construcción")

def registrarPesoBruto():
    print("\n\tRegistrar Peso Bruto\n")

    patente = ""

    while(patente != "V"):        
        patente = input("Ingrese la patente (ó V. para volver): ")

        if(patente != "V"):
            if(largoPatente(patente) == True):
                if(cupoDuplicado(patente) == True):
                    if(estadoEnProceso(patente) == True):
                        if(pesoBrutoLibre() == True):
                            pesoBruto[punteroCamion] = int(input("Ingrese el peso bruto del camion: "))
                            print("Se registro el peso bruto del camion\n")
                        else:
                            print("Éste camión ya tiene un peso bruto registrado")
                    else:
                        print("Éste camión no posee un cupo en estado En Proceso")         
                else:
                    print("Ésta patente no posee un cupo, vuelva a intenarlo ó adquiera un cupo")     
            else:
                print("Patente inválida, la patente debe estar compuesta por 6 ó 7 caracteres")

def estadoEnProceso(patente):
    global punteroCamion
    i = 0 
    punteroCamion = 0

    while(i < 8):
        if(patente == cupos[i]):
            punteroCamion = i
        
            if(estado[punteroCamion] == 'E'):
                return True
        i += 1
    
    return False

def pesoBrutoLibre():
    if(punteroCamion < 8 and pesoBruto[punteroCamion] == 0):
        return True
    else:
        return False

def registrarDescarga():
    print("Esta funcionalidad está en construcción")

def registrarTara():
    print("\n\tRegistrar Tara\n")

    patente = ""

    while(patente != "V"):        
        patente = input("Ingrese la patente (ó V. para volver): ") 
        
        if(patente != "V"):
            if(largoPatente(patente) == True):
                if(cupoDuplicado(patente) == True): 
                    if(estadoEnProceso(patente) == True):
                        if(pesoBrutoLibre() == False):
                            if(taraLibre() == True):
                                producto = ""

                                while(producto != productos[0] and producto != productos[1] and producto != productos[2]):
                                    producto = input("Tipo de producto: ")

                                    if(producto == productos[0]): 
                                        tara[punteroCamion] = int(input("Ingrese la tara del camion: "))

                                        productoCamion[punteroCamion] = producto

                                        contadorCamiones[0] += 1

                                        pesoNeto[punteroCamion] = pesoBruto[punteroCamion] - tara[punteroCamion]
                                        totalNeto[0] += pesoNeto[punteroCamion]

                                        if(pesoNeto[punteroCamion] > mayorPeso[0]):
                                            mayorPeso[0] = pesoNeto[punteroCamion]
                                            mayorPatente[0] = patente

                                        if(pesoNeto[punteroCamion] < menorPeso[0] or camion[0] == 0):
                                            menorPeso[0] = pesoNeto[punteroCamion]
                                            menorPatente[0] = patente
                                            camion[0] = 1      
                                    elif(producto == productos[1]):
                                        tara[punteroCamion] = int(input("Ingrese la tara del camion: "))

                                        productoCamion[punteroCamion] = producto

                                        contadorCamiones[1] += 1

                                        pesoNeto[punteroCamion] = pesoBruto[punteroCamion] - tara[punteroCamion]
                                        totalNeto[1] += pesoNeto[punteroCamion]
                                        
                                        if(pesoNeto[punteroCamion] > mayorPeso[1]):
                                            mayorPeso[1] = pesoNeto[punteroCamion]
                                            mayorPatente[1] = patente

                                        if(pesoNeto[punteroCamion] < menorPeso[1] or camion[1] == 0):
                                            menorPeso[1] = pesoNeto[punteroCamion]
                                            menorPatente[1] = patente       
                                            camion[1] = 1 
                                    elif(producto == productos[2]):
                                        tara[punteroCamion] = int(input("Ingrese la tara del camion: "))

                                        productoCamion[punteroCamion] = producto

                                        contadorCamiones[2] += 1

                                        pesoNeto[punteroCamion] = pesoBruto[punteroCamion] - tara[punteroCamion]
                                        totalNeto[2] += pesoNeto[punteroCamion]
                                        
                                        if(pesoNeto[punteroCamion] > mayorPeso[2]):
                                            mayorPeso[2] = pesoNeto[punteroCamion]
                                            mayorPatente[2] = patente

                                        if(pesoNeto[punteroCamion] < menorPeso[2] or camion[2] == 0):
                                            menorPeso[2] = pesoNeto[punteroCamion]
                                            menorPatente[2] = patente       
                                            camion[2] = 1 
                                    else: 
                                        print("Producto no encontrado")
                            else:
                                print("Éste camión ya tiene una tara registrada")
                        else:
                            print("Éste camión no tiene un peso bruto registrado")
                    else:
                        print("Éste camión no posee un cupo en estado En Proceso")         
                else:
                    print("Ésta patente no posee un cupo, vuelva a intenarlo ó adquiera un cupo")     
            else:
                print("Patente inválida, la patente debe estar compuesta por 6 ó 7 caracteres")
    for i in range(0,3):
        if(contadorCamiones[i] != 0):
            promedioNeto[i] = totalNeto[i] / contadorCamiones[i]
           
def taraLibre():
    if(punteroCamion < 8 and tara[punteroCamion] == 0): 
        return True
    else:
        return False

def reportes():
    print("\tReportes\n")
    
    opcion = ""

    while(opcion != "V"):        
        print("Cantidad de cupos otorgados: ", posicion)
        print("Cantidad total de camiones recibidos: ", camionesRecibidos)
        for i in range(0,3):
            print("Cantidad total de camiones de ", productos[i], ": ", contadorCamiones[i], "kg")
            print("Peso neto total de ", productos[i], ": ", totalNeto[i], "kg")
            print("Promedio del peso neto de ", productos[i], ": ", promedioNeto[i], "kg")
            print("Camión con mayor peso neto de ", productos[i], ": ", mayorPatente[i], " ", mayorPeso[i], "kg") 
            print("Camión con menor peso neto de ", productos[i], ": ", menorPatente[i], " ", menorPeso[i], "kg")
            print("_________________________________________________________")
        
        print("Camiones ordenados por peso descendente: ")
        ordenarPorPeso()
        for i in range(0, 8):
            print("Camion: ", cupos[i], " ", pesoNeto[i], " kg de ", productoCamion[i])
        
        opcion = input("V. para volver: ")

def ordenarPorPeso():
    for i in range(0,7):
        for j  in range(i + 1, 8):
            if(pesoNeto[i] < pesoNeto[j]):
                auxPeso = pesoNeto[i]
                pesoNeto[i] = pesoNeto[j]
                pesoNeto[j] = auxPeso

                auxPatente = cupos[i]
                cupos[i] = cupos[j]
                cupos[j] = auxPatente

                auxProductoCamion = productoCamion[i]
                productoCamion[i] = productoCamion[j]
                productoCamion[j] = auxProductoCamion

                auxEstado = estado[i]
                estado[i] = estado[j]
                estado[j] = auxEstado

opcion = 1
while(opcion != 0):
    menuPrincipal()

    opcion = int(input("Ingrese una opción: "))

    if opcion == 0:
        print("Programa terminado")
    elif opcion == 1:
        administraciones()
    elif opcion == 2:
        entregaCupos()
    elif opcion == 3:
        recepcion()
    elif opcion == 4:
        registrarCalidad()
    elif opcion == 5:
        registrarPesoBruto()
    elif opcion == 6:
        registrarDescarga()
    elif opcion == 7:
        registrarTara()
    elif opcion == 8:
        reportes()
    else:
        print("Elija una opción válida.")
