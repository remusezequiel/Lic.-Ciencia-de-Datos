"""
1) Escape de sala más veloz [1 punto]

Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, 
escribir una función en Python que devuelva la posición  (índice) en la cual se encuentra el tiempo más rápido,
excluyendo las salas en las que no haya salido (0 o mayor a 60).

problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩): Z {
  requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive}
  asegura: {
    res es la posición de la sala en tiempos_salas de la que más rápido se salió 
    (en caso que haya más de una, devolver la primera, osea la de menor índice)
  }
}
"""

def posicion_si_es_minimo(tiempos_salas:list[int], tiempo:int)->int:
    """
        Devuelve el indice si el tiempo pasado es minimo dentro de la lista.
    """
    for indice in range(len(tiempos_salas)):
        if tiempos_salas[indice]<=tiempo:
            return indice
    

def tiempo_mas_rapido (tiempos_salas:list[int])->int:
    """
        Si la posición de posicion_si_es_minimo(tiempos_salas,tiempo) es menor a 
        la posición del minimo anterior, entonces 
    """
    posicion:int=0

    for tiempo in tiempos_salas:
        if posicion<=posicion_si_es_minimo(tiempos_salas,tiempo):
            posicion=posicion_si_es_minimo(tiempos_salas,tiempo)
    return posicion

if __name__ == "__main__":
    lista_1=[1]
    lista_2=[9,1,8,1]
    lista_3=[9,7,8,1]
    lista_4=[0,7,8,0]
    lista_5=[0,7,0,8,0]
    lista_5=[0,7,0,8,1]

    print("Lista: ",lista_1 ,"posicion del minimo: ", tiempo_mas_rapido(lista_1))
    print("Lista: ",lista_2 ,"posicion del minimo: ", tiempo_mas_rapido(lista_2))
    print("Lista: ",lista_3 ,"posicion del minimo: ", tiempo_mas_rapido(lista_3))
    print("Lista: ",lista_4 ,"posicion del minimo: ", tiempo_mas_rapido(lista_4))
    print("Lista: ",lista_5 ,"posicion del minimo: ", tiempo_mas_rapido(lista_5))