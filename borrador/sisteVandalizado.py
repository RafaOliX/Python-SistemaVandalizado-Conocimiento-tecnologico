# EL CÓDIGO A CONTINUACIÓN HA SIDO VANDALIZADO POR EL HAMPA, POR LO QUE YA NO FUNCIONA. TU TAREA ES CORREGIR EL CÓDIGO PARA HACER QUE ESTE VUELVA A FUNCIONAR. 
#Variables globales 
nombres = ["Juan", "Pablo", "Carlos", "María", "Sofía", "Cristiano", "Laura", "Diego", "Gabriela", "Daniel", "Natalia", "José", "Isabella", "Pedro", "Alejandro", "Camila", "Ana", "Valentina", "Miguel", "Edith"] 
notas = [17, 5, 11, 3, 8, 19, 6, 7, 14, 15, 16, 17, 18, 5, 11, 12, 4, 10, 19, 20] 
 
#Función para imprimir todos los estudiantes en pantalla 
def verEstudiantes(): 
    # Determinar la longitud máxima de los nombres para ajustar el formato 
    max_length = #max(len(nombre) for nombre in nombres) 
     
    print("") 
 
    for i in #range(len(nombres)): 
        print(f"Nombre: {nombres[i]:<{max_length}}  Nota: {notas[i]} ") 
    input() 
 
#Función para mostrar a los estudiantes y determinar si están aprobados o no 
def mostrarAprobados(): 
    # Determinar la longitud máxima de los nombres para ajustar el formato 
    max_length = max(len(nombre) for nombre in nombres) 
 
    print("") 
     
    for i in #range(len(nombres)): 
        #Determinar aprobación 
        estado = "APROBADO" if notas[i] # Aquí había algo 
        print(f"Nombre: {nombres[i]:<{max_length}}  Nota: {notas[i]:<{4}} {estado}") 
    input() 
 
