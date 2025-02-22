"""
4) Subsecuencia más larga de salidas [3 puntos]

Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona,
escribir una función en Python que devuelva una tupla con el índice de inicio y el índice de fin de la
subsecuencia más larga de salidas exitosas de salas de escape consecutivas.

problema racha_mas_larga (in tiempos: seq⟨Z⟩): ⟨Z x Z⟩ {
  requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive}
  asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga}
  asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga}
  asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {La primera posición de res es menor o igual a la segunda posición de res }
  asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res}
  asegura: {
    No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer 
    posición de res y la segunda posición de res
  }
  asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
}
"""
def posicion_maximo_en_lista(numeros:list[int])->int:
    posicion_maximo:int=0
    valor_maximo:int = numeros[0]

    for indice in range(1,len(numeros)):
        if numeros[indice]>valor_maximo:
            valor_maximo = numeros[indice] 
            posicion_maximo=indice
           
        
    return posicion_maximo

#(posicionInicialRacha,posiciónFinalRacha)
def racha_mas_larga (tiempos:list[int])->list[tuple[int,int]]:
    posicion_inicial:int = 0
    posicion_Final:int = 0

    contador:int = 0 

    rachas:list[int] = list() # Se va a encargar de medir la longitud maxima
    lista_tuplas:list[tuple[int,int]] = list()
    
    tiempos.append(0) # Le agrego un cero porque sino no logro que frene

    for indice in range(len(tiempos)):
        
        if 0<tiempos[indice]<61 and contador==0:
            contador+=1
            posicion_inicial=indice
            
        elif 0<tiempos[indice]<61 and contador>0:
            contador+=1
            posicion_Final=indice
            
        elif 0==tiempos[indice] or tiempos[indice]==61:
            lista_tuplas.append((posicion_inicial,posicion_Final))
            rachas.append(contador)
            contador=0
            posicion_inicial = 0
            posicion_Final = 0

    return lista_tuplas[posicion_maximo_en_lista(rachas)]


if __name__ == "__main__":
    lista:list[int] = [1,1,2,0,6,3,0,3,3,4,1,1,0]
    print(racha_mas_larga(lista))
