#Ejercicios con While y Colecciones en Python
#1. Eliminar duplicados de una lista:

"""def eliminar_duplicados(lista):


  sin_duplicados = set()
  resultado = []
  indice = 0

  while indice < len(lista):
    numero = lista[indice]
    if numero not in sin_duplicados:
      sin_duplicados.add(numero)
      resultado.append(numero)
    indice += 1

  return resultado

cantidad_numeros = int(input("¿Cuántos números vas a ingresar? "))
numeros = []
for _ in range(cantidad_numeros):
  try:
    num = int(input("Ingrese un número: "))
    numeros.append(num)
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")

nueva_lista = eliminar_duplicados(numeros)
print("Lista sin duplicados:", nueva_lista)"""

"""
import random

def adivina_numero():
    
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
    adivina_numero()  """
"""
numeros_pares = []
contador = 2

while contador <= 100:
  numeros_pares.append(contador)
  contador += 2

print(numeros_pares)"""