# Función de Quicksort para ordenar la lista de tuplas (nombre, nota) por el nombre 
def quicksort(arr): 
    #if len(arr) <= 1: 
        return arr 
    pivot = arr[len(arr) // 2][0]  # Usa el primer elemento (nombre) para el pivot 
    left = [x for x in arr if x[0] < pivot] 
    middle = [x for x in arr if x[0] == pivot] 
    right = [x for x in arr if x[0] > pivot] 
    return quicksort(left) + middle + quicksort(right) 
 
# Función para buscar un estudiante 
def busquedaBinaria(buscado): 
    # Combinar las listas de nombres y notas en una lista de tuplas 
    nombres_notas = list(aquí_había_un_método(nombres, notas)) #no olvides revisar aquí 
 
    # Ordenar la lista de tuplas por el nombre usando Quicksort 
    nombres_notas_ordenados = quicksort(nombres_notas) 
 
    buscado = buscado[0].upper() + buscado[1:].lower() 
 
    print(buscado) 
 
    # Realizar búsqueda binaria en la lista de tuplas 
    inicio = 0 
    final = len(nombres_notas_ordenados) - 1 
 
    # ¿Y la búsqueda? 
 
    return None, None 
 
# Función correspondiente a la opción buscar estudiante 
def buscarEstudiante(): 
    while True: 
        print("\nPuede escribir 'salir' para dejar de buscar") 
        print("\n¿Que estudiante quieres buscar?") 
        buscado = input("> ") 
 
        #if buscado.upper() == "SALIR": 
            break 
 
        nombreBuscado, notaBuscado = busquedaBinaria(buscado) 
        if nombreBuscado: 
            print(f"\nEstudiante encontrado: {nombreBuscado} con una calificación de: {notaBuscado}") 
            input() 
        else: 
            print("\nEstudiante no encontrado") 
            input() 
 
#Función de algoritmo burbuja para ordenar estudiantes según su notas 
def burbuja(Nombre, Calificacion): 
    cont = len(Calificacion) 
 
    # Que desordenado se ve, ¿no? 
     
    return Nombre, Calificacion 
 
# Función correspondiente a la opción ordenar notas 
def ordenarNotasEstudiantes(): 
    global nombres, notas 
    print("\nEstas seguro de que quieres ordenar las notas de los estudiantes?") 
    opcion = input("> ") 
 
    if opcion.upper() == "SI": 
        nombres, notas = burbuja(nombres, notas) 
        print("") 
        #verEstudiantes() OJO 
 
#Función para agregar un nuevo estudiante 
def nuevoEstudiante(): 
 
    while True: 
        print("\nPuede escribir 'salir' para dejar de agregar") 
        nombre = input("\nIndique el nombre del estudiante: ") 
        nota = input("Indique su calificación actual: ") 
 
        #if nombre.upper() == "SALIR" or nota.upper() == "SALIR": 
            break 
 
        try: 
           nota = int(nota) 
           if nota < 0 or nota > 20 or len(nombre) == 0: 
            print("\nPor favor, escriba datos validos") 
           else: 
            print(f"\nEsta seguro de que quiere agregar al estudiante {nombre} con una calificacion de {nota}?\nIndique si o no") 
            opcion = input("> ") 
 
            if opcion.upper() == "SI": 
                nombres.append(nombre) 
                notas.append(nota) 
                print(f"\n{nombre} y su calificación de {nota} fue agregado satisfactoriamente") 
        except: 
            print("\nDebe colocar datos validos") 
 
#Función para eliminar un estudiante 
def eliminarEstudiante(): 
 
    # ¿BUCLES? 
        print("\nPuede escribir 'salir' para dejar de eliminar") 
        print("\nQue estudiante desea eliminar?") 
        buscado = input("> ") 
 
        #if buscado.upper() == "SALIR": 
            break 
 
        nombreBuscado, notaBuscado = busquedaBinaria(buscado) 
 
        print(f"\nEsta seguro de que quiere eliminar a {nombreBuscado} y su calificación de {notaBuscado}?") 
        opcion = input("> ") 
 
        if opcion.upper() == "SI": 
            nombres.remove(nombreBuscado) 
            notas.remove(notaBuscado) 
            print(f"\nEliminado a {nombreBuscado} satisfactoriamente") 
 
#Función para actualizar los datos de un estudiante 
def actualizarEstudiante(): 
    global nombres, notas 
 
    # ¿BUCLES? 
        print("\nPuede escribir 'salir' para dejar de actualizar") 
        print("\nQue estudiante desea actualizar?") 
        buscado = input("> ") 
 
        #if buscado.upper() == "SALIR": 
            break 
 
        nombreBuscado, notaBuscado = busquedaBinaria(buscado) 
 
        print(f"\nEsta seguro de que quiere actualizar a {nombreBuscado} y su calificación de {notaBuscado}?") 
        opcion = input("> ") 
 
        if opcion.upper() == "SI": 
            indice = nombres.index(nombreBuscado) 
            print("\nIndique si quiere actualizar el nombre, la nota o ambos:") 
            opcion = input("> ") 
 
            if opcion.upper() == "NOMBRE" or opcion.upper() == "AMBOS": 
                print("\nIndique el nuevo nombre") 
                nuevoNombre = input("> ") 
                nombres[indice] = nuevoNombre 
                print(f"\nEl nombre {nombreBuscado} a sido actualizado a {nuevoNombre} satisfactoriamente") 
                input() 
            if opcion.upper() == "NOTA" or opcion.upper() == "NOTAS" or opcion.upper() == "AMBOS": 
                print("\nIndique la nueva nota") 
                nuevaNota = input("> ") 
                try: 
                    nuevaNota = int(nuevaNota) 
                    notas[indice] = int(nuevaNota) 
                    print(f"\nLa nota {notaBuscado} a sido actualizado a {nuevaNota} satisfactoriamente") 
                    input() 
                except: 
                    print("\nDebe colocar datos validos") 
 
            if opcion.upper() != "AMBOS" and opcion.upper() != "NOMBRE" and opcion.upper() != "NOTA" and opcion.upper() != "NOTAS": 
                print("\nOpcion invalida") 
             
#Bucle principal 
def main(): 
    # ¿BUCLE PRINCIPAL? ¿EN DÓNDE? 
        print('''\nBienvenido al programa de control de estudiantes.\nPor favor eliga una opcion. 
    1.Ver estudiantes 
    2.Agregar nuevo estudiante 
    3.Actualizar nota 
    4.Eliminar estudiante 
    5.Ordenar notas 
    6.Mostrar aprobados 
    7.Buscar estudiante 
    8.Salir''') 
        opcion = input("> ") 
         
        if opcion == "8" or opcion.upper() == "SALIR": 
            print("\nFinalizando programa!") 
            break 
        # 
        else: 
            print("Por favor, escriba una opcion valida.\nPuede escribir versiones recortadas de las opciones como ver, agregar, o eliminar y tambien puede escribir el numero correspondiente a la opcion.\n") 
 
# espropiese