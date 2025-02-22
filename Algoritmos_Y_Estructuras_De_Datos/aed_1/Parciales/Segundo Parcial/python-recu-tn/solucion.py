from queue import Queue as Cola
from typing import TypeVar 

T = TypeVar('T')

def pertenece (cadena: list[T], elem:T) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False

#Ej 1 palabras_por_consonantes
def palabras_por_consonantes (s:str)  -> dict[int, int]:
    res:dict[int, int] = {}

    palabras:list[str] = get_palabras(s)
    for p in palabras:
        cant_c:int = cant_consonantes(p)
        incrementar (res, cant_c)

    return res

def incrementar (dic:dict[int, int], v : int) -> bool:
    dic.keys()
    if pertenece (list(dic.keys()), v):
        dic[v] += 1
    else:
        dic[v] = 1


def cant_consonantes (s:str)  -> int:
    res:int  = 0
    for c in s:
        if es_consonante ( c):
            res += 1

    return res    

#c solo puede ser: caracteres entre 'a' y 'z' inclusive, entre 'A' y 'Z' inclusive. 
# No incluye espacios (' '), números ni símbolos especiales como 'á', 'ñ', '+', etc.
def es_consonante (c:str) -> bool:
    return not es_vocal (c)
    
def es_vocal (c:str) -> bool:
    return pertenece("aeiouAEIOU", c)         



def get_palabras (s:str)  -> list[str]:
    res:list[str] = []
    actual:str = ""

    for c in s:
        if c == ' ' or c == '\n':
            if actual != "":
                res.append(actual)
                actual = ""
        else:
            actual = actual + c

    if actual != "":
        res.append(actual)

    return res


#Ej 2 cantidad_de_filas_valle
def cantidad_de_filas_valle (m:list[:list[int]])  -> int:
    res:int = 0
    for f in m:
        if es_valle(f):
            res = res + 1
    
    return res

def es_valle (f:list[int])  -> bool:
    if len(f) < 3:
        return False  

    i:int = 1

    # Verifico que exista la parte decreciente
    while i < len(f) and f[i] < f[i - 1]:
        i += 1

    # Si no avanzó i, entonces no hay parte decreciente
    # or Si llegué al final, no habrá parte creciente
    if i == 1 or i == len(f):
        return False

    # Verifico que exista la parte creciente
    while i < len(f) and f[i] > f[i - 1]:
        i += 1

    # es valle si llegamos al final creciendo
    return i == len(f)


#Ej 3 aprobados_y_desaprobados
def aprobados_y_desaprobados(examenes: Cola[list[bool]], correctas: Cola[list[bool]]):
    correctas_tmp:Cola[list[bool]] = Cola()
    aprobados:Cola[list[bool]] = Cola()
    desaprobados:Cola[list[bool]] = Cola()

    while not examenes.empty():
        examen = examenes.get()
        correcta = correctas.get()
        correctas_tmp.put(correcta)

        if aprobo (examen, correcta):
            aprobados.put(examen)
        else:
            desaprobados.put(examen)

    #guardo primero las aprobadas
    while not aprobados.empty():
        examenes.put(aprobados.get())

    #y luego guardo las desaprobadas
    while not desaprobados.empty():
        examenes.put(desaprobados.get())

    #restauro las correctas
    while not correctas_tmp.empty():
        correctas.put(correctas_tmp.get())


def aprobo (examen:list[bool], correctas:list[bool]):
    cant_bien = 0
    cant_mal = 0
    for i in range(len(examen)):
        if examen[i] == correctas[i]:
            cant_bien += 1
        else:
            cant_mal += 1
    
    return cant_bien >= cant_mal
    
    
#Ej 4 geometrica2_mas_larga
def geometrica2_mas_larga (lista:list[int]) ->  tuple[int, int]:
    long_max:int = 1
    pos_fin:int = 0  
    long_actual:int = 1 

    for i in range(1, len(lista)):
        if lista[i] == 2 * lista[i - 1]:  
            long_actual += 1
            if long_actual > long_max:
                long_max = long_actual
                pos_fin = i
        else:
            long_actual = 1  

    return (long_max, pos_fin)
