lista = [100,4,30,29,18,2,10,1]
aux = 0
aux2 = 0
i = 0
while i < (len(lista)-1):
    j = i+1
    while j < len(lista):
        if lista[i] > lista[j]:
            aux = lista[i]
            aux2 = lista[j]
            lista[i] = aux2
            lista[j] = aux
        j+=1
    i+=1
print(lista)
            
