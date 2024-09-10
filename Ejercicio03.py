def leer_matriz(filas, columnas, nombre):
    """Lee una matriz desde la entrada del usuario"""
    matriz = []
    print(f"Ingrese los valores para la {nombre} matriz de {filas}x{columnas}:")
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los valores de la fila {i+1} separados por espacios: ").split()))
        while len(fila) != columnas:
            print(f"Error: Debe ingresar exactamente {columnas} valores. Intente de nuevo.")
            fila = list(map(int, input(f"Ingrese los valores de la fila {i+1} separados por espacios: ").split()))
        matriz.append(fila)
    return matriz

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

def imprimir_matriz(matriz):
    """Imprime una matriz"""
    for fila in matriz:
        print(" ".join(map(str, fila)))

def main():
    # Pedir dimensiones de las matrices
    filas = int(input("Número de filas de las matrices: "))
    columnas = int(input("Número de columnas de las matrices: "))

    # Leer las dos matrices
    matriz1 = leer_matriz(filas, columnas, "primera")
    matriz2 = leer_matriz(filas, columnas, "segunda")

    try:
        # Realizar operaciones y mostrar resultados
        print("\nSuma de matrices:")
        resultado_suma = suma_matrices(matriz1, matriz2)
        imprimir_matriz(resultado_suma)

        print("\nResta de matrices:")
        resultado_resta = resta_matrices(matriz1, matriz2)
        imprimir_matriz(resultado_resta)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

