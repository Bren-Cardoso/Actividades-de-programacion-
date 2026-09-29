x = "Messi vuelve a las canchas"
y = x.split(" ")
ult=0
pal=0
i = 0
while (i < len(y)):
    ult = len(y[i])-1
    if (y[i][ult] == "s"):
        pal= y[i]
        y[i]= pal[ :ult]
        i=+1
        print (y[i])
    else:
        pass
print(y)

