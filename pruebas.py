import pygame
import random

fichasAsignadas = []
posicion = 0
clave = ""
fichaExiste = False

jugador1 = []
jugador2 = []
jugador3 = []
jugador4 = []
jugador1Ganador = 0
jugador2Ganador = 0
jugador3Ganador = 0
jugador4Ganador = 0

class Ficha:
    def __init__(self, valor1, valor2, imagen_path, size=(40, 60)):
        self.valor1 = valor1
        self.valor2 = valor2
        self.imagen_path = imagen_path
        self.size = size
        self.imagen = pygame.image.load(imagen_path)    
        self.imagen = pygame.transform.scale(self.imagen, size)

    def __str__(self):
        return f"({self.valor1}, {self.valor2}, {self.imagen_path})"

# Generacion de fichas
ficha00 = Ficha(0,0,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,0.png')
ficha01 = Ficha(0,1,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,1.png')
ficha02 = Ficha(0,2,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,2.png')
ficha03 = Ficha(0,3,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,3.png')
ficha04 = Ficha(0,4,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,4.png')
ficha05 = Ficha(0,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,5.png')
ficha06 = Ficha(0,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\0,6.png')
ficha11 = Ficha(1,1,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,1.png')
ficha12 = Ficha(1,2,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,2.png')
ficha13 = Ficha(1,3,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,3.png')
ficha14 = Ficha(1,4,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,4.png')
ficha15 = Ficha(1,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,5.png')
ficha16 = Ficha(1,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\1,6.png')
ficha22 = Ficha(2,2,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\2,2.png')
ficha23 = Ficha(2,3,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\2,3.png')
ficha24 = Ficha(2,4,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\2,4.png')
ficha25 = Ficha(2,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\2,5.png')
ficha26 = Ficha(2,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\2,6.png')
ficha33 = Ficha(3,3,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\3,3.png')
ficha34 = Ficha(3,4,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\3,4.png')
ficha35 = Ficha(3,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\3,5.png')
ficha36 = Ficha(3,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\3,6.png')
ficha44 = Ficha(4,4,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\4,4.png')
ficha45 = Ficha(4,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\4,5.png')
ficha46 = Ficha(4,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\4,6.png')
ficha55 = Ficha(5,5,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\5,5.png')
ficha56 = Ficha(5,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\5,6.png')
ficha66 = Ficha(6,6,'C:\\Users\\luiso\\OneDrive\\Escritorio\\domino\\6,6.png')

def asignarFichas(jugador):
    contador = 0
    while contador < 7:
        clave = ""
        fichaExiste = False
        lado1 = random.random()
        if(lado1>0 and lado1<=0.1479):
            clave = "0"
        elif(lado1>0.1479 and lado1<=0.2958):
            clave = "1"
        elif(lado1>0.2958 and lado1<=0.4437):
            clave = "2"
        elif(lado1>0.4437 and lado1<=0.5916):
            clave = "3"
        elif(lado1>0.5916 and lado1<=0.7395):
            clave = "4"
        elif(lado1>0.7395 and lado1<=0.8874):
            clave = "5"
        elif(lado1>0.8874 and lado1<=1):
            clave = "6"

        lado2 = random.random()
        if(lado2>0 and lado2<=0.1479):
            clave = clave+"0"
        elif(lado2>0.1479 and lado2<=0.2958):
            clave = clave+"1"
        elif(lado2>0.2958 and lado2<=0.4437):
            clave = clave+"2"
        elif(lado2>0.4437 and lado2<=0.5916):
            clave = clave+"3"
        elif(lado2>0.5916 and lado2<=0.7395):
            clave = clave+"4"
        elif(lado2>0.7395 and lado2<=0.8874):
            clave = clave+"5"
        elif(lado2>0.8874 and lado2<=1):
            clave = clave+"6"

        claveInversa = clave[1]+clave[0]

        if (len(fichasAsignadas) > 0):
            for j in range(len(fichasAsignadas)):
                if(fichasAsignadas[j] == clave):
                    fichaExiste = True
                    contador = contador-1
                    break
                elif(fichasAsignadas[j] == claveInversa):
                    fichaExiste = True
                    contador = contador-1
                    break

        if(fichaExiste == False):
            fichasAsignadas.append(clave)
            if(clave == "00"):
                jugador.append(ficha00)
            elif(clave == "01" or clave == "10"):
                jugador.append(ficha01)
            elif(clave == "02" or clave == "20"):
                jugador.append(ficha02)
            elif(clave == "03" or clave == "30"):
                jugador.append(ficha03)
            elif(clave == "04" or clave == "40"):
                jugador.append(ficha04)
            elif(clave == "05" or clave == "50"):
                jugador.append(ficha05)
            elif(clave == "06" or clave == "60"):
                jugador.append(ficha06)
            elif(clave == "11"):
                jugador.append(ficha11)
            elif(clave == "12" or clave == "21"):
                jugador.append(ficha12)
            elif(clave == "13" or clave == "31"):
                jugador.append(ficha13)
            elif(clave == "14" or clave == "41"):
                jugador.append(ficha14)
            elif(clave == "15" or clave == "51"):
                jugador.append(ficha15)
            elif(clave == "16" or clave == "61"):
                jugador.append(ficha16)
            elif(clave == "22" or clave == "22"):
                jugador.append(ficha22)
            elif(clave == "23" or clave == "32"):
                jugador.append(ficha23)
            elif(clave == "24" or clave == "42"):
                jugador.append(ficha24)
            elif(clave == "25" or clave == "52"):
                jugador.append(ficha25)
            elif(clave == "26" or clave == "62"):
                jugador.append(ficha26)
            elif(clave == "33"):
                jugador.append(ficha33)
            elif(clave == "34" or clave == "43"):
                jugador.append(ficha34)
            elif(clave == "35" or clave == "53"):
                jugador.append(ficha35)
            elif(clave == "36" or clave == "63"):
                jugador.append(ficha36)
            elif(clave == "44"):
                jugador.append(ficha44)
            elif(clave == "45" or clave == "54"):
                jugador.append(ficha45)
            elif(clave == "46" or clave == "64"):
                jugador.append(ficha46)
            elif(clave == "55"):
                jugador.append(ficha55)
            elif(clave == "56" or clave == "65"):
                jugador.append(ficha56)
            elif(clave == "66"):
                jugador.append(ficha66)
            fichasAsignadas.append(clave)
            fichasAsignadas.append(claveInversa)
        contador = contador+1

displayWidth = 1600 # CAMBIAR
displayHeight = 1000 # CAMBIAR
surface = pygame.display.set_mode((displayWidth, displayHeight))

def mostrar_fichas2(fichas1, fichas2, fichas3, fichas4, fichasTablero):
    pygame.display.set_caption('Fichas')
    surface.fill((255, 255, 255))

    x, y = displayWidth/3, 0
    for ficha in fichas1:
        surface.blit(ficha.imagen, (x, y))
        x += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha
        
    x, y = 1500, 250
    for ficha in fichas2:
        imagen = pygame.transform.rotate(ficha.imagen, 90)
        surface.blit(imagen, (x, y))
        y += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

    x, y = 500, (displayHeight*3)//4
    for ficha in fichas3:
        surface.blit(ficha.imagen, (x, y))
        x -= ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

    x, y = 0, displayHeight//4
    for ficha in fichas4:
        imagen = pygame.transform.rotate(ficha.imagen, 90)
        surface.blit(imagen, (x, y))
        y += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

    x, y = 400, 500
    for ficha in fichasTablero:
        surface.blit(ficha.imagen, (x, y))
        x += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

    pygame.display.update()

def mostrar_fichas(fichas1, fichas2, fichas3, fichas4, fichasTablero):
    ejecucionMetodo = False
    
    pygame.display.init()
    pygame.display.set_caption('Fichas')

    while True:
        surface.fill((255, 255, 255))
        x, y = displayWidth/3, 0
        for ficha in fichas1:
            surface.blit(ficha.imagen, (x, y))
            x += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha
 
        x, y = 1500, 250
        for ficha in fichas2:
            imagen = pygame.transform.rotate(ficha.imagen, 90)
            surface.blit(imagen, (x, y))
            y += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

        x, y = 500, (displayHeight*3)//4
        for ficha in fichas3:
            surface.blit(ficha.imagen, (x, y))
            x += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha

        x, y = 0, displayHeight//4
        for ficha in fichas4:
            imagen = pygame.transform.rotate(ficha.imagen, 90)
            surface.blit(imagen, (x, y))
            y += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha
           
        x, y = 400, 500
        for ficha in fichasTablero:
            surface.blit(ficha.imagen, (x, y))
            x += ficha.size[0]  # Mueve la posición horizontal para la próxima ficha
        pygame.time.wait(100)
        pygame.display.update()

        if ejecucionMetodo == False:
            ejecucionMetodo = True
            juego(fichas1, fichas2, fichas3, fichas4, fichasTablero)

# FICHA PARA PONER DENTRO DEL TABLERO POR JUGADOR  
def colocarFicha(jugador, fichasTablero):
    if len(jugador) != 0:
        for i in range(len(jugador)):
            valoriz = jugador[i].valor1
            valorde = jugador[i].valor2

            if valorde == fichasTablero[0].valor1:   # BIEN
                fichasTablero.insert(0,jugador[i])
                jugador.remove(jugador[i])
                return True
            
            elif valoriz == fichasTablero[len(fichasTablero)-1].valor2: #CAMBIAR o quizas no uwu
                fichasTablero.append(jugador[i])
                jugador.remove(jugador[i])
                return True
            
            elif valoriz == fichasTablero[0].valor1:    # BIEN
                imagen = jugador[i].imagen_path
                ficha1 = Ficha(valorde, valoriz, imagen)
                fichasTablero.insert(0,ficha1)
                jugador.remove(jugador[i])
                return True

            elif valorde == fichasTablero[len(fichasTablero)-1].valor2: #CAMBIAR
                imagen = jugador[i].imagen_path
                ficha1 = Ficha(valorde, valoriz, imagen)
                fichasTablero.append(ficha1)
                jugador.remove(jugador[i])
                return True
            
        return False

def juego(jugador1,jugador2,jugador3,jugador4, fichasTablero):
    #Sabemos el turno inicial
    turno = 0
    contador = 0
    juegoTermina = False
    while contador < 8:
        print(contador)
        print(jugador1[contador])
        if jugador1[contador].valor1 == 6 and jugador1[contador].valor2 == 6:
            print("Jugador 1 empieza")
            fichasTablero.append(jugador1[contador])
            jugador1.remove(jugador1[contador])
            turno = 2
            break
        elif jugador2[contador].valor1 == 6 and jugador2[contador].valor2 == 6:
            print("Jugador 2 empieza")
            fichasTablero.append(jugador2[contador])
            jugador2.remove(jugador2[contador])
            turno = 3
            break
        elif jugador3[contador].valor1 == 6 and jugador3[contador].valor2 == 6:
            print("Jugador 3 empieza")
            fichasTablero.append(jugador3[contador])
            jugador3.remove(jugador3[contador])
            turno = 4
            break
        elif jugador4[contador].valor1 == 6 and jugador4[contador].valor2 == 6:
            print("Jugador 4 empieza")
            fichasTablero.append(jugador4[contador])
            jugador4.remove(jugador4[contador])
            turno = 1
            break
        contador = contador + 1

    for i in range(len(jugador1)):
        print(jugador1[i].valor1, jugador1[i].valor2)
    print()
    for i in range(len(jugador2)):
        print(jugador2[i].valor1, jugador2[i].valor2)
    print()
    for i in range(len(jugador3)):
        print(jugador3[i].valor1, jugador3[i].valor2)
    print()
    for i in range(len(jugador4)):
        print(jugador4[i].valor1, jugador4[i].valor2)
    print()
    for i in range(len(fichasTablero)):
        print(fichasTablero[i].valor1, fichasTablero[i].valor2)

    # HACER QUE EL JUEGO SIGA HASTA QUE ALGUNO SE QUEDE SIN FICHAS
    empate = 0
    while juegoTermina == False:
        if turno == 1:
            print("Turno de jugador 1")
            print("Fichas en el tablero: ",len(fichasTablero))
            print("Fichas en la mano: ",len(jugador1))
            if colocarFicha(jugador1, fichasTablero) == False:
                empate = empate + 1
                if empate == 4:
                    print("Empate")
                    juegoTermina = True
            else:
                empate = 0
            mostrar_fichas2(jugador1, jugador2, jugador3, jugador4, fichasTablero)
            if len(jugador1) == 0:
                print("Jugador 1 gana")
                juegoTermina = True
            else:
                turno = 2
        elif turno == 2:
            print("Turno de jugador 2")
            print("Fichas en el tablero: ",len(fichasTablero))
            print("Fichas en la mano: ",len(jugador2))
            if colocarFicha(jugador2, fichasTablero) == False:
                empate = empate + 1
                if empate == 4:
                    print("Empate")
                    juegoTermina = True
            else:
                empate = 0
            mostrar_fichas2(jugador1, jugador2, jugador3, jugador4, fichasTablero)
            if len(jugador2) == 0:
                print("Jugador 2 gana")
                juegoTermina = True
            else:
                turno = 3
        elif turno == 3:
            print("Turno de jugador 3")
            print("Fichas en el tablero: ",len(fichasTablero))
            print("Fichas en la mano: ",len(jugador3))
            if colocarFicha(jugador3, fichasTablero) == False:
                empate = empate + 1
                if empate == 4:
                    print("Empate")
                    juegoTermina = True
            else:
                empate = 0
            mostrar_fichas2(jugador1, jugador2, jugador3, jugador4, fichasTablero)
            if len(jugador3) == 0:
                print("Jugador 3 gana")
                juegoTermina = True
            else:
                turno = 4
        elif turno == 4:
            print("Turno de jugador 4")
            print("Fichas en el tablero: ",len(fichasTablero))
            print("Fichas en la mano: ",len(jugador4))
            if colocarFicha(jugador4, fichasTablero) == False:
                empate = empate + 1
                if empate == 4:
                    print("Empate")
                    juegoTermina = True
            else:
                empate = 0
            mostrar_fichas2(jugador1, jugador2, jugador3, jugador4, fichasTablero)
            if len(jugador4) == 0:
                print("Jugador 4 gana")
                juegoTermina = True
            else:
                turno = 1
    pygame.display.quit()  # Cerrar la ventana actual
    seguir()
    
def cerrar_y_abrir_ventana():
    #pygame.display.quit()  # Cerrar la ventana actual
    #pygame.display.init()  # Inicializar una nueva ventana
    #ventana = pygame.display.set_mode((displayWidth, displayHeight))  # Crear una nueva ventana
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    fichasTablero = []
    juegoTermina = False
    mostrar_fichas(jugador1, jugador2, jugador3, jugador4, fichasTablero)

#def cerrar_juego():
    #pygame.quit()

def iniciar_siguiente_juego():
    pass

def seguir():
    print("Desea seguir jugando?")
    #cerrar_juego()
    iniciar_siguiente_juego()
    cerrar_y_abrir_ventana()
    
def run():
    # Asignacion de fichas a jugadores
    print("Juego del Domino")
    
    repeticiones = 0
    rep = 0
    while repeticiones < 1:
        repeticiones = int(input("Ingrese el numero de repeticiones: "))

    while rep < repeticiones:
        pygame.init()
        fichasTablero = []
        print("Repeticion: ",rep)
        asignarFichas(jugador1)
        asignarFichas(jugador2)
        asignarFichas(jugador3)
        asignarFichas(jugador4)
        mostrar_fichas(jugador1, jugador2, jugador3, jugador4, fichasTablero)
        #seguir()
    print("Jugador 1 Gano: ",jugador1Ganador)
    print("Jugador 2 Gano: ",jugador2Ganador)
    print("Jugador 3 Gano: ",jugador3Ganador)
    print("Jugador 4 Gano: ",jugador4Ganador)

if __name__ == "__main__":
    run()