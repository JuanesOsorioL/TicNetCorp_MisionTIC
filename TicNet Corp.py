import math
import os

usuarioGuardado = "52212"
contrasenaGuardado = "21225"
capcha1 = 212
capcha2 = (2 + 1) - ((5 % 2) * 2)
capcha = capcha1 + capcha2

opt1 = "Cambiar contraseña"
opt2 = "Ingresar coordenadas actuales"
opt3 = "Ubicar zona wifi más cercana"
opt4 = "Guardar archivo con ubicación cercana"
opt5 = "Actualizar registros de zonas wifi desde archivo"
opt6 = "Elegir opción de menú favorita"
opt7 = "Cerrar sesión"
listMenu = [opt1, opt2, opt3, opt4, opt5, opt6, opt7]

control = True
contadorFallas = 0


def updateMenu(position):
    optionTexto = listMenu[position-1]
    listMenu.remove(optionTexto)
    listMenu.insert(0, optionTexto)


def msjOption(option):
    os.system('cls')
    print(f"Usted ha elegido la opción {option}")
    contador = 4
    return contador


###########inicio reto3 #######
coordenadas = []
# coordenadas = [[6.088, -75.888], [6.100, -75.999], [6.200, -76.000]]
#coordenadas = [[6.183, -75.973], [6.188, -75.974], [6.187, -75.975]]


def ingresarCoordenadas():
    latitud = validarLatitudLongitud("latitud")
    if latitud == "Error" or latitud == "Error coordenada":
        os.system('cls')
        print(latitud)
    else:
        longitud = validarLatitudLongitud("longitud")
        if longitud == "Error" or longitud == "Error coordenada":
            os.system('cls')
            print(longitud)
        else:
            return [float(latitud), float(longitud)]


def validarLatitudLongitud(coordenada):
    valor = input(f"Ingrese la {coordenada}: ")
    if (valor == "" or valor == " "):
        return "Error"
    else:
        if coordenada == "latitud":
            if float(valor) >= 6.077 and float(valor) <= 6.284:
                return valor
            else:
                return "Error coordenada"
        else:
            if float(valor) >= -76.049 and float(valor) <= -75.841:
                return valor
            else:
                return "Error coordenada"


def mostrarListaCoordenadas(listaCoordenadas):
    for x in range(0, len(listaCoordenadas)):
        print(
            f"coordenada [latitud, longitud] {x+1} : ['{listaCoordenadas[x][0]}','{listaCoordenadas[x][1]}']")


def mostrarLatitudMasNorte(listaCoordenadas):
    masAlNorte = 6.066
    posicion = 0
    for x in range(0, len(listaCoordenadas)):
        if masAlNorte < listaCoordenadas[x][0]:
            masAlNorte = listaCoordenadas[x][0]
            posicion = x+1
    print(f"La Coordenada {posicion} es la que está más al norte")


def mostrarLongitudMasOccidente(listaCoordenadas):
    masAlOccidente = -75.841
    posicion = 0
    for x in range(0, len(listaCoordenadas)):
        if masAlOccidente > listaCoordenadas[x][1]:
            masAlOccidente = listaCoordenadas[x][1]
            posicion = x+1
    print(f"La Coordenada {posicion} es la que está más al occidente")


def actualizarCoordenadas(posicion, listaCoordenadas):
    lista = ingresarCoordenadas()
    if lista:
        listaCoordenadas[posicion] = lista
        return True
    else:
        return False


###########fin reto3 #######

###########inicio reto4 #######
r = 6373
zonasWifiDistancias = []
zonaswifi = [[6.124, -75.946, 1035], [6.125, -75.966, 109],
             [6.135, -75.976, 31], [6.144, -75.836, 151]]


