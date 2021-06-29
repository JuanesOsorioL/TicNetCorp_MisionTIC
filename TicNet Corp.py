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
                contadorFallas = msjOption(optionMenu)
            elif optionMenuNombre == opt2:
                contadorFallas = msjOption(optionMenu)
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
