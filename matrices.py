import random

# Definir el tamaño de la matriz
filas = 5
columnas = 6

# Crear una matriz vacía
matriz = [[0] * columnas for _ in range(filas)]

# Llenar la matriz con números aleatorios
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(0, 10)

# Mostrar la matriz
print("Matriz:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=' ')
    print()

# Calcular la suma de los números en la matriz
suma_total = sum(sum(fila) for fila in matriz)
print("Suma total:", suma_total)

# Calcular la suma de los números pares e impares en la matriz
suma_pares = sum(num for fila in matriz for num in fila if num % 2 == 0)
suma_impares = sum(num for fila in matriz for num in fila if num % 2 != 0)
print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)

# Calcular la suma de cada columna
sumas_columnas = [sum(fila[j] for fila in matriz) for j in range(columnas)]
print("Suma de cada columna:", sumas_columnas)

# Calcular la suma de cada fila
sumas_filas = [sum(fila) for fila in matriz]
print("Suma de cada fila:", sumas_filas)

# Calcular la suma de los elementos de la diagonal principal
suma_diagonal = sum(matriz[i][i] for i in range(min(filas, columnas)))
print("Suma de la diagonal principal:", suma_diagonal)

# Calcular la transpuesta de la matriz
transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

# Mostrar la transpuesta de la matriz
print("Transpuesta de la matriz:")
for i in range(columnas):
    for j in range(filas):
        print(transpuesta[i][j], end=' ')
    print()
