
# Ejercicios de Listas con For en Python











# 3. Encontrar el elemento más grande de una lista

def elemento_mas_grande(lista):
    # Verificar que la lista no esté vacía
    if not lista:
        raise ValueError("La lista está vacía y no se puede encontrar el elemento más grande.")

    # Inicializar el elemento más grande con el primer elemento de la lista
    max_elemento = lista[0]

    # Iterar sobre los elementos de la lista
    for numero in lista:
        # Si el número actual es mayor que el máximo encontrado hasta ahora, actualizar el máximo
        if numero > max_elemento:
            max_elemento = numero

    return max_elemento
=======
#Ejercicios de Listas con For en Python
#2. Contar la cantidad de elementos pares en una lista:
def contar_pares(ingreso_numeros):
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
print("La totalidad de números pares es:", cantidad_pares)

