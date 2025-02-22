"""
3) Matriz de responsables por turnos [2 puntos]

Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los
días, en orden de lunes a domingo, y cada fila a un rango de una hora. Hay cuatro filas para los turnos 
de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde (14, 15, 16 y 17).

Para hacer más eficiente el trabajo del personal de la veterinaria, se necesita analizar si quienes 
quedan de responsables, están asignadas de manera continuada en los turnos de cada día.

Para ello se pide desarrollar una función en Python que, dada la matriz de turnos, devuelva una lista
de tuplas de Bool, una por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser
True sí y solo sí todos los valores de los turnos de la mañana para ese día son iguales entre sí. El 
segundo elemento debe ser True sí y solo sí todos los valores de los turnos de la tarde para ese día 
son iguales entre sí. Siempre hay una persona responsable en cualquier horario de la veterinaria.

problema un_responsable_por_turno(in grilla_horaria: seq<seq<String>>): seq<(Bool x Bool)> {
    requiere: {|grilla_horaria| = 8}
    requiere: {
        Todos los elementos de grilla_horaria tienen el mism tamaño (mayor a 0 y menor a 8)
    }
    requiere: {
        No hay cadenas vacías en las listas de grilla_horaria
    }
    asegura: {
        |res| = |grilla_horaria[0]|
    }
    asegura: {
        El primer valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <==> los primeros
        4 valores de la columna i de grilla_horaria son iguales entre sí
    }
    asegura: {
        El segundo valor de la tupla en res[i], con i:<, 0 <= i < |res| es igual a True <==> los últimos
        4 valores de la columna i de grilla_horaria son iguales entre sí
    }
}
"""
def tomar_submatriz(grilla_horaria: list[list[str]],desde:int,hasta:int)->list[list[str]]:
    res:list[list[str]] = list()    
    for fila in range(desde,hasta):     
        res.append(grilla_horaria[fila])
    return res
        
## La idea es que las primeras 4 filas son turnos mañana y las 4 ultimas son turnos tarde
# Luego si grilla[i][j]==grilla[i][j+1]==grilla[i][j+2]==grilla[i][j+3], entonces debe devolver True 
# teniendo encuenta que el primer elemento de la tupla es el TM y el segundo el TN
def un_responsable_por_turno(grilla_horaria: list[list[str]])->list[tuple[bool,bool]]:
    res:list[tuple[bool,bool]] = list()
    
    condicion_mañana:bool = bool()
    condicion_tarde:bool = bool()

    turno_mañana:list[list[str]]=tomar_submatriz(grilla_horaria,0,4)
    turno_tarde:list[list[str]]=tomar_submatriz(grilla_horaria,4,8)

    for j in range(len(turno_mañana[0])):
        condicion_mañana = turno_mañana[0][j]==turno_mañana[1][j]==turno_mañana[2][j]==turno_mañana[3][j]
        condicion_tarde = turno_tarde[0][j]==turno_tarde[1][j]==turno_tarde[2][j]==turno_tarde[3][j]
        
        res.append((condicion_mañana,condicion_tarde))
    return res

if __name__ == "__main__":
    grilla_horaria = [ # Turno mañana
                  ["Ana", "Ana", "Ana", "Ana", "Carlos", "Carlos", "Carlos", "Carlos"], # i_fila = 0 -> todos comparan con este
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 1
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 2
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 3
                  # Turno tarde
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 4 -> todos comparan con este
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 5
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Pedro", "Carlos"], # i_fila = 6
                  ["Ana", "Ana", "Ana", "Pedro", "Carlos", "Carlos", "Ana", "Carlos"]] # i_fila = 7
    
    print(un_responsable_por_turno(grilla_horaria))
