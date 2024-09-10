def multiplicar_escalar_matriz(escalar, matriz):
    """Multiplica un escalar por una matriz"""
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear una nueva matriz para almacenar el resultado
    resultado = [[0]*columnas for _ in range(filas)]
    
    # Realizar la multiplicación escalar
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = escalar * matriz[i][j]
    
    return resultado

# Ejemplo de uso
escalar = 3
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(f"Multiplicación del escalar {escalar} por la matriz:")
resultado = multiplicar_escalar_matriz(escalar, matriz)
for fila in resultado:
    print(fila)
