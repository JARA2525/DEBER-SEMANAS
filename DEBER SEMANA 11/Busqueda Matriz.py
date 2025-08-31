# Programa: Búsqueda en una Matriz Bidimensional (3x3)

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorre filas
        for j in range(len(matriz[i])):   # Recorre columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna posición (fila, columna)
    return None  # Si no lo encuentra, retorna None

# Definir el valor a buscar
valor_buscado = 4

# Ejecutar la búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Mostrar resultado
if resultado:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: Fila {resultado[0]}, Columna {resultado[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")

