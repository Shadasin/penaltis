import random

#Información sobre el programa
print("LANZADOR DE PENALTIS")

#Declaración e inicialización de variables
continuar = 1
posicion = 0
goles = 0
golesuno = 0
golesdos = 0
n = 1
numjugadores = 0
usuario = ""
usuariouno = ""
usuariodos = ""

#Función para preguntar cuántas personas van a jugar
def cuantosjug():
    global numjugadores
    numjugadores = int (input("¿Cuántas personas van a jugar? (1 o 2) "))

#Función para el modo de un jugador
def penaltiunjugador ():
        global goles
        global n
        print (f"Ronda {n}")
        posicion = int(input ("¿Dónde deseas lanzar el penalti? 1=Centro 2=Derecha rasa 3=Izquierda rasa 4=Derecha por la escuadra 5=Izquierda por la escuadra 6=Palo 7=Fuera "))
        if posicion != random.randint (1,5) and posicion != 6 and posicion !=7:
            goles += 1
            print(f"GOOOOOOOL. Ya llevas {goles} gol(es).")
        else:
            print(f"Has fallado. Llevas {goles} gol(es).")
        n += 1

#Función para decidir el ganador
def decidirganador(golesuno,golesdos):
    if (golesuno > golesdos):
        print("¡Ha ganado el J1!")
        input("")
    elif (golesdos > golesuno):
        print("¡Ha ganado el J2!")
        input("")
    else:
        print("¡Empate!")
        input("")
    
#Función para el modo de dos jugadores
def penaltidosjugadores ():
        global golesuno, golesdos
        global n
        print (f"Ronda {n}, turno de {usuariouno}")
        posicion = int(input ("¿Dónde deseas lanzar el penalti? 1=Centro 2=Derecha rasa 3=Izquierda rasa 4=Derecha por la escuadra 5=Izquierda por la escuadra 6=Palo 7=Fuera "))
        if posicion != random.randint (1,5) and posicion != 6 and posicion !=7:
            golesuno += 1
            print(f"GOOOOOOOL. Ya llevas {golesuno} gol(es).")
        else:
            print(f"Has fallado. Llevas {golesuno} gol(es).")
        print (f"Ronda {n}, turno de {usuariodos}")
        posicion = int(input ("¿Dónde deseas lanzar el penalti? 1=Centro 2=Derecha rasa 3=Izquierda rasa 4=Derecha por la escuadra 5=Izquierda por la escuadra 6=Palo 7=Fuera "))
        if posicion != random.randint (1,5) and posicion != 6 and posicion !=7:
            golesdos += 1
            print(f"GOOOOOOOL. Ya llevas {golesdos} gol(es).")
        else:
            print(f"Has fallado. Llevas {golesdos} gol(es).")
        n += 1

#Ejecución del programa
cuantosjug()
#Funcionamiento del modo singleplayer
if (numjugadores == 1):
    usuario = input ("Introduce tu nombre: ")
    while continuar == 1:
        penaltiunjugador ()
        continuar = int(input ("¿Deseas continuar? 1: Sí 2: No "))
    #Salida por pantalla de los resultados
    print(f"PUNTUACIONES:\n {usuario}:\n\tGOLES:{goles}\n\tTASA DE ACIERTOS: {goles*100/(n-1)}%")
    input("")
#Funcionamiento del modo multiplayer
if (numjugadores == 2):
    usuariouno = input ("Introduce el nombre del J1: ")
    usuariodos = input ("Introduce el nombre del J2: ")
    while continuar == 1:
        penaltidosjugadores ()
        continuar = int(input ("¿Deseas continuar? 1: Sí 2: No "))
    #Salida por pantalla de los resultados de ambos jugadores
    print(f"PUNTUACIONES:\n {usuariouno}:\n\tGOLES:{golesuno}\n\tTASA DE ACIERTOS: {golesuno*100/(n-1)}%")
    print(f"{usuariodos}:\n\tGOLES:{golesdos}\n\tTASA DE ACIERTOS: {golesdos*100/(n-1)}%")
    decidirganador(golesuno, golesdos)
    input("")