import random


class mastermind:
    def __init__(self):
        self.fichas = []

    def inicializar(self,lista):
        self.fichas = lista

    def inicializarRandom (self, dificultad):
        if (dificultad.lower() == "facil"):
            for _ in range(4): 
                ficha = random.choice(["rojo","azul","verde","amarillo"])
                while ficha in self.fichas:
                    ficha = random.choice(["rojo","azul","verde","amarillo"])
                self.fichas.append(ficha)
        elif (dificultad.lower() == "medio"):
            for _ in range(4): 
                ficha = random.choice(["rojo","azul","verde","amarillo"])
                self.fichas.append(ficha)
        else:
            for _ in range(4): 
                self.fichas.append(random.choice(["rojo","azul","verde","amarillo","naranja","lila"]))
    
    def chequeo (self,solucion):
        fichas = self.fichas[:]
        pista = ["errado","errado","errado","errado"]
        for i in range (len(solucion)):
            for j in range ( len(fichas) ):
                # print(solucion[i],i,fichas[j],j)
                if solucion[i] == fichas[j] and i == j:
                    pista [i] = "toque"
                    fichas[j] = " "
                    break
        for i in range (len(solucion)):
            for j in range ( len(fichas) ):
                # print(solucion[i],i,fichas[j],j)
                if solucion[i] == fichas[j] and pista[i] != "toque":
                    pista[i] = "roce"
                    fichas[j] = " "
                
        pista.sort()
        return pista
    
    def mostrar(self):
        print(self.fichas)

intentos = 0
juego = mastermind()
juga = int(input("¿De a cuántos jugadores quiere jugar 1 o 2? "))
if juga == 1 :
    dificultad = input("¿Qué dificultad quiere? Fácil, Medio o Difícil?")
    juego.inicializarRandom(dificultad)
    print(juego.mostrar())

elif juga == 2 :
    fichas = input("Escribe los 4 colores (solamente con espacios:3):").split()
    random.choice(fichas)
    juego.inicializar(fichas)


pistas2 = []
while intentos <= 10 or co != juego.fichas:
    intentos = intentos + 1
    co = []
    for q in range(4):
        cor = input("Ingrese uno de los colores :3 ")
        co.append(cor)
    print("")
    print(co)
    print("")
    pistas = juego.chequeo(co)
    pistas2.append(co)
    pistas2.append(pistas)
    print(pistas2)
    print("intentos:", intentos)
    if co == juego.fichas:
        print(" ")
        print("Ganaste :D")
        print("Intentos:", intentos)
        break
    elif intentos > 10:
        print(" ")
        print("Perdiste pipipi")
        print("Intentos", intentos)
        break
    
