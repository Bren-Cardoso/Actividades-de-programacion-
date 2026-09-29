x = [2,5,9,10,12,16]
ingresar = int(input("Ingrese un número "))
i = 0
j = 0
for i in x:
    if ingresar == i:
        j+=1
if j >= 1:
    print("Su número es igual a la de la lista:", ingresar)
else:
    print("Su número no esta en la lista")
