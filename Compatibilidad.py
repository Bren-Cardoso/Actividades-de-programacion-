import random
class compa: 
    def __init__(self, nombre, edad, altura, signo, colorp, subcultura):
         self.nombre = nombre,
         self.edad = edad,
         self.altura = altura,
         self.signo = signo,
         self.colorp = colorp,
         self.subcultura = subcultura,

puntos =  0

puntos = random.randint (0,25)    #puntos random

print ("Ingrese los datos del HOMBRE")

hombre = compa (
    input("Ingrese el primer nombre ").lower(),
    int( input("Ingrese la primera edad ")),
    int( input("Ingrese la primer altura (en cm) ")),
    input("Ingrese el primer signo ").lower(),
    input("Ingrese el primer color de pelo ").lower(),
    input("Ingrese la primer subculura ").lower()
    )

print(" ")
print("Ingrese los datos de la MUJER")

mujer = compa (
    input("Ingrese el segundo nombre ").lower(),
    int(input("Ingrese la segunda edad ")),
    int(input("Ingrese la segunda altura (en cm) ")),
    input("Ingrese el segundo signo ").lower(),
    input("Ingrese el segundo color de pelo ").lower(),
    input("Ingrese la segunda subculura ").lower()
    )

#EDAD

edadmax  = hombre.edad[0] - mujer.edad[0]        

if edadmax == 3:
    puntos += 10

elif edadmax <3 or edadmax == 0:
    puntos += 5
    
elif edadmax >3:
    puntos +=2
    
elif edadmax > 10:
    puntos -= 5

elif hombre.edad[0] < mujer.edad[0] :
    puntos -=2
    
else:
    pass

#ALTURA

alturamax = hombre.altura[0] - mujer.altura[0]    
if alturamax == 20:
    puntos += 10
    
elif alturamax == 15 or alturamax == 10:
    puntos += 5
    
elif alturamax == 0:
    puntos += 2

elif hombre.altura[0] < mujer.altura[0] :
    puntos -=2

else:
    pass

#SIGNOS

elementos1 = " "     
elementos2 = " "

#elementos hombre

if hombre.signo[0] == "capricornio" or hombre.signo[0] == "virgo" or hombre.signo[0] == "tauro":
    elementos1 = "tierra"

elif hombre.signo[0] == "picsis" or hombre.signo[0] == "cancer" or hombre.signo[0] == "escorpio":
    elementos1 = "agua"

elif hombre.signo[0] == "aries" or hombre.signo[0] == "leo" or hombre.signo[0] == "sagitario":
    elementos1 = "fuego"

elif hombre.signo[0] == "capricornio" or hombre.signo[0] == "virgo" or hombre.signo[0] == "tauro":
    elementos1 = "tierra"

#elementos mujer

if mujer.signo[0] == "capricornio" or mujer.signo[0] == "virgo" or mujer.signo[0] == "tauro":
    elementos2 = "tierra"

elif mujer.signo[0] == "picsis" or mujer.signo[0] == "cancer" or mujer.signo[0] == "escorpio":
    elementos2 = "agua"

elif mujer.signo[0] == "aries" or mujer.signo[0] == "leo" or mujer.signo[0] == "sagitario":
    elementos2 = "fuego"

elif mujer.signo[0] == "capricornio" or mujer.signo[0] == "virgo" or mujer.signo[0] == "tauro":
    elementos2 = "aire"

else:
    pass

if elementos1 == "tierra" and elementos2 == "agua":
    puntos += 10

elif elementos1 == "agua" and elementos2 == "tierra":
    puntos += 10

elif elementos1 == "fuego" and elementos2 == "aire":
    puntos += 10
    
elif elementos1 == "aire" and elementos2 == "fuego":
    puntos += 10

else:
    puntos += 5

#NOMBRE
    
nombre1 = hombre.nombre[0]   
nombre2 = mujer.nombre[0]
 
nombres = []
puntosT = []
 
if nombre2 < nombre1:
  nombres = nombre1 + nombre2
else:
  nombres = nombre2 + nombre1
 
for letra in nombres:
  puntosletra = nombres.count(letra)
  if puntosletra != 0:
    puntosT.append(puntosletra)
  nombres = nombres.replace(letra, "")
 
puntosR = []
 
while len(puntosT) > 2:
  for i in range((len(puntosT)//2)):
    puntosR.append(puntosT[i] + puntosT[len(puntosT)-i-1])
  if len(puntosT) % 2 != 0:
    puntosR.append(puntosT[(len(puntosT)//2)+1])
  puntosT = puntosR
  puntosR = []
 
puntosT = puntosT[0] + puntosT[1]*0.1
puntos += int(puntosT)

#COLOR DE PELO

##rubio
if hombre.colorp[0] == "rubio" and mujer.colorp[0] == "morocha":
    puntos += 10

elif hombre.colorp[0] == "rubio" and mujer.colorp[0] == "rubia":
    puntos += 8

elif hombre.colorp[0] == "rubio" and mujer.colorp[0] == "castaña":
    puntos += 10

##morocho

if hombre.colorp[0] == "morocho" and mujer.colorp[0] == "rubia":
    puntos += 8

elif hombre.colorp[0] == "morocho" and mujer.colorp[0] == "morocha":
    puntos += 10

elif hombre.colorp[0] == "morocho" and mujer.colorp[0] == "castaña":
    puntos += 7

##castaño

if hombre.colorp[0] == "castaño" and mujer.colorp[0] == "rubia":
    puntos += 9

elif hombre.colorp[0] == "castaño" and mujer.colorp[0] == "morocha":
    puntos += 6

elif hombre.colorp[0] == "castaño" and mujer.colorp[0] == "castaña":
    puntos += 9

#SUBCULTURA

##tincho
if hombre.subcultura[0] == "tincho" and mujer.subcultura[0] == "mili":
    puntos += 10

elif hombre.subcultura[0] == "tincho" and mujer.subcultura[0] == "turra":
    puntos += 2

elif hombre.subcultura[0] == "tincho" and mujer.subcultura[0] == "nerd":
    puntos += 6

##turro

if hombre.subcultura[0] == "turro" and mujer.subcultura[0] == "mili":
    puntos += 8

elif hombre.subcultura[0] == "turro" and mujer.subcultura[0] == "turra":
    puntos += 7

elif hombre.subcultura[0] == "turro" and mujer.subcultura[0] == "nerd":
    puntos += 4

##nerd

if hombre.subcultura[0] == "nerd" and mujer.subcultura[0] == "mili":
    puntos += 8

elif hombre.subcultura[0] == "nerd" and mujer.subcultura[0] == "turra":
    puntos -= 2

elif hombre.subcultura[0] == "nerd" and mujer.subcultura[0] == "nerd":
    puntos += 7

print("Su compatibilidad es de: ", puntos, "%")
