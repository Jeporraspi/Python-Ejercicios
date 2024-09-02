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