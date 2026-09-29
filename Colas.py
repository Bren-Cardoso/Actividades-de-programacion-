def presentacion():
    print("1- Cargar Pedido")
    print("2- Mostrar Pedido siguiente")
    print("3- Procesar Pedido")
    print("4- Detalle del ingreso parcial")
    print("5- Salir")
    print(" ")
    input("Ingrese el número de la cción que quiere realizar ")

class Cola:
    def __init__(self,tamanio):
        self.tamanio = tamanio
        self.lista = []

    def es_vacia(self):
        return len(self.lista) == 0
        #retorna verdadero si es vacía

    def encolar(self, x):
        if len(self.lista) < self.tamanio:
            self.lista.insert(0,x)
        else:
            print("cola llena bro")
        #si no está llena, ingresa el elemento x al final de la lista

    def consultar(self):
        if not (self.es_vacia()):
            return self.lista[0]
        else:
            print("cola vacía bro")
        #si no está vacía, retorna el elemento que esta al comienzo de la lista

    def desencolar(self):
        if not (self.es_vacia()):
            self.lista = self.lista[1:]
        else:
            print("cola vacía bro")
         #si no está vacía, elimina el elemento al inicio de la lista

    def es_llena(self):
        return len(self.lista) == self.tamanio
    #retorna verdadero si el tamaño de la lista es igual al tamaño de la pila

presentacion()
    
class Pedido:
    def __init__ (self, descripcion, apellido, envio, monto):
        self.descripcion = descripcion
        self.apellido = apellido
        self.envio = envio
        self.monto = monto

test = Cola(5)

test.encolar(3)

ganancias = 0

if presentacion == 1:
    cargar_pedido = Pedido(
        descripcion = input("Ingrese la descripción de su pedido: "),
        apellido = input("Ingrese su apellido: "),
        envio = input("¿Desea envio? "),
        monto = input("Ingrese el monto del pedido: ")
        )
    if envio == "Si":
        envio = 0
    else:
        envio = 1
        
elif presentacion == 4:
    print(ganancias)

elif presentacion == 5:
    exit


    
print(test.consultar())
test.desencolar()
print (test.es_vacia())
print(test.es_llena())
test.encolar(3)
test.encolar(3)
test.encolar(3)
test.encolar(3)
test.encolar(3)
test.encolar(3)

print(test.es_llena())
