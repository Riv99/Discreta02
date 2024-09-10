def suma_matrices(matriz1, matriz2):
    """Suma dos matrices"""
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    resultado = [[0]*columnas for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return resultado

def resta_matrices(matriz1, matriz2):
    """Resta dos matrices"""
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    resultado = [[0]*columnas for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] - matriz2[i][j]
    
    return resultado

# Ejemplo de uso
matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8, 9],
    [10, 11, 12]
]

print("Suma de matrices:")
resultado_suma = suma_matrices(matriz1, matriz2)
for fila in resultado_suma:
    print(fila)

print("\nResta de matrices:")
resultado_resta = resta_matrices(matriz1, matriz2)
for fila in resultado_resta:
    print(fila)
