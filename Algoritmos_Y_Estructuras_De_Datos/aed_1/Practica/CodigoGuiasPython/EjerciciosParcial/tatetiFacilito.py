"""
4) Ta-Te-Ti-Facilito (2 puntos)
Ana y Beto juegan al Ta-Te-Ti-Facilito. 

El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su ficha en cada turno. 
Juegan intercaladamente y comienza Ana. Ana pone siempre una 'X' en su turno y Beto pone una 'O' en el suyo. 
Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. 

Si el tablero está completo y no ganó nadie, entonces se declara un empate. 
El tablero comienza vacío, representado por ' ' en cada posición.
Notar que dado que juegan por turnos y comienza Ana poniendo una 'X' se cumple
que la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' son uno más que la cantidad de 'O'.

Se nos pide implementar una función en python 'problema quien_gano_el_tateti_facilito' 
que determine si ganó alguno, o si Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

problema quien_gano_el_tateti_facilito(in tablero:seq⟨seq⟨Char⟩) : Z {
  requiere: {tablero es una matriz cuadrada}
  requiere: {5<=|tablero[0]|<= 10}
  requiere: {tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'}
  asegura: {
    res = 1 <==> hay tres 'X' consecutivas en forma vertical(misma columna) 
    y no hay tres 'O' consecutivas en forma vertical(misma columna) 
  }
  asegura: {
    res = 2 <==> hay tres 'O' consecutivas en forma vertical (misma columna)
    y no hay tres 'X' consecutivas en forma vertical(misma columna)
  }
  asegura: {
    res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical
  }
  asegura: {
    res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)
  }
}
"""


def hay_3_consecutivos_en_columna(tablero:list[list[str]], letra:str)->bool:
    # 5<=len(tablero)<=10
    # tablero[Fila][Columna]
    for i in range(len(tablero)):
        for j in range(len(tablero)-2):
            if (tablero[j][i] ==  tablero[j+1][i] ==  tablero[j+2][i] == letra):
                return True
    return False

def quien_gano_el_tateti_facilito(tablero:list[list[str]])->int:

    anna = hay_3_consecutivos_en_columna(tablero,"X")
    beto = hay_3_consecutivos_en_columna(tablero,"O")

    if anna and not beto:
        return 1
    elif not anna and beto:
        return 2
    elif not anna and not beto:
        return 0
    elif anna and beto:
        return 3

if __name__ == "__main__":
    tablero:list[list[str]] = [["X","","","",""],["X","","","",""],["X","","","O",""],["O","","","O",""],["O","","","O",""]] 
    print(hay_3_consecutivos_en_columna(tablero,"O"))
