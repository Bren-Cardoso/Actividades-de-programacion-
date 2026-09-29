contraseña = input("Ingrese una contraseña ")
contra = len(contraseña)
x = list(contraseña)
cantNum = 0
cantSim = 0
simboloResta = 0
cantMay = 0
cantMin = 0
for i in x:
    if i.isdigit():
        cantNum+=1
    if i.isalnum():
        cantSim+=1
        simboloResta = contra - cantSim
    if i.isupper():
        cantMay+=1
    if i.islower():
        cantMin+=1

if cantNum<1 or simboloResta<1 or cantMay<2 or cantMin<2:
    print("Su contraseña tiene que tener por lo menos un número ")
    print("Su contraseña tiene que tener por lo menos un símbolo")
    print("Su contraseña tiene que tener por lo menos dos letras mayúsculas")
    print("Su contraseña tiene que tener por lo menos dos letras minúsculas")
    print("Todo mal con tu contraseña >~<")
else:
    print("Que capo que sos :p")
    
