"""
def promediodenotas():
    notas = {}
    cantidad_estudiantes = int(input("cantidad de estudiantes: "))
    for _ in range(cantidad_estudiantes):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        notas[nombre] = nota
    suma_notas = 0
    cantidad_notas = 0

    for alumno, nota in notas.items():
        suma_notas += nota
        cantidad_notas += 1

    promedio = suma_notas / cantidad_notas
    return promedio

promedio = promediodenotas()
print("El promedio:", promedio) 
"""