def calcularDistancia(coordenada):
    for x in range(len(zonaswifi)):
        coordenadaZonaWifi = zonaswifi[x]
        lat1 = coordenada[0]
        lon1 = coordenada[1]
        lat2 = coordenadaZonaWifi[0]
        lon2 = coordenadaZonaWifi[1]
        latdelta = lat2-lat1
        londelta = lon2-lon1
        operacion = math.sin(londelta/2)**2
        operacion = operacion*(math.cos(lat1)*math.cos(lat2))
        operacion = (math.sin(latdelta/2)**2)*operacion
        operacion = math.sqrt(operacion)
        operacion = math.asin(operacion)
        operacion = (2*r)*operacion
        operacion = operacion*1000
        operacion = round(operacion)

        lista = [operacion, coordenadaZonaWifi[0],
                 coordenadaZonaWifi[1], coordenadaZonaWifi[2]]
        zonasWifiDistancias.append(lista)
    return zonasWifiDistancias


def mostrarMasCercana(Distancia):
    control = True
    cont = 1
    mostrarprimero = []
    mostrarsegundo = []
    segundo = 0
    posicion = 0
    copiaLista = list(Distancia)
    while control:
        for x in range(len(copiaLista)):
            if x == 0:
                segundo = copiaLista[x][0]
                mostrarsegundo = copiaLista[x]
            elif segundo > copiaLista[x][0]:
                segundo = copiaLista[x][0]
                mostrarsegundo = copiaLista[x]
                posicion = x
        if cont == 2:
            control = False
        else:
            copiaLista.pop(posicion)
            mostrarprimero = mostrarsegundo
            cont = cont+1
    return [mostrarprimero, mostrarsegundo]


def mostrarWifiCercanas(lista):
    primero = lista[0]
    segundo = lista[1]
    print(f"La zona wifi 1: ubicada en ['{primero[1]}','{primero[2]}'] a {primero[0]} metros , tiene en promedio {primero[3]} usuarios\nLa zona wifi 2: ubicada en ['{segundo[1]}','{segundo[2]}'] a {segundo[0]} metros , tiene en promedio {segundo[3]} usuarios")


def direccionZonaWifi(usuario, zonaWifi):
    msj = ""
    msj1 = ""
    if usuario[1] > zonaWifi[2]:
        msj = "occidente"
    else:
        msj = "oriente"

    if usuario[0] > zonaWifi[1]:
        msj1 = "sur"
    else:
        msj1 = "norte"
    print(
        f"Para llegar a la zona wifi dirigirse primero al {msj} y luego hacia el {msj1}")


def menuCalcularDistancia(usuario):
    listaDistancias = calcularDistancia(usuario)
    listaDistancias = mostrarMasCercana(listaDistancias)
    if listaDistancias[0][3] > listaDistancias[1][3]:
        optionTexto = listaDistancias[1]
        listaDistancias.remove(optionTexto)
        listaDistancias.insert(0, optionTexto)
    return listaDistancias


def tiempoViaje(ZonaWifi):
    msjTiempoBus = "segundos"
    msjTiempoAuto = "segundos"
    distancia = ZonaWifi[0]
    tiempoBus = distancia/16.67
    if tiempoBus > 60:
        tiempoBus = round(tiempoBus/60)
        msjTiempoBus = "minutos"
    tiempoAuto = distancia/20.83
    if tiempoAuto > 60:
        tiempoAuto = round(tiempoAuto/60)
        msjTiempoAuto = "minutos"
    informacion['recorrido'] = [distancia, 'Bus', tiempoBus]
    print(
        f"El tiempo promedio que tardaría en Bus = {tiempoBus} {msjTiempoBus}\nEl tiempo promedio que tardaría en Auto = {tiempoAuto} {msjTiempoAuto}")


def subMenuWifiCercanas(usuario, listaDistancias):
    direccionZonaWifi(usuario, listaDistancias)
    tiempoViaje(listaDistancias)


###########inicio reto5 #######
informacion = {}
###########fin reto5 #######

########### easter #######


def egg411():
    print("Este fue mi primer programa y vamos por más")


