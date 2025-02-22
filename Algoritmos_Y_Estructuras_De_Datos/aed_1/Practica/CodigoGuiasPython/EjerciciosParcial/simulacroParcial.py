""""""
# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7
##########################################

def ultima_aparicion(s:list[int],e:int)->int:
    res:int=0

    for i in range(len(s)):
        if s[i]==e:
            res = i
    return res

""""""
# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]
""""""
def pertenece_a_la_lista(elemento:int, lista:list[int])->bool:
    for e in lista:
        if e == elemento:
            return True
    return False
def elementos_exclusivos(s:list[int], t:list[int])->list[int]:
    res:list[int]=list()
    for i in s:
        for j in t:
            if not pertenece_a_la_lista(i,t) and not pertenece_a_la_lista(i,res):
                res.append(i)
            if not pertenece_a_la_lista(j,s) and not pertenece_a_la_lista(j,res):
                res.append(j)
            
    return res
    
""""""
# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

# recorro las keys (claves) de ingles y me fijo a la vez si pertenece a la lista de keys (claves) de aleman Y si 
# el valor de la clave en ambas listas es igual. OJO: si pongo los dos operadores logicos en orden inverso (o sea
# digamos si pongo primero la igualdad y luego el pertenece), como no me estoy asegurando de que la clave EXISTE
# en el diccionario de palabras en aleman, el programa SE ROMPE o algo asi en realidad no se bien que pasa pero
#  no esta bueno.
""""""
def contar_traducciones_iguales(ing:dict[str,str],ale:dict[str,str])->int:
    res:int=0
    for ki,vi in ing.items():
        for ka,va in ale.items():
            if ki==ka and vi==va:
                res+=1
    
    return res



""""""
# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
""""""
def contar_en_lista(numero:int, lista:list[int])->int:
    res:int=0
    for elemento in lista:
        if elemento==numero:
            res+=1
    return res

def convertir_a_diccionario(lista:list[int])->dict[int,int]:
    res:dict[int,int] = dict()

    for elemento in lista:
        res[elemento]=contar_en_lista(elemento, lista)
    
    return res
