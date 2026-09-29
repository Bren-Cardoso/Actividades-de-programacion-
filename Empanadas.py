def presentacion():
    print("¡Bienvenido a la Empanederia!")
    print("Nuestro menú cuenta con una variedad de relleno que le pasaremos a continuación")
    print("Si usted quiere envio, tiene un costo adicional de $500")
    print(" ")
    print("Menú:")
    print("Opcion 1 -> Empanada de Carne $900")
    print("Opcion 2 -> Empanada de Jamon y Queso $700")
    print("Opcion 3 -> Empanada de Arabe $1000")
    print("Opcion 4 -> Empanada de Carne Dulce $500")
    print(" ")
    
def ticket(comanda):
    print(" ___________________________________________________________ ")
    print("|            ---------- TICKET ----------                   |")
    print("  ► Nombre:                   ", comanda.nombre)
    print("|                                                           |")
    print("  ► Tipo de empanada:          Empanada de", comanda.relleno)
    print("|                                                           |")
    print("  ► Cantidad:                 ", comanda.cantidad)
    print("|                                                           |")
    print("  ► Envio:                    ", comanda.envio)
    print("|                                                           |")
    print("  ► Direccion:                ", comanda.direccion)
    print("|                                                           |")
    print("  ► Descuento                ", descuento)
    print("|___________________________________________________________|")
    print("|                                                           |")
    print("  TOTAL:                      ", comanda.precio, )
    print("|___________________________________________________________|")
    print("|                                                           |")
    print("|             ║|║║║|║║║║║║║|║║║║|║║║║|║║║|║║║|║             |")
    print("|             ║|║║║|║║║║║║║|║║║║|║║║║|║║║|║║║|║             |")
    print("|___________________________________________________________|")
    print(" ")


carne = 0
jamonyqueso = 0
arabe = 0
dulce = 0
delivery = 500
descuento = 0
ganacia = 0

class comandaEmp:
    def __init__(self, relleno, cantidad, precio, nombre, envio, direccion):
        self.relleno = relleno
        self.cantidad = cantidad
        self.precio = precio
        self.nombre = nombre
        self.envio = envio
        self.direccion = direccion
        
presentacion()

comanda1 = comandaEmp(
    nombre = input("Ingrese su nombre por favor "),
    relleno = input("¿Que relleno desea elegir? "),
    cantidad = int(input("¿Que cantidad de empanadas quiere? ")),
    envio = input("¿Quiere un envio de su pedido?  si/no "),
    precio = 0,
    direccion = ""
    )

if comanda1.relleno.isnumeric or comanda.relleno1.isalum():
    print("Su relleno no es valido")
    comanda1.relleno = input("¿Que relleno desea elegir? ")
if comanda1.cantidad <= 0:
    print("Su cantidad no es valida")
    comanda1.cantidad = int(input("¿Que cantidad de empanadas quiere? "))

if comanda1.relleno == "carne" or "Carne":
    carne = 900
    comanda1.precio = carne * comanda1.cantidad
elif comanda1.relleno == "jamon y queso" or "Jamon y queso" or "Jamón y queso" or "jamón y queso" or "Jamon y Queso" or "Jamón y Queso":
    jamonyqueso = 700
    comanda1.precio = jamonyqueso * comanda1.cantidad
elif comanda1.relleno == "arabe" or "Arabe" or "Árabe":
    arabe = 1000
    comanda1.precio = arabe * comanda1.cantidad
elif comanda1.relleno == "carne dulce" or "Carne dulce" or "Carne Dulce":
    dulce = 500
    comanda1.precio = dulce * comanda1.cantidad
else:
    pass
    
if comanda1.cantidad >= 12 :
    descuento = (comanda1.precio * 20)/100
    comanda1.precio = comanda1.precio - descuento
else:
    descuento = 0

if comanda1.envio == "si":
    comanda1.direccion = input("Ingrese su direccion por favor ")
    comanda1.precio = comanda1.precio + delivery
else:
    print(" ")
    print("Gracias por su atencion, en dentro de poco su pedido estará listo")

ticket(comanda1)
print(" ")

presentacion()

comanda2 = comandaEmp(
    nombre = input("Ingrese su nombre por favor "),
    relleno = input("¿Que relleno desea elegir? "),
    cantidad = int(input("¿Que cantidad de empanadas quiere? ")),
    envio = input("¿Quiere un envio de su pedido?  si/no "),
    precio = 0,
    direccion = ""
    )

if comanda2.relleno.isnumeric or comanda.relleno2.isalum():
    print(" ")
    print("Su relleno no es valido")
    comanda2.relleno = input("¿Que relleno desea elegir? "),
if comanda2.cantidad <= 0:
    print(" ")
    print("Su cantidad no es valida")
    comanda1.cantidad = int(input("¿Que cantidad de empanadas quiere? "))
    
if comanda2.relleno == "carne" or "Carne":
    carne = 900
    comanda2.precio = carne * comanda2.cantidad
elif comanda2.relleno == "jamon y queso" or "Jamon y queso" or "Jamón y queso" or "jamón y queso" or "Jamon y Queso" or "Jamón y Queso":
    jamonyqueso = 700
    comanda2.precio = jamonyqueso * comanda2.cantidad
elif comanda2.relleno == "arabe" or "Arabe" or "Árabe":
    arabe = 1000
    comanda2.precio = arabe * comanda2.cantidad
elif comanda2.relleno == "carne dulce" or "Carne dulce" or "Carne Dulce":
    dulce = 500
    comanda2.precio = dulce * comanda2.cantidad
else:
    pass

if comanda2.cantidad >= 12 :
    descuento = (comanda2.precio * 20)/100
    comanda2.precio = comanda2.precio - descuento
else:
    pass
   
if comanda2.envio == "si":
    comanda2.direccion = input("Ingrese su direccion por favor ")
    comanda2.precio = comanda2.precio + delivery
else:
    print(" ")
    print("Gracias por su atencion, en dentro de poco su pedido estará listo")
    print(" ")

if comanda1.nombre == comanda2.nombre:
    descuento = (comanda2.precio * 50)/100
    comanda2.precio = comanda2.precio - descuento

ticket(comanda2)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

ganancia = comanda1.precio + comanda2.precio
print(" ___________________________________________________________ ")
print("|              ---------- GANANCIA ----------               |")
print("  ► Orden 1:                   ", comanda1.precio)
print("|                                                           |")
print("  ► Orden 2:                   ", comanda2.precio)
print("|___________________________________________________________|")
print("|                                                           |")
print("  TOTAL:                      ", ganancia , )
print("|___________________________________________________________|")
