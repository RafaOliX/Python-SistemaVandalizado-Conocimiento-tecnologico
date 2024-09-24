import locale
import csv
import datetime
import json

# Archivo JSON
archivo_json = "datos_estudiantes.json"

# Función para cargar datos desde un archivo JSON (si existe)
def cargar_datos():
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            return data['nombres'], data['notas']
        print("Datos cargados desde el archivo JSON.")
    except FileNotFoundError:
        print("Archivo JSON no encontrado. Se utilizarán los datos iniciales.")
        return [], []

# Función para guardar datos en un archivo JSON
def guardar_datos_en_json(nombres, notas):
    try:
        data = {
            'nombres': nombres,
            'notas': notas
        }
        with open(archivo_json, 'w') as f:
            json.dump(data, f)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Cargar datos al inicio del programa
nombres, notas = cargar_datos()

# Función para imprimir todos los estudiantes en pantalla
def verEstudiantes():
    max_length = max(len(nombre) for nombre in nombres)
    print("")
    for i in range(len(nombres)):
        print(f"Nombre: {nombres[i]:<{max_length}}  Nota: {notas[i]}")
    input("Pulse cualquier botón para continuar...")

    print("\n¿Deseas generar un reporte en formato CSV?\n\n(Indique 'si' o 'no')")
    if input("> ").lower() == "si":
        locale.setlocale(locale.LC_ALL, '')
        with open('calificaciones_alumnos.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Calificaciones de Alumnos', datetime.datetime.now().strftime("%d/%m/%Y")])
            writer.writerow(['Nombre', 'Nota', 'Aprobado/Reprobado'])
            for nombre, nota in zip(nombres, notas):
                aprobado = "Aprobado" if nota >= 10 else "Reprobado"
                writer.writerow([nombre, f"{locale.format_string('%.2f', nota)}", aprobado])

        input("¡Exportación realizada con éxito! Abra su archivo con Excel.\n\nPulse cualquier botón para continuar...")

def mostrarAprobados():
    max_length = max(len(nombre) for nombre in nombres)
    print("")
    for i in range(len(nombres)):
        estado = "APROBADO" if notas[i] >= 10 else "REPROBADO"
        print(f"Nombre: {nombres[i]:<{max_length}}  Nota: {notas[i]:<{4}} {estado}")
    input("Pulse cualquier botón para continuar...")

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]
    return quicksort(left) + middle + quicksort(right)

def busquedaBinaria(buscado):
    nombres_notas = list(zip(nombres, notas))
    nombres_notas_ordenados = quicksort(nombres_notas)
    buscado = buscado[0].upper() + buscado[1:].lower()
    inicio = 0
    final = len(nombres_notas_ordenados) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if nombres_notas_ordenados[medio][0] == buscado:
            return nombres_notas_ordenados[medio]
        elif nombres_notas_ordenados[medio][0] < buscado:
            inicio = medio + 1
        else:
            final = medio - 1

    return None, None

def buscarEstudiante():
    while True:
        print("\nPuede escribir 'salir' para dejar de buscar")
        print("\n¿Qué estudiante quieres buscar?")
        buscado = input("> ")

        if buscado.upper() == "SALIR":
            break

        nombreBuscado, notaBuscado = buscar_estudiante_en_json(buscado)

        if nombreBuscado:
            print(f"\nEstudiante encontrado: {nombreBuscado} con una calificación de: {notaBuscado}")
        else:
            print("\nEstudiante no encontrado")

        input("Pulse cualquier botón para continuar...")

def buscar_estudiante_en_json(nombre):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            nombres_json = data['nombres']
            for i, nombre_json in enumerate(nombres_json):
                if nombre_json == nombre:
                    return nombre_json, data['notas'][i]
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")
    return None, None

def burbuja(Nombre, Calificacion):
    cont = len(Calificacion)
    for i in range(cont):
        for j in range(0, cont-i-1):
            if Calificacion[j] > Calificacion[j+1]:
                Calificacion[j], Calificacion[j+1] = Calificacion[j+1], Calificacion[j]
                Nombre[j], Nombre[j+1] = Nombre[j+1], Nombre[j]
    return Nombre, Calificacion


