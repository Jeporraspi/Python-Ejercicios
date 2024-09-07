#Ejercicios de Listas con For en Python
#1. Sumar todos los elementos de una lista
mi_lista = [1, 2, 3, 3.5, 4, 4.5]

total = sum(mi_lista)

print(total)

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

#4. Crear una nueva lista con los elementos de otra lista multiplicados por 2.
#Primero se debe definir la lista. 
lista_multiplicacion = [2, 4, 6, 8, 10]

#Segundo se crea una nueva lista con los elementos a multiplicar por 2. 
#For elemento in lista_multiplicación, recorre la primera lista y se va ejecutando la expresion elemento * 2

nueva_lista = [elemento * 2 for elemento in lista_multiplicacion]

print(nueva_lista)

#5. Invertir una lista.
lista_nueva = [5, 6, 7, 8, 9, 10, 11]
lista_nueva.reverse()
print(lista_nueva)