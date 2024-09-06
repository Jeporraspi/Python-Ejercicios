# Ejercicios con While y Colecciones en Python










# -----------------------------------------------------------------------------------------------------


#3. Contar vocales en una frase

def contar_vocales(frase):
    # 3.1 Definir un conjunto de vocales
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Inicializar el contador de vocales en 0
    contador_vocales = 0

    # 3.2 Inicializar el índice para recorrer la frase
    i = 0
    
    # 3.3 Bucle while para recorrer la frase
    while i < len(frase):
        # 3.4 Si el carácter actual es una vocal, incrementar el contador
        if frase[i] in vocales:
            contador_vocales += 1
        # 3.5 Avanzar al siguiente carácter
        i += 1
    
    return contador_vocales

# 3.4 Pedir al usuario que ingrese una frase
frase_usuario = input("Ingrese una frase: ")

# 3.5 Llamar a la función y mostrar el resultado
vocales_encontradas = contar_vocales(frase_usuario)
print(f"La frase contiene {vocales_encontradas} vocales.")

# -----------------------------------------------------------------------------------------------------

# 4 Calculadora básica

def calculadora():
    # 4.1 Diccionario con las operaciones disponibles
    operaciones = {
        '+': 'suma',
        '-': 'resta',
        '*': 'multiplicación',
        '/': 'división'
    }

    while True:
        # 4.2 Mostrar las operaciones disponibles
        print("\nOperaciones disponibles:")
        for simbolo, nombre in operaciones.items():
            print(f"{simbolo}: {nombre}")

        # 4.3 Pedir al usuario que seleccione una operación
        operacion = input("Ingrese una operación (+, -, *, /) o 'salir' para finalizar: ")

        # 4.5 Verificar si el usuario quiere salir
        if operacion.lower() == 'salir':
            print("Saliendo de la calculadora...")
            break

        # 4.6 Verificar que la operación ingresada sea válida
        if operacion not in operaciones:
            print("Operación no válida. Inténtelo de nuevo.")
            continue

        # 4.7 Pedir al usuario que ingrese los números
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números válidos.")
            continue

        # 4.8 Realizar la operación seleccionada
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            # 4.9 Evitar la división por cero
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                continue
            resultado = num1 / num2

        # 4.10 Mostrar el resultado
        print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

# 4.11 Ejecutar la calculadora
calculadora()

# -----------------------------------------------------------------------------------------------------

