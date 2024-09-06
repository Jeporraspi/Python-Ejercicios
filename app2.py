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