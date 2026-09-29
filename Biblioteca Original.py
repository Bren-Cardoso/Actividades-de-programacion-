class Libro: #clase Ámbar y Nico original
    def __init__(self,titulo,autor,editorial,genero,añop,disponibilidad):
         self.titulo = titulo
         self.autor = autor
         self.editorial = editorial
         self.genero = genero
         self.añop  = añop
         self.disponibilidad = disponibilidad
         
    def ticket(self):
        print("- - - - - - - - - - - - - - - - - - - - ")
        print("|                                      |")
        print("  Titulo:",self.titulo)
        print("|                                      |")
        print("  Autor:",self.autor)
        print("|                                      |")
        print("  Editorial:",self.editorial)
        print("|                                      |")
        print("  Genero:",self.genero)
        print("|                                      |")
        print("  Año de Publicacion:",self.añop)
        print("|                                      |")
        print("  Disponibilidad:",self.disponibilidad)
        print("|                                      |")
        print("- - - - - - - - - - - - - - - - - - - - ")
    def prestar(self):
            self.disponibilidad = "no"
            
    def devuelto(self):
            self.disponibilidad = "si"
            
    def antiguedad(self):
        año = 2024-self.añop

biblioteca = []
opcion  = 0
while  opcion != 11:
    print("Bienvenido al sistema de gestión de biblioteca:")
    print("1. Cargar un libro")
    print("2. Modificar un libro")
    print("3. Eliminar un libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Listar todos los libros")
    print("7. Listar libros prestados")
    print("8. Listar libros disponibles")
    print("9. Listar libros por género")
    print("10. Listar libros modernos")
    print("11. Salir")
    opcion = int(input("Ingrese el número de opción que desea ejecutar: "))

    if opcion == 1 :                                       #OPCION 1
        libro1 = Libro(
        input("Ingrese el titulo"),
        input("Ingrese el autor"),
        input("Ingrese la editorial"),
        input("Ingrese el genero"),
        int(input("Ingrese el año de publicacion")),
        input("Ingrese disponibilidad si/no")
        )
        if libro1.añop > 2024 or libro1.añop < 0:
            print("ERROR: Su fecha no es valida")
            libro1.añop=int(input("Ingrese el año de publicacion nuevamente"))
        else:
            pass
        biblioteca.append(libro1)
        libro1.ticket()
        
    if opcion == 2:                                     #OPCION 2
        opcion2 = 0
        while  opcion2 != 7:
            print("1. Titulo ")
            print("2. Autor")
            print("3. Editorial ")
            print("4. Género")
            print("5. Año de publicación")
            print("6. Disponibilidad")
            print("7. Nada, me confundi de opción D:")
            opcion2 = int(input("¿Qué desea cambiar?"))

            if opcion2 == 1:
                libro1.titulo = input("Ingrese el nuevo titulo")

            elif opcion2 == 2:
                libro1.autor = input("Ingrese el nuevo autor")

            elif opcion2 == 3:
                libro1.editorial = input("Ingrese la nueva editorial")

            elif opcion2 == 4:
                libro1.genero = input("Ingrese el nuevo género")

            elif opcion2 == 5:
                libro1.añop = int(input("Ingrese el nuevo año"))

            else:
                libro1.disponibilidad = input("Ingrese la nueva disponibilidad")


    if opcion == 3:                                        #OPCION 3
        elim =  input("Ingrese el titulo del libro que quiere eliminar")
        for li in biblioteca:
            if li.titulo == elim:
                biblioteca.remove(li)
                print("Tu libro ah sido eliminado correctamente")
            else :
                print("Tu libro no se ah podido eliminar, perdon :(")
        
    if opcion == 4:                                        #OPCION 4
        pre = input("Ingrese el titulo del libro que quiere")
        for libro1 in biblioteca:
            if libro1.titulo == pre:
                if libro1.disponibilidad == "si" :
                    libro1.prestar()
                    print("Libro correctamente prestado")
                else :
                    print("Libro no disponible")

    

    if opcion == 5:                                        #OPCION 5
        dev = input("Ingrese el titulo del libro que quiere devolver")
        for libro1 in biblioteca:
            if libro1.titulo == dev:
                if libro1.disponibilidad == "no" :
                    libro1.devuelto()
                    print("Libro correctamente devuelto")
                else :
                    print("Libro ya devuelto")
    
            
    if opcion == 6 :                                        #OPCION 6
        for libro1 in biblioteca:
            libro1.ticket()


    if opcion == 7 :                                        #OPCION 7
        for p in biblioteca:
            if p.disponibilidad == "no":
                print(p.titulo)
            else :
                pass
                
    if opcion == 8 :                                        #OPCION 8
        for d in biblioteca:
            if d.disponibilidad == "si":
                print(d.titulo)
            else :
                pass

    if opcion == 9 :                                        #OPCION 9
        gen=input("ingrese el genero de un libro que le interese")
        for g in biblioteca:
            if gen == g.genero:
                print(g.titulo)
            else :
                pass
    if opcion == 10 :                                        #OPCION 10
        for m in biblioteca:
            año =  2024 - m.añop
            if año < 20 :
                print(m.titulo)
            else :
                pass
            año == 0
