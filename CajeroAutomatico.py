import os


intentos = 3
while intentos < 3:
    try:
        pwd = 1234
        print('Bienvenido al Cajero Automatico')
        opcion = int(input('Ingrese su Pin: '))

        if opcion == pwd:
            os.system('cls')
            print('Bienvenido Usuario')
        elif opcion != pwd:
            os.system('cls')
            print('Pin incorrecto')

    except ValueError:
        print('pin Incorrecto')
        intentos +=1
if intentos == 3:
    print('Has superado los intentos, se bloqueo su cuenta')