import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciar_trivia = True
intento = 0
puntaje = random.randint(1, 11)
puntaje_secreto = False
vali = True
total = 0
historialPregunta = []
historialPuntos = []

print(BLUE + "Bienvenido al Trivia sobre Música" + RESET)
nombre = input("\nIngrese nombre: ")

#Instrucciones

print(
    BLUE + "\nHOLA", nombre, "!!" + RESET +
    "\n\nAntes de iniciar no olvides seguir estas instrucciones:\n■ Escribe la letra de de la alternativa que consideres correcta.\n■ Presiona 'Enter' para enviar tu respuesta."
)

#Confirmacion

print(
    BLUE + "\nRECUERDA:" + RESET +
    "\n\n■ Cada pregunta vale 10 puntos.\n■ Comenzarás con", puntaje,
    "puntos solo en el primer intento\n■ Los secretos dan puntos...")

conf = input("\n¿Estas listo?\nResponde " + RED + "si/no: " + RESET)
conf = conf.upper()

while conf not in {"SI", "NO"}:
    conf = input(RED + "\nError: Valor incorrecto, ingrese nuevamente: " +
                 RESET)
    conf = conf.upper()

if conf == "SI":
    #Pregunta 1
    
  
    for x in range(5, -1, -1):
        if x == 0:
            print("\n Vamos!!" + RESET)
        else:
            print("\n", YELLOW, x)
        time.sleep(1)

    while iniciar_trivia == True:
        historialPregunta.append("Puntos extra")
        historialPuntos.append(puntaje)
        intento += 1

        print(MAGENTA + "\nNumero de intentos:", intento, RESET)
        print(YELLOW + "\nPUNTAJE ACTUAL:", puntaje, "" + RESET)
        print(
            BLUE + "\nPregunta 1:" + GREEN +
            "\n\nA que cantante(s) pertenece el siguiente coro: 'Hoy se cumple un mes que ya no me ves, te fuiste nada más, quisiste renunciar a quererme y cómo dueles…'"
            + RESET +
            "\n\nA)	Jesse & Joy\nB)	Vicentico\nC)	Stratovarius\nD)	Andrés Calamaro"
        )

        #validación

        while vali:
            rp1 = input("\nRespuesta: ").upper()

            if rp1 not in {"A", "B", "C", "D", "X"}:
                print(RED + "\nError: Solo a, b, c, d para responder." + RESET)
                vali = True

            elif rp1 == 'X':
                print(MAGENTA + "\nPISTA SECRETA ACTIVADA: Son hermanos!!" +
                      RESET)
                vali = True
                puntaje_secreto = True

            elif rp1 == 'A':
                print(BLUE + "\n■ Respuesta Correcta!!" + RESET)
                if puntaje_secreto == True:
                    print(
                        GREEN +
                        "\n+ 1000 puntos por acertar con la pista secreta!!" +
                        RESET)
                    puntaje = puntaje + 1000
                    historialPuntos.append(1000)
                    puntaje_secreto = False
                else:
                    puntaje += 10
                    historialPuntos.append(10)

                historialPregunta.append(rp1)

                vali = False

            else:
                print(RED + "\n■ Respuesta Incorrecta :(" + RESET)
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp1)
                historialPuntos.append(0)

        print(YELLOW + "\nPUNTAJE ACTUAL:", puntaje, "" + RESET)
        time.sleep(2)

        #Pregunta 2

        print(BLUE + "\nPregunta 2:" + GREEN +
              "\n\nA qué banda peruana le pertence el tema: 'Ojos de ángel'." +
              RESET +
              "\n\nA)	Amén\nB)	Cementerio Club\nC)	Arena Hash\nD)	Libido")

        #Validación
        vali = True

        while vali:
            rp2 = input("\nRespuesta: ").upper()

            if rp2 not in {"A", "B", "C", "D", "X"}:
                print(RED + "\nError: Solo a, b, c, d para responder." + RESET)
                vali = True

            elif rp2 == 'X':
                print(
                    MAGENTA +
                    "\nPISTA SECRETA ACTIVADA: El nombre tiene seis caracteres!!"
                    + RESET)
                vali = True
                puntaje_secreto = True

            elif rp2 == 'D':
                print(BLUE + "\n■ Respuesta Correcta!!" + RESET)
                if puntaje_secreto == True:
                    print(
                        GREEN +
                        "\n+ 1000 puntos por acertar con la pista secreta!!" +
                        RESET)
                    puntaje += 1000
                    puntaje_secreto = False
                    historialPuntos.append(1000)
                else:
                    puntaje += 10
                    historialPuntos.append(10)
                  
                vali = False
                historialPregunta.append(rp2)
                

            else:
                print(RED + "\n■ Respuesta Incorrecta :(" + RESET)
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp2)
                historialPuntos.append(0)

        print(YELLOW + "\nPUNTAJE ACTUAL:", puntaje, "" + RESET)
        time.sleep(2)

        #Pregunta 3

        print(
            BLUE + "\nPregunta 3:" + GREEN +
            "\n\nSolo una banda es peruana: " + RESET +
            "\n\nA)	Enanitos Verdes\nB)	Los saicos\nC)	Los Prisioneros\nD)	Sui Generis"
        )

        #Validación
        vali = True

        while vali:
            rp3 = input("\nRespuesta: ").upper()

            if rp3 not in {"A", "B", "C", "D", "X"}:
                print(RED + "\nError: Solo a, b, c, d para responder." + RESET)
                vali = True

            elif rp3 == 'X':
                print(MAGENTA +
                      "\nPISTA SECRETA ACTIVADA: Se llamaron Los Sádicos" +
                      RESET)
                print(puntaje_secreto)
                puntaje_secreto = True
                vali = True

            elif rp3 == 'A':
                print(
                    RED +
                    "\n■ Incorrecto! Enanitos Verdes es una banda argentina." +
                    RESET)
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp3)
                historialPuntos.append(0)

            elif rp3 == 'C':
                print(RED +
                      "\n■ Incorrecto! Los Prisioneros es una banda chilena." +
                      RESET)
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp3)
                historialPuntos.append(0)

            elif rp3 == 'D':
                print(RED +
                      "\n■ Incorrecto! Sui Generis es una banda argentina." +
                      RESET)
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp3)
                historialPuntos.append(0)

            else:
                if puntaje_secreto == True:
                    print(
                        GREEN +
                        "\n+ 1000 puntos por acertar con la pista secreta!!" +
                        RESET)
                    puntaje += 1000
                    puntaje_secreto = False
                    historialPuntos.append(1000)
                else:
                    print(BLUE + "\n■ Respuesta Correcta!!" + RESET)
                    puntaje += 10
                    historialPuntos.append(10)
                  
                vali = False
                historialPregunta.append(rp3)
                

        print(YELLOW + "\nPUNTAJE ACTUAL:", puntaje, "" + RESET)
        time.sleep(2)

        #Pregunta 4

        print(
            BLUE + "\nPregunta 4:" + GREEN +
            "\n\nEl dia internacional de la música es el: " + RESET +
            "\n\nA)	20 de marzo\nB)	21 de noviembre\nC)	22 de noviembre\nD)	32 de noviembre"
        )

        #Validación
        vali = True

        while vali:
            rp4 = input("\nRespuesta: ").upper()

            if rp4 not in {"A", "B", "C", "D", "X"}:
                print(RED + "\nError: Solo a, b, c, d para responder." + RESET)
                vali = True

            elif rp4 == 'X':
                print(MAGENTA + "\nPISTA SECRETA ACTIVADA: Es en noviembre!!" +
                      RESET)
                puntaje_secreto = True
                vali = True

            elif rp4 == 'A':
                print(RED + "\n■ Incorrecto! -5 puntos" + RESET)
                puntaje = puntaje - 5
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp4)
                historialPuntos.append("-5")

            elif rp4 == 'B':
                print(RED + "\n■ Casi correcto! +5 puntos" + RESET)
                puntaje = puntaje + 5
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp4)
                historialPuntos.append("+5")

            elif rp4 == 'D':
                print(
                    RED +
                    "\n■ No existe la fecha 32 en noviembre! Tu puntaje total se divide entre 2"
                    + RESET)
                puntaje = puntaje / 2
                vali = False
                puntaje_secreto = False
                historialPregunta.append(rp4)
                historialPuntos.append("/2")

            else:
                if puntaje_secreto == True:
                    print(
                        GREEN +
                        "\n+ 1000 puntos por acertar con la pista secreta!!" +
                        RESET)
                    puntaje += 1000
                    puntaje_secreto = False
                    historialPuntos.append("1000")
                else:
                    print(BLUE +
                      "\n■ Respuesta Correcta, Tu puntaje se duplica!!" +
                      RESET)
                    puntaje = puntaje * 2
                    historialPuntos.append("x2")
                vali = False
                historialPregunta.append(rp4)
                

        time.sleep(2)

        #Salida

        print("\n==================================")
        if puntaje > 40:
            print(
                YELLOW + "Alcanzaste", puntaje,
                "puntos de 40 O_o\nVeo que descubriste la pista secreta :)"
                + RESET)
        else:
            print(YELLOW + "Alcanzaste", puntaje, "puntos de 40 ■_■" + RESET)
            print("==================================")

            #Ruleta
            ruleta = input(
                BLUE +
                "\nQuieres probar tu suerte?, podras aumentar tus puntos!!" +
                RESET + "\nResponde " + RED + "si/no: " + RESET).upper()

            while (ruleta not in {"SI", "NO"}):
                ruleta = input(RED + "\nIngrese un valor correcto: " +
                               RESET).upper()

            if (ruleta == "SI"):
                for x in range(random.randint(1, 10), random.randint(10, 30),
                               +1):
                    total = total + x

            print("\n==================================")
            if total > 40:
                print(
                    GREEN + "Haz ganado", total,
                    "puntos, tu suerte rompió los limites!! O_o\n" + BLUE +
                    "Puntaje Total:", (total + puntaje), RESET)
            else:
                print(GREEN + "Haz ganado", total,
                      "puntos\n" + BLUE + "Puntaje Total:", (total + puntaje),
                      RESET)
        print("==================================")

        #reiniciar trivia

        print(BLUE + "\n¿Deseas intentar nuevamente la Trivia?" + RESET)

        repetir_trivia = input("Responder " + RED + "si/no: " + RESET).upper()

        while (repetir_trivia not in {"SI", "NO"}):
            repetir_trivia = input(RED + "\nIngrese un valor correcto: " +
                                   RESET).upper()

        if repetir_trivia != "SI":
            print(GREEN + "\nGracias por jugar!!, hasta otra oportunidad",
                  nombre, ":)" + RESET)
            iniciar_trivia = False

            time.sleep(2)

            print("\n==================================")
            print(RED+"Historial\n")
            for x in range(0, 5):
                if x == 0:
                  print(BLUE+historialPregunta[x]+":"+RESET,historialPuntos[x])
                else:
                  print(BLUE+"\nPregunta:",RESET,x,BLUE,
                      "\nAlternativa:",RESET,historialPregunta[x],BLUE,"\nPuntos:",RESET,
                      historialPuntos[x])
            print("==================================")
          
        vali = True
        total = 0
        puntaje = 0
        historialPuntos = []
        historialPregunta = []

else:
    print(GREEN + "\nAdiós!!, hasta otra oportunidad", nombre, ":)" + RESET)
