"""
3)Posiciones pares [3 puntos]

Implementar la función elem_en_pos_pares() que dada una lista de listas
matriz y un elemento elem devuelva una lista de bool de igual longitud 
de matriz, que indique en cada posición si elem se encuentra en alguna 
posición par de la sublista de matriz que ocupa esaposición.

    problema elem_en_pos_pares(in matriz:seq⟨seq⟨Z⟩⟩, in elem:Z ) : seq⟨Bool⟩ {
        asegura:{
            (|res|=|matriz|) 
        }
        asegura: {
            Cada i-ésima posición de res indica si
            elem pertenece a la lista matriz[i] en una posición par}
        }

Por ejemplo, dados:
elem = 1
M = [ [1, 2, 3, 4, 5, 6, 7, 8, 9],
      [9, 8, 7, 6, 4, 5, 3, 2, 1],
      [0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 4, 0, 0, 0],  
      [0, 1, 0, 0, 6, 0, 0, 1, 0],
    ]
se debería devolver
res = [true, true, true,false,false]
"""

def es_par(num:int)->bool:
    return num%2==0

def esta_en_posicion_par(fila:list[int],elem:int)->bool:
    for i in range(len(fila)):
        if elem==fila[i] and es_par(i):
            return True
    return False 

# elem_en_pos_pares(in matriz:seq⟨seq⟨Z⟩⟩, in elem:Z ) : seq⟨Bool⟩
def elem_en_pos_pares(matriz:list[list[int]], elem:int)->list[bool]:
    
    res:list[bool]=list()
    for i in matriz:
        res.append(esta_en_posicion_par(i,elem))
    
    return res

if __name__ == "__main__":
    elem = 1
    M = [ [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 4, 5, 3, 2, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 4, 0, 0, 0],  
        [0, 1, 0, 0, 6, 0, 0, 1, 0],
        ]

    print(elem_en_pos_pares(M,elem))