def ordenarNotasEstudiantes():
    global nombres, notas
    print("\n¿Estás seguro de que quieres ordenar las notas de los estudiantes?\n\n(Indique 'si' o 'no')")
    opcion = input("> ")
    if opcion.upper() == "SI":
        nombres, notas = burbuja(nombres, notas)
        guardar_datos_en_json(nombres, notas)  # Guardar el orden en el archivo JSON
        print("")
        verEstudiantes()

def nuevoEstudiante():
    while True:
        print("\nPuede escribir 'salir' para dejar de agregar")
        nombre = input("\nIndique el nombre del estudiante: ")
        nota = input("Indique su calificación actual: ")

        if nombre.upper() == "SALIR" or nota.upper() == "SALIR":
            break

        try:
            nota = int(nota)
            if nota < 0 or nota > 20 or len(nombre) == 0:
                print("\nPor favor, escriba datos válidos")
            else:
                print(f"\n¿Está seguro de que quiere agregar al estudiante {nombre} con una calificación de {nota}?\n\n(Indique 'si' o 'no')")
                opcion = input("> ")

                if opcion.upper() == "SI":
                    nombres.append(nombre)
                    notas.append(nota)
                    print(f"\n{nombre} y su calificación de {nota} fueron agregados satisfactoriamente")
                    guardar_datos_en_json(nombres, notas)
        except:
            print("\nDebe colocar datos válidos")

def eliminarEstudiante():
    while True:
        print("\nPuede escribir 'salir' para dejar de eliminar")
        print("\n¿Qué estudiante desea eliminar?")
        buscado = input("> ")

        if buscado.upper() == "SALIR":
            break

        try:
            index = nombres.index(buscado)
            nombres.pop(index)
            notas.pop(index)
            print(f"\n{buscado} ha sido eliminado.")
            guardar_datos_en_json(nombres, notas)
        except ValueError:
            print("\nEstudiante no encontrado.")


def editarEstudiante():
    while True:
        print("\nPuede escribir 'salir' para dejar de editar")
        print("\n¿Qué estudiante desea editar?")
        buscado = input("> ")

        if buscado.upper() == "SALIR":
            break

        try:
            index = nombres.index(buscado)
            print(f"\nEstudiante encontrado: {nombres[index]} con una calificación de: {notas[index]}")
            
            nuevo_nombre = input("\nIndique el nuevo nombre del estudiante (o presione Enter para mantener el actual): ")
            nueva_nota = input("Indique la nueva calificación del estudiante (o presione Enter para mantener la actual): ")

            if nuevo_nombre:
                nombres[index] = nuevo_nombre
            if nueva_nota:
                try:
                    nueva_nota = int(nueva_nota)
                    if 0 <= nueva_nota <= 20:
                        notas[index] = nueva_nota
                    else:
                        print("\nPor favor, ingrese una calificación válida (0-20).")
                except ValueError:
                    print("\nPor favor, ingrese una calificación válida (0-20).")

            guardar_datos_en_json(nombres, notas)
            print("\nDatos del estudiante actualizados correctamente.")
        except ValueError:
            print("\nEstudiante no encontrado.")

# Añadir la opción de editar estudiante en el menú principal
def menu():
    while True:
        print("\n1. Ver estudiantes")
        print("2. Mostrar aprobados")
        print("3. Buscar estudiante")
        print("4. Ordenar notas de estudiantes")
        print("5. Agregar nuevo estudiante")
        print("6. Eliminar estudiante")
        print("7. Editar estudiante")
        print("8. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            verEstudiantes()
        elif opcion == "2":
            mostrarAprobados()
        elif opcion == "3":
            buscarEstudiante()
        elif opcion == "4":
            ordenarNotasEstudiantes()
        elif opcion == "5":
            nuevoEstudiante()
        elif opcion == "6":
            eliminarEstudiante()
        elif opcion == "7":
            editarEstudiante()
        elif opcion == "8":
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")

# Ejecutar el menú principal
menu()