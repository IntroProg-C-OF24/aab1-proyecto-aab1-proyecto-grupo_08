import random

def main():
    nIng, nAdiv, intentos, limMay, limMen, maxintentos = 0, 0, 0, 0, 0, 0
    pistas, rango, rules = "", "", ""
    adivino = False

    print("---------------------")
    print("CONFIGURE SU PARTIDA")
    print("---------------------")
    print("-Si desea la configuracion por defecto escriba (CPU)")
    print("-Si desea configurar manualmente su partida escriba (YO)")
    rules = input()

    if rules == "CPU":
        intentos = 10
        pistas = "SI"
        nAdiv = random.randint(1, 100)
        rango = "1 - 100"
    else:
        print("1-INTENTOS")
        print("INGRESE EL NUMERO DE INTENTOS: ")
        intentos = int(input())
        print("2-PISTAS")
        print("-Si quiere recibir pistas sobre el numero secreto escriba (SI)")
        print("-Si no quiere recibir pistas escriba (NO)")
        pistas = input()
        print("3-RANGO")
        print("INGRESE EL LIMITE MAYOR: ")
        limMay = int(input())
        print("INGRESE EL LIMITE MENOR: ")
        limMen = int(input())
        nAdiv = random.randint(limMen, limMay)
        rango = f"{limMen} - {limMay}"

    maxintentos = intentos

    print("--------------------------------------------------")
    print("INICIO DE LA PARTIDA")
    print(f"INTENTOS: {intentos}  -  PISTAS: {pistas}  -  RANGO: {rango}")
    print("--------------------------------------------------")

    if pistas == "SI":
        if nAdiv % 2 == 0:
            print("TEN EN CUENTA QUE EL NUMERO ES PAR")
        else:
            print("TEN EN CUENTA QUE EL NUMERO ES IMPAR")

    print(f"INGRESE UN NUMERO {rango}")

    while intentos >= 1:
        nIng = int(input())
        intentos -= 1

        if nIng == nAdiv:
            adivino = True
            break
        elif intentos >= 1 and pistas == "SI":
            if nAdiv > nIng:
                print("INTENTA CON UNO MAYOR")
            else:
                print("INTENTA CON UNO MENOR")

        print(f"TE QUEDAN: {intentos} intentos")

    if adivino:
        print(f"GANASTE, LO LOGRASTE EN: {maxintentos - intentos} INTENTOS")
    else:
        print("PERDISTE")

if __name__ == "__main__":
    main()
