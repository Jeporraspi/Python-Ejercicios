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