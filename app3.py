# Ejercicios con Diccionarios














# -----------------------------------------------------------------------------------------------------

# 3. Encontrar al alumno con la nota más alta

def alumno_con_mejor_nota(alumnos):
    # 3.1 Inicializar variables para almacenar el nombre del mejor alumno y la mejor nota
    mejor_alumno = None
    mejor_nota = -1

    # 3.2 Recorrer el diccionario de alumnos y notas
    for alumno, nota in alumnos.items():
        if nota > mejor_nota:  # Nota: Si se encuentra una nota mayor, actualizar
            mejor_nota = nota
            mejor_alumno = alumno

    return mejor_alumno

# 3.3 Ejemplo de uso
alumnos = {
    'Juan': 85,
    'María': 92,
    'Pedro': 78,
    'Ana': 95,
    'Carlos': 88
}

mejor_alumno = alumno_con_mejor_nota(alumnos)
print(f"El alumno con la mejor nota es: {mejor_alumno}")


# -----------------------------------------------------------------------------------------------------

# 4. Crear un diccionario de palabras y sus definiciones

def crear_diccionario():
    # 4.1 Inicializar un diccionario vacío
    diccionario = {}

    while True:
        # 4.2 Pedir al usuario que ingrese una palabra
        palabra = input("Ingrese una palabra (o escriba 'salir' para finalizar): ")

        # 4.3 Verificar si el usuario desea salir
        if palabra.lower() == 'salir':
            break

        # 4.5 Pedir al usuario que ingrese la definición de la palabra
        definicion = input(f"Ingrese la definición de '{palabra}': ")

        # 4.6 Almacenar la palabra y su definición en el diccionario
        diccionario[palabra] = definicion

    # 4.7 Mostrar todas las palabras y definiciones
    print("\nDiccionario completo:")
    for palabra, definicion in diccionario.items():
        print(f"{palabra}: {definicion}")

# 4.8 Ejecutar el programa
crear_diccionario()


# -----------------------------------------------------------------------------------------------------
