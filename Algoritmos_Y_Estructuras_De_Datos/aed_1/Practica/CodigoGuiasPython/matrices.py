# Matriz[Fila][Columna]

def columna(matris:list[list[int]], num_columna:int)->list[int]:
    columna:list[int]=list()
    for fila in range(len(matris)):
        columna.append(matris[fila][num_columna])
    return columna

def fila(matris:list[list[int]],num_fila:int)->list[int]:
    return matris[num_fila]

if __name__ == "__main__":
    matris:list[list[int]]=[[1,2,3],[4,5,6],[7,8,9]]

    print("La matriz es: ", matris)
    print("Columna 1: ", columna(matris,0))
    print("Columna 2: ", columna(matris,1))
    print("Columna 3: ", columna(matris,2))
    print("Fila 1: ", fila(matris,0))
    print("Fila 2: ", fila(matris,1))
    print("Fila 3: ", fila(matris,2))