def egg421():
    os.system('cls')
    hemisferio = int(input("Dame una latitud y te diré cual hemisferio es… "))
    if hemisferio > 0:
        print("Usted está en hemisferio norte")
    else:
        print("Usted está en hemisferio sur")


def egg511():
    cantidad = int(
        input('Ingrese la cantidad de latitudes que desea calcular '))
    suma = 0
    for i in range(cantidad):
        os.system('cls')
        suma = suma + float(input(f'Latitud {i+1}: '))
    os.system('cls')
    dividir = suma/cantidad
    print(f"El promedio de latitudes ingresadas es : {dividir} ")


def egg512():
    os.system('cls')
    coordenadaSudamerica = float(input(
        "Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario "))
    if coordenadaSudamerica <= -35.833 and coordenadaSudamerica >= -54.316:
        print('El huso horario es -3')
    elif coordenadaSudamerica <= -54.316 and coordenadaSudamerica >= -67.402:
        print('El huso horario es -4')
    elif coordenadaSudamerica <= -67.401 and coordenadaSudamerica >= -81.296:
        print('El huso horario es -5')
########### easter #######


os.system('cls')
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
LoguinUsuario = input("Ingrese su nombre de usuario: ")

if LoguinUsuario == "Tripulante2022":
    egg411()
