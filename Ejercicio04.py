def leer_matriz(filas, columnas):
    """Lee una matriz desde la entrada del usuario"""
    matriz = []
    print(f"Ingrese los valores para una matriz de {filas}x{columnas}:")
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los valores de la fila {i+1} separados por espacios: ").split()))
        while len(fila) != columnas:
            print(f"Error: Debe ingresar exactamente {columnas} valores. Intente de nuevo.")
            fila = list(map(int, input(f"Ingrese los valores de la fila {i+1} separados por espacios: ").split()))
        matriz.append(fila)
    return matriz

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

def imprimir_matriz(matriz):
    """Imprime una matriz"""
    for fila in matriz:
        print(" ".join(map(str, fila)))

def main():
    # Pedir el valor del escalar
    escalar = float(input("Ingrese el valor del escalar: "))

    # Pedir dimensiones de la matriz
    filas = int(input("Número de filas de la matriz: "))
    columnas = int(input("Número de columnas de la matriz: "))

    # Leer la matriz
    matriz = leer_matriz(filas, columnas)

    # Multiplicar el escalar por la matriz
    resultado = multiplicar_escalar_matriz(escalar, matriz)

    # Mostrar el resultado
    print("\nResultado de multiplicar el escalar por la matriz:")
    imprimir_matriz(resultado)

if __name__ == "__main__":
    main()
