x = [2,4,2,4,8,8,6]
aux = []
i = 0
while i < len(x):
    j = i+1
    while j < len(x):
        if x[i] == x[j]:
            aux.append(x[i])
        j+=1
    i+=1
print("La lista es:", x)
print("Los números repetidos de la lista son:", aux)
