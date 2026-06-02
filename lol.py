saldo = 5
cont = 0
conti = True

while (saldo >= 1.5 and cont < 3 and conti):
    print("maquina de snacks")
    print("1. papas : 1.50")
    print("2. chocolate : 2.0")
    print("3. refresco : 2.5")

    opcion = input()

    if opcion == "salir":
        conti = False
    else:
        opcion = int(opcion)

        if ((opcion == 1 and saldo >= 1.5) or
            (opcion == 2 and saldo >= 2.0) or
            (opcion == 3 and saldo >= 2.5)):

            if opcion == 1:
                saldo = saldo - 1.5
                cont = cont + 1
                print("disfrute sus papas")
            elif opcion == 2:
                saldo = saldo - 2.0
                cont = cont + 1
                print("disfrute su chocolate")
            elif opcion == 3:
                saldo = saldo - 2.5
                cont = cont + 1
                print("disfrute su refresco")

            print("su saldo es: ", saldo)
        else:
            print("error")

print("usted compro ", cont, " productos")