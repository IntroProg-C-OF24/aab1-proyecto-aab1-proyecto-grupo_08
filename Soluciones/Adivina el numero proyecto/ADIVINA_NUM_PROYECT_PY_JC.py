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
    rules = input() #SI EL JUGADOR ELIGE CPU SE AUTOESTABLECEN LAS REGLAS, SI ELIGE YO, LAS ELIGE ESTE MISMO

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
        pistas = input() #SI RESPONDE "SI" SE LE AVISARA AL JUGADOR SI EL NUMERO INGRESADO ES MAYOR O MENOR AL NUMERO SECRETO   
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

    if pistas == "SI": #SI SE ACEPTARON LAS PISTAS, EL JUEGO COMIENZA CON UNA PISTA INICIAL
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
'''
---------------------
CONFIGURE SU PARTIDA
---------------------
-Si desea la configuracion por defecto escriba (CPU)
-Si desea configurar manualmente su partida escriba (YO)
CPU
--------------------------------------------------
INICIO DE LA PARTIDA
INTENTOS: 10  -  PISTAS: SI  -  RANGO: 1 - 100
--------------------------------------------------
TEN EN CUENTA QUE EL NUMERO ES IMPAR
INGRESE UN NUMERO 1 - 100
51
INTENTA CON UNO MAYOR
TE QUEDAN: 9 intentos
75
INTENTA CON UNO MAYOR
TE QUEDAN: 8 intentos
91
INTENTA CON UNO MENOR
TE QUEDAN: 7 intentos
85
INTENTA CON UNO MENOR
TE QUEDAN: 6 intentos
81
GANASTE, LO LOGRASTE EN: 5 INTENTOS


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''