elif LoguinUsuario == usuarioGuardado:
    LoguinPassword = input("Ingrese su contraseña: ")
    if LoguinPassword == "m1s10nt1c":
        egg511()
    elif LoguinPassword == contrasenaGuardado:
        if (input(f"{capcha1} + {capcha2} = ") == "213"):
            os.system('cls')
            print("Sesión iniciada")
            while contadorFallas < 4:
                for x in range(len(listMenu)):
                    print(f"{x+1}. {listMenu[x]}")
                optionMenu = int(input("Elija una opción "))
                if optionMenu == 2021:
                    egg421()
                    contadorFallas = 4
                elif optionMenu == 2022:
                    egg512()
                    contadorFallas = 4

                elif((optionMenu <= len(listMenu)) and (optionMenu >= 0)):
                    optionMenuNombre = listMenu[optionMenu-1]

                    if optionMenuNombre == opt1:
                        os.system('cls')
                        if (contrasenaGuardado == input("confirmar la contraseña actual: ")):
                            contrasenaGuardado = input(
                                "Nueva contraseña del usuario: ")
                            os.system('cls')
                        else:
                            os.system('cls')
                            print("Error")
                            contadorFallas = 4
                    elif optionMenuNombre == opt2:
                        os.system('cls')
                        if (coordenadas == []):
                            for x in range(0, 3):
                                lista = ingresarCoordenadas()
                                if lista:
                                    coordenadas.append(lista)
                                    os.system('cls')
                                else:
                                    coordenadas = []
                                    contadorFallas = 4
                                    break
                        else:
                            mostrarListaCoordenadas(coordenadas)
                            mostrarLatitudMasNorte(coordenadas)
                            mostrarLongitudMasOccidente(coordenadas)
                            option = int(input(
                                "Presione 1, 2 ó 3 para actualizar la respectiva coordenada.\nPresione 0 para regresar al menú "))
                            if option == 0:
                                os.system('cls')
                            elif option == 1 or option == 2 or option == 3:
                                if option == 1:
                                    if actualizarCoordenadas(0, coordenadas):
                                        os.system('cls')
                                    else:
                                        contadorFallas = 4
                                elif option == 2:
                                    if actualizarCoordenadas(1, coordenadas):
                                        os.system('cls')
                                    else:
                                        contadorFallas = 4
                                elif option == 3:
                                    if actualizarCoordenadas(2, coordenadas):
                                        os.system('cls')
                                    else:
                                        contadorFallas = 4
                            else:
                                os.system('cls')
                                print("Error actualización")
                                contadorFallas = 4
                    elif optionMenuNombre == opt3:
                        os.system('cls')
                        if (coordenadas == []):
                            print("Error sin registro de coordenadas")
                            contadorFallas = 4
                        else:
                            mostrarListaCoordenadas(coordenadas)
                            option = input(
                                "Por favor elija su ubicación actual(1, 2 ó 3) para calcular la distancia a los puntos de conexión ")
                            if int(option) == 1 or int(option) == 2 or int(option) == 3:
                                informacion['actual'] = coordenadas[(
                                    int(option)-1)]
                                usuario = coordenadas[(int(option)-1)]
                                listaDistancias = menuCalcularDistancia(
                                    usuario)
                                os.system('cls')
                                print("Zonas wifi cercanas con menos usuarios")
                                mostrarWifiCercanas(listaDistancias)
                                optionIndicacion = input(
                                    "Elija 1 o 2 para recibir indicaciones de  llegada ")
                                if int(optionIndicacion) == 1 or int(optionIndicacion) == 2:

                                    informacion['zonawifi1'] = [
                                        listaDistancias[int(optionIndicacion)-1][1], listaDistancias[int(optionIndicacion)-1][2], listaDistancias[int(optionIndicacion)-1][3]]

                                    subMenuWifiCercanas(
                                        usuario, listaDistancias[int(optionIndicacion)-1])

                                    if input("Presione 0 para salir ") == "0":
                                        os.system('cls')
                                    else:
                                        print("Error zona wifi")
                                        contadorFallas = 4
                                else:
                                    print("Error zona wifi")
                                    contadorFallas = 4
                            else:
                                print("Error ubicación")
                                contadorFallas = 4
                    elif optionMenuNombre == opt4:
                        os.system('cls')
                        if (informacion == {}):
                            print("Error de alistamiento")
                            contadorFallas = 4
                        else:
                            print(informacion)
                            option = input(
                                '¿Está de acuerdo con la información a exportar?\nPresione 1 para confirmar, 0 para regresar al menú principal ')
                            if (option == "1"):
                                os.system('cls')
                                #base = os.getcwd()
                                archivo = open(
                                    r'C:\Users\juanc\Desktop\TIC\ciclo 1\programacion\Unidad 4\Reto5\fichero.txt', "a")
                                archivo.write(str(informacion))
                                print('Exportando archivo')
                                contadorFallas = 4
                            else:
                                os.system('cls')
                    elif optionMenuNombre == opt5:
                        os.system('cls')
                        #datos = []
                        #archivo = open(r'C:\Users\juanc\Desktop\TIC\ciclo 1\programacion\Unidad 4\Reto5\wifi.txt')
                        # for i in archivo.readlines():
                        #valor = i.replace('\n', '')
                        # datos.append(float(valor))

                        #coordenadas = [[datos[0], datos[1]], [datos[2], datos[3]], [datos[4], datos[5]]]

                        input(
                            'Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principa ')
                        os.system('cls')
                    elif optionMenuNombre == opt6:
                        optionMenu6 = int(input("Seleccione opción favorita "))
                        if optionMenu6 == 1 or optionMenu6 == 2 or optionMenu6 == 3 or optionMenu6 == 4 or optionMenu6 == 5:
                            if input("De muchos hijos que somos, el primero yo nací, pero soy el menor de todos. ¿Cómo puede ser así?,¿sabes cuál número soy? ") == "1" and input("Soy más de uno sin llegar a tres y llego a cuatro cuando dos me des. ¿Cuál número soy? ") == "2":
                                os.system('cls')
                                updateMenu(optionMenu6)
                                continue
                            else:
                                os.system('cls')
                                contadorFallas = 4
                                print("Error")
                                continue
                        else:
                            contadorFallas = 4
                            print("Error")
                            continue
                    elif optionMenuNombre == opt7:
                        os.system('cls')
                        print("Hasta pronto")
                        contadorFallas = 4
                else:
                    contadorFallas += 1
                    os.system('cls')
                    print("Error")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
