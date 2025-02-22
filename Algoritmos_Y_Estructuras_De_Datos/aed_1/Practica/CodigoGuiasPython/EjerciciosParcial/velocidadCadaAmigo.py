"""
2) Velocidad de cada amigo [2 puntos]

Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) 
registrados para cada sala de escape en Capital, escribir  una función en Python que devuelva un diccionario.
En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la 
cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir)

problema promedio_de_salidas (in registro: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, ⟨Z x R⟩⟩ {
  requiere: {registro tiene por lo menos un integrante}
  requiere: {Todos los integrantes de registro tiene por lo menos un tiempo}
  requiere: {Todos los valores de registro tiene la misma longitud}
  requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive}
  asegura: {res tiene las mismas claves que registro}
  asegura: {
    El primer elemento de la tupla de res para un integrante, 
    es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 
    que figuran en sus valores de registro
    }
  asegura: {
    El segundo elemento de la tupla de res para un integrante, 
    si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor 
    estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0
    }
}
"""
def escapes_y_promedio(tiempos:list[int])->tuple[int,float]:
    suma:int=0
    escapes:int=0

    for t in tiempos:
        if 0<t<61:
            suma+=t
            escapes+=1
    
    if escapes==0:
        return (0,0.0)
    return (escapes,suma/escapes)

# res: dict[str, tuple[int,float]={nombre:(long[list],promedio[list])}                                                                            
def promedio_de_salidas(registro:dict[str,list[int]])->dict[str, tuple[int,float]]:
    res:dict[str, tuple[int,float]]=dict()

    for nombre,tiempos in registro.items():
        res[nombre] = escapes_y_promedio(tiempos)

    return res 

if __name__ == "__main__":
    r1 = {"agus": [0,21,3,61], "leo": [34,0,12,61]} #{"agus":(2,12.0), "leo":(2,23.0)}
    print(promedio_de_salidas(r1))
    r2 = {"agus": [0,21,3,61], "leo": [61,0,61,61]} #{"agus":(2,12.0), "leo":(0,0.0)}
    print(promedio_de_salidas(r2))
    r3 = {"agus": [0,61,13,12,45,34,12,61], "leo": [35,46,21,31,21,23,25,38,], "ale": [61,61,61,61,61,61,61,61]} #{"agus":(5,23.2), "leo":(8,30.0), "ale":(0,0.0)}
    print(promedio_de_salidas(r3))
    r4 = {"agus": [58,58,58,0,61,58], "leo": [0,0,0,0,61,54], "ale": [14,13,0,61,10,12]}  #{"agus":(4,58), "leo":(1,54), "ale":(4,12.25)}
    print(promedio_de_salidas(r4))
