# Programa: Ordenar una fila específica de una matriz 3x3 con Bubble Sort

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]

# Función Bubble Sort para ordenar una lista en orden ascendente
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar elementos
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Función para ordenar una fila específica
def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        matriz[fila_index] = bubble_sort(matriz[fila_index])
    else:
        print("⚠️ Índice de fila inválido.")

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir fila a ordenar (ejemplo: 1 = segunda fila)
fila_a_ordenar = 2
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
