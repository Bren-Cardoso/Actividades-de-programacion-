x = [[2,4],[3,8]]
y = [[3,5],[6,2]]
rta = [[0,0],[0,0]]
i = 0
j = 0

for i in range(len(x)):
    rta[i][0] = x[i][0] * y[i][0]
    rta[i][1] = x[i][1] * y[i][1]
print(rta)
