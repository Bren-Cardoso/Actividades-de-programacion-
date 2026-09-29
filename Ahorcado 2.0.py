import string, random
def colgado (error):
    if error == 1:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|")  
        print("|")  
        print("|")
        print("=====")
    elif error == 2:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|     |")  
        print("|")  
        print("|")
        print("=====")
    elif error == 3:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|    /|")  
        print("|")  
        print("|")
        print("=====")
    elif error == 4:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|    /|\\")  
        print("|")  
        print("|")
        print("=====")
    elif error == 5:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|    /|\\")  
        print("|    /")  
        print("|")
        print("=====")
    elif error == 6:
        print(" ___")
        print("|     |")
        print("|     o")
        print("|    /|\\")  
        print("|    / \\")  
        print("|")
        print("=====")
        print("Perdiste :(")
        print("La palabra era:" ,pSecreta)
   
error = 0
print ("¡Bienvenido al ahorcado :D!")
print(" _____")
print("|     |")
print("|")
print("|")
print("|")
print("|")
print("=====")

palabra =["hipopotomonstrosesquipedaliofobia","electroencefalografista","esternocleidomastoideo","otorrinolaringólogo","hola","ornitorrinco","pizzaron","crayon","mar","playa","colegio","denuncia","fotosintéticamente","hoja","mesada","pileta"]
pSecreta = random.choice(palabra)
nro = len(pSecreta)
guion = "_"
g = []
x = []
g = list(guion * nro)

while (error <6 and "_" in g):
    letra = input("ingrese una letra ")
    i = 0
    for i in range (len(pSecreta)) :   #ingresa letra en los guiones
        if letra == pSecreta[i]:
            g[i] = letra

    if letra not in pSecreta: #le va sumando al error y hace el dibujito
        error+=1
        print("Letra incorrecta")
        colgado(error)
    else:
        pass
    print(g)


if (g == list(pSecreta)):
    print("¡Ganaste :3!")
else:
    print("Perdiste :(")
