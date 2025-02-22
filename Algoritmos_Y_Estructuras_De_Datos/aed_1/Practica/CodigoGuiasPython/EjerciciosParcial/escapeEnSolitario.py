"""
3) Escape en solitario [2 puntos]

Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape,
y los valores son los tiempos (en minutos) registrados para cada sala
(0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), 
escribir una función en Python que devuelva los índices de todas las filas (que representan 
las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).

problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩): seq⟨Z⟩ {
  requiere: {Hay por lo menos una sala en amigos_por_salas}
  requiere: {Hay 4 amigos en amigos_por_salas}
  requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive}
  asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas}
  asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0,
    la posición de dicha sala en amigos_por_salas debe aparecer res}
  asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, 
  y el tercer valor es distinto de 0}
}
"""
# Matris[fila][columa]
#amigos_por_salas[tiempo de la sala de escape][amigo]
# tiempo de la sala de escape = ["0 si no fueron", "61 si no salieron",  "un número entre 1 y 60 si salieron"]


def escape_en_solitario(amigos_por_salas:list[list[int]])->list[int]:
    res:list[int]=list()

    for fila in range(len(amigos_por_salas)):
        if amigos_por_salas[fila][0]==amigos_por_salas[fila][1]==amigos_por_salas[fila][3]==0 and amigos_por_salas[fila][2]!=0 :
            res.append(fila)
    return res

if __name__ == "__main__":
    aps1 = [[0,0,1,4],
         [0,0,21,0]]
    print(escape_en_solitario(aps1)) #[1]
    aps2 = [[0,0,1,0],
         [0,0,21,0],
         [1,2,54,1],
         [0,0,5,1]]
    print(escape_en_solitario(aps2)) #[0,1]
    aps3 = [[0,0,61,61],
         [12,32,0,0],
         [35,21,26,21]]
    print(escape_en_solitario(aps3)) #[]
    aps4 = [[0,0,0,0],
         [0,0,61,0],
         [0,0,21,0],
         [0,0,0,0]]
    print(escape_en_solitario(aps4)) #[1,2]
    aps5 = [[0,0,34,0],
            [0,0,61,0],
            [0,0,21,0],
            [0,0,54,0]]
    print(escape_en_solitario(aps5)) #[0,1,2,3]