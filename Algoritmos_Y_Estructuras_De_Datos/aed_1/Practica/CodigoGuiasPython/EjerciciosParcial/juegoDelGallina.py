"""
1) Juego del gallina (3 puntos)
    El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario;
    si alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina".
    Se hizo un torneo para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando.
    
    Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. 
    Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas.
    Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos! 
    
    En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se devía, o nunca lo hace. 
    
    Se debe programar la función 'torneo_de_gallinas' que recibe un diccionario 
    (donde las claves representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) 
    y devuelve un diccionario con los puntajes obtendidos por cada jugador.

    problema torneo_de_gallinas (in estrategias: dict⟨String,String⟩) : dict⟨String,Z⟩ {
    requiere: {estrategias tiene por lo menos 2 elementos (jugadores)}
    requiere: {Las claves de estrategias tienen longitud mayor a 0}
    requiere: {Los valores de estrategias sólo pueden ser los strings "me desvio siempre" ó "me la banco y no me desvio"}
    asegura: {Las claves de res y las claves de estrategias son iguales}
    asegura: {
        para cada jugador p perteneciente a claves(estrategias), 
        res[p] es igual a la cantidad de puntos que obtuvo al finalizar el torneo, 
        dado que jugó una vez contra cada otro jugador
        }
}
"""
def jugador_jugando_contra_otros(jugador:str,est_jugador:str, estrategias:dict[str,str])->int:
    puntaje:int=0
    for j,e in estrategias.items():
        if jugador!=j:
            if est_jugador=="me la banco y no me desvio" and est_jugador==e:#chocan
                puntaje=puntaje-5
            elif est_jugador=="me la banco y no me desvio" and est_jugador!=e: #no me desvio y el otro si
                puntaje=puntaje+10
            elif est_jugador!="me la banco y no me desvio" and est_jugador==e:# me Desvio y el otro tambien
                puntaje=puntaje-10
            elif est_jugador!="me la banco y no me desvio" and est_jugador!=e:# me Desvio y el otro se la banca
                puntaje=puntaje-15
    return puntaje
        
def torneo_de_gallinas(estrategias: dict[str,str])-> dict[str,int]:
    res:dict[str,int]=dict()

    for j,e in estrategias.items():
        res[j]=jugador_jugando_contra_otros(j,e,estrategias)
    
    return res


if __name__ == "__main__":

    me_la_banco:str ="me la banco y no me desvio"
    desvio:str = "me desvio siempre"
    
    estrategias_1 = {"juan":me_la_banco, "marcelo":desvio} # res = {"juan":10, "marcelo":-15}
    estrategias_2 = {"juan":me_la_banco, "marcelo":me_la_banco} # res = {"juan":-5, "marcelo":-5}
    estrategias_3 = {"juan":desvio, "marcelo":desvio} # res = {"juan":10, "marcelo":-10}
    # res         = {"juan":-15-10-15 = -40, "marcelo":10+10-5 = 15, "pedro":-10-15-15=40, "willy":10-5+10 =15}
    estrategias_4 = {"juan":desvio, "marcelo":me_la_banco, "pedro":desvio, "willy":me_la_banco} 

    print("1: ", torneo_de_gallinas(estrategias_1))
    print("2: ", torneo_de_gallinas(estrategias_2))
    print("3: ", torneo_de_gallinas(estrategias_3))
    print("4: ", torneo_de_gallinas(estrategias_4))