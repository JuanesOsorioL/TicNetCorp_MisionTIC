usuarioGuardado = "52212"
contrasenaGuardado = "21225"
capcha1 = 212
capcha2 = (2 + 1) - ((5 % 2) * 2)
capcha = capcha1 + capcha2

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

if input("Ingrese su nombre de usuario: ") == usuarioGuardado and input("Ingrese su contraseña: ") == contrasenaGuardado:
    if (input(f"{capcha1} + {capcha2} = ") == "213"):
        print("Sesión iniciada")
    else:
        print("Error")
else:
    print("Error")
