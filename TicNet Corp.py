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
    # contadorFallas = 0
    os.system('cls')
    print(f"Usted ha elegido la opción {option}")
    contador = 4
    # contadorFallas = 4
    return contador


###########inicio reto3 #######
coordenadas = []
#coordenadas = [[6.088, -75.888], [6.100, -75.999], [6.200, -76.000]]


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


os.system('cls')
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
if input("Ingrese su nombre de usuario: ") == usuarioGuardado and input("Ingrese su contraseña: ") == contrasenaGuardado:
    if (input(f"{capcha1} + {capcha2} = ") == "213"):
        os.system('cls')
        print("Sesión iniciada")
        while contadorFallas < 4:
            for x in range(len(listMenu)):
                print(f"{x+1}. {listMenu[x]}")
            optionMenu = int(input("Elija una opción "))
            if ((optionMenu <= len(listMenu)) and (optionMenu >= 0)):
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
                    contadorFallas = msjOption(optionMenu)
                elif optionMenuNombre == opt4:
                    contadorFallas = msjOption(optionMenu)
                elif optionMenuNombre == opt5:
                    contadorFallas = msjOption(optionMenu)
                elif optionMenuNombre == opt6:
                    #contadorFallas = 0
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
