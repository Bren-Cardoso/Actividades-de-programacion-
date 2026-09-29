x = [5,7,6,4,8,14]
i = 0
contarPar = 0
contarImpar = 0
for i in x:
    y = i%2
    if y == 0:
        contarPar+=1
    else:
        contarImpar+=1
print("La cantidad de numeros impares son:",contarImpar)
print("La cantidad de numeros pares son",contarPar)
