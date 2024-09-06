#Ejercicios de Listas con For en Python
#2. Contar la cantidad de elementos pares en una lista:
"""def contar_pares(ingreso_numeros):
  contador = 0
  for numero in ingreso_numeros:
    if numero % 2 == 0:
      contador += 1
  return contador
numeros = []
contador_ingresos = 0
while contador_ingresos < 4:
  try:
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    contador_ingresos += 1
  except ValueError:
    print("Por favor, ingrese un número entero.")
cantidad_pares = contar_pares(numeros)
8
print("La totalidad de números pares es:", cantidad_pares)"""
import random

def adivina_numero():
    """
    Juego de adivinar un número aleatorio entre 1 y 100.
    """

    numero = random.randint(1, 100)
    intentos = 7

    print("Adivinar un número con intentos limitados:")
    print("Tienes 7 intentos para adivinar un número entre 1 y 100.")

    while intentos > 0:
        intento = int(input("Ingresa número: "))

        if intento == numero:
            print(f" Adivinaste el número en {7 - intentos + 1} intentos.")
            break
        elif intento < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intentos -= 1
        print(f"Te quedan {intentos} intentos.")

    if intentos == 0:
        print(f"Perdiste. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_numero()