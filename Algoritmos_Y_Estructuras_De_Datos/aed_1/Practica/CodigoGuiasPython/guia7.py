# @ Guia 7
"""
    Simbolos: Ǝ,
"""

def linea():
    print("----------------------------------")


"""------------------------------------------------
                    EJERCICIO 1
---------------------------------------------------"""

############################## Ej1.1 ##############################
"""
    Ej 1.1
    problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
        requiere: { T rue }
        asegura: { 
            (res = true) ↔ (Ǝ i ∈ Z : 0≤i<|s| ∧ s[i]=e)
        }
}
Implementar al menos de 3 formas distintas éste problema.
"""

def pertenece_1(s:list, e:int)->bool:
    """ En este caso, recorreremos toda la lista 
    para fijarnos si alguno cumple con la especificación"""
    mod_s:int = len(s)
    res:bool = False

    for i in range(0,mod_s):
        print(i)
        print(f's[{i}]={s[i]}=={e}?')
        if s[i]==e:
            res=True
    return res    

def pertenece_2(s:list, e:int)->bool:
    """ En este caso, recorreremos la lista 
    pata fijarnos si alguno cumple con la especificación
    pero si encruentra algun valor corta y no itera en 
    el resto de la lista, ya que con uno ya basta"""
    mod_s:int = len(s)
    res:bool = False
    cont:int = 0
    while cont<mod_s:
        print(f's[{cont}]={s[cont]}, cont: {cont}, e:{e}')
        if s[cont]==e:
            cont+=1
            res=True
        else:
            cont+=1
    return res

def pertenece(s:list, e:int)->bool:
    """ Mezcla de los dos algoritmos anteriores. 
        Si se satisface la condicion retorno True
        sin seguir iterando"""
    for i in range(0,len(s)):
        if s[i]==e:
            return True
    return False    

############################## Ej1.2 ##############################

def divide_a_todos(s:list[int],e:int)->bool:
    """
        problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
            requiere: {e ̸= 0 }
            asegura: { 
                (res = true) ↔ (para todo i∈Z si 0≤i<|s| → s[i] mod e = 0)
            }
        }
    """
    for i in range(0,len(s)):
        print(f'{i+1}) mod s[{i}] {e} = {s[i]%e}')
        if s[i]%e!=0:            
            return False  
    return True

############################## Ej 1.3 ##############################
def suma_total(s:list[int])->int:
    """
        problema suma_total (in s:seq⟨Z⟩) : Z {
            requiere: { T rue }
            asegura: { res es la suma de todos los elementos de s}
        }

        Nota: no utilizar la funci´on sum() nativa
    """
    res:int = 0
    for i in s:
        res+=i
    return res

############################## Ej 1.4 ##############################
def maximo(s:list[int])->int:
    """
        problema maximo (in s:seq⟨Z⟩) : Z {
            requiere: {|s| > 0 }
            asegura: { res = al mayor de todos los n´umeros que aparece en s}
        }
    """
    aux:int = 0
    for i in s:
        if i>=aux:
            aux = i
    return aux

############################## Ej 1.5 ##############################
def minimo(s:list[int])->int:
    """
    problema minimo (in s:seq⟨Z⟩) : Z {
            requiere: {|s| > 0 }
            asegura: { res = al menor de todos los n´umeros que aparece en s}
        }   
    """
    aux:int = s[0]
    for i in s:
        if i<=aux:
            aux = i
    return aux

############################## Ej 1.6 ##############################
def ordenados(s:list[int])->bool:
    """
    problema ordenados (in s:seq⟨Z⟩) : Bool {
            requiere: { True }
            asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
        }  
    """
    a : bool = False
    for i in range (0 , len(s)-1 , 1):
        if s[i] < s[i+1]:
            a = True
        else :
            return False

    return a
############################## Ej 1.7 ##############################
def pos_maximo(s:list[int])->int:
    """
    problema pos maximo (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
                    de s (si hay varios es la primera aparici´on)}
        }
    """
    if len(s)==0:
        return -1
    else:
        indice:int=0
        for i in range(0 , len(s) , 1):
            if s[i] > s[indice]:
                indice = i
            else:
                indice = i+1
        return indice

############################## Ej 1.8 ##############################
def pos_minimo(s:list[int])->int:
    """
    problema pos minimo (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
                    de s (si hay varios es la ´ultima aparici´on)}
    }
    """
    if len(s)==0:
        return -1
    else:
        indice:int=0
        for i in range(0 , len(s) , 1):
            if s[i] < s[indice]:
                indice = i
    
        return indice

############################## Ej 1.9 ##############################
def palabra_de_menos_de_siete_letras(s:list[str])->bool:
    """
        Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. 
        Ejemplo: [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
    """
    for palabra in s:
        contador:int = 0
        for letra in palabra:
            contador+=1
            if contador>7:
                return True
    if contador<=7:
        return False
   
############################## Ej 1.10 ##############################           
def quitar_espacios_vacios(cadena:str)->str:
    newCadena:str=""
    for i in cadena:
        if i != " ":
            newCadena = newCadena + i
    return newCadena

def invertir_string(cadena:str)->str:
    newCadena:str = ""
    n:int=len(cadena)
    for caracter in cadena:
        newCadena = newCadena + cadena[n-1]
        n=n-1
    return newCadena

def es_palidromo(cadena:str)->bool:
    """
        Dado un texto en formato string, devolver verdadero si es palindromo 
        (se lee igual en ambos sentidos), falso en caso contrario. 
        Las cadenas de texto vacias o con 1 solo elemento son palindromo.
    """
    cadenaSinEspacios:str = quitar_espacios_vacios(cadena)
    inversaCadena:str = invertir_string(cadenaSinEspacios) 
    return cadenaSinEspacios==inversaCadena

############################## Ej 1.11 ############################## 
def tres_numeros_consecutivos_iguales(enteros:list[int])->bool:
    """
        Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 numeros iguales 
        consecutivos, en cualquier posicion y False en caso contrario.
    """
    contador:int=0
    for indice in range(0,len(enteros)-1):
        if enteros(indice)==enteros(indice+1):
            contador = 1
        if contador == 3:
            return True
    return False
############################## Ej 1.12 #############################     
def tiene_tres_o_mas_vocales_distintas(cadena:str)->bool:
    """
        Recorrer una palabra en formato string y devolver True si ésta 
        tiene al menos 3 vocales distintas y False en caso contrario.
    """
    contadores:list[int]=[0,0,0,0,0]
    cuento_vocales:int=0
    for i in cadena:
        if i=='a':
            contadores[0]+=1
        if i=='e':
            contadores[1]+=1
        if i=='i':
            contadores[2]+=1
        if i=='o':
            contadores[3]+=1
        if i=='u':
            contadores[4]+=1
    for vocal in contadores:
        if vocal != 0:
            cuento_vocales+=1
    if cuento_vocales>=3:
        return True
    else:
        return False 
# Una forma mucho mas optimizada
def vocales_distintas(s: str) -> bool:
    vocales: list[str] = ['a','e','i','o','u']
    vocales_palabra: list[str] = []

    for i in range(len(s)):
        if s[i] in vocales and s[i] not in vocales_palabra:
            vocales_palabra.append(s[i])
    
    if len(vocales_palabra) >= 3:
        return True
    return False
############################## Ej 1.13 #############################   
"""
Recorrer una seq⟨Z⟩ y devolver la posicion donde inicia la secuencia 
de numeros ordenada mas larga. Si hay dos subsecuencias de igual 
longitud devolver la posicion donde empieza la primera. 
La secuencia de entrada es no vacia.
"""
def posicion_secuencia_ordenada_mas_larga(lista:list[int])->int:
    pass

def sec_ordenada(s: list[int]) -> int:
    cantidad: int = 0
    indice: int
    cantidad_mayor: int = 0
    indice_mayor: int

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] + 1 == s[i + 1]:
            if cantidad == 0:
                indice = i
            cantidad += 1
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                indice_mayor = indice
        else:
            cantidad = 0

    return indice_mayor
############################## Ej 1.14 #############################
"""
Cantidad de digitos impares.
    problema cantidad digitos impares (in s:seq⟨Z⟩) : Z {
        requiere: {Todos los elementos de numeros son mayores o iguales a 0}
        asegura: {res es la cantidad total de digitos impares que aparecen en cada uno de los elementos de numeros}
    }
Por ejemplo, si la lista de numeros es [57, 2383, 812, 246], entonces el resultado esperado seria 5 (los digitos impares
son 5, 7, 3, 3 y 1).
def cantidad_digitos_impares(lista:list[int])->int:
    pass
"""

def cant_digitos_impares(s: list[int]) -> int:
    contador_impares: int = 0

    for numero in s:
        numero = str(numero) # cambio la variable del numero de int a str
        indice = 0
        while indice < len(numero):
            digito = int(numero[indice]) # para poder operar con el numero lo vuelvo int
            if digito % 2 != 0:
                contador_impares += 1
            indice += 1
    return contador_impares
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Recorrido: Filtrado, modificado y procesando secuencias
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

############################## Ej 2.1 #############################
def es_par(entero:int)->bool:
    return entero % 2 == 0

def cerosEnPosicionesPares(s:list[int])->list[int]:
    """
    problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
        requiere: { True }
        modifica: {s}
        asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
                    es par, entonces s[i] = 0)}
    }
    """
    for numero in range(0, len(s)-1):
        if es_par(numero):
            s[numero]=0
    return s
############################## Ej 2.2 #############################
def cerosEnPosicionesPares2(s:list[int])->list[int]:
    res = s.copy()
    for i in range(0, len(res)):
        if i % 2 == 0:
            res[i] = 0
    return res

############################## Ej 2.3 #############################
def es_vocal(letra:str)->bool:
    vocales:list[str]=["a","A","e","E","i","I","o","O","u","U"]
    for vocal in vocales:
        if letra == vocal:
            return True
    return False

def reemplazar_caracter(cadena, viejo, nuevo):
    """Funciona similar a la funcion replace"""
    resultado = ""
    for caracter in cadena:
        if caracter == viejo:
            resultado += nuevo
        else:
            resultado += caracter
    return resultado


def sacar_vocales(s:str)->str:
    """
        Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. 
        No se agregan espacios, sino que borra la vocal y concatena a continuacion.
    """
    new_s:str=s
    for letra in s:
        if es_vocal(letra):
            new_s=reemplazar_caracter(new_s,letra,"")
    return new_s


############################## Ej 2.4 #############################
def reemplaza_vocales(s:str)->list[int]:
    """
    problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {|res| = |s|}
        asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = '_') ||
                 (¬ pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = s[i] ) ) }
    }
    """
    new_s:str=s
    for letra in s:
        if es_vocal(letra):
            new_s=reemplazar_caracter(new_s,letra,"_")
    return new_s

############################## Ej 2.5 #############################
def da_vuelta_str (s:str)->str:
    """
    problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {|res| = |s|}
        asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1]}
    }
    """
    res:str=""
    for i in range(0,len(s)):
        res += s[len(s)-i-1]
    return res
    

############################## Ej 2.6 #############################
def pertenece_mas_de_una_vez(palabra:str, letra:str):
    contador:int=0
    for p in palabra:
        if p==letra:
            contador+=1
    return contador>=1

def eliminar_repetidos(s:str)->str:
    """
    problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
                  (0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j])}
    }
    """
    new_palabra:str=""
    
    for i in s:
        if pertenece_mas_de_una_vez(new_palabra,i):
            new_palabra+=""
        else:    
            new_palabra+=i
    return new_palabra    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 3. Implementar una función para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
#               por un/a alumno/a cumpliendo con la siguiente especificaci´on:
#    problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
#        requiere: {|notas| > 0}
#        requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
#        asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
#        asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7}
#        asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
#    }
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def son_mayoresOiguales_a_cuatro(notas:list[int])->bool:
    for i in notas:
        if i<=4:
            return False
    return True

def resultado_materia(notas:list[int])->int:
    #    resultado_materia (in notas: seq⟨Z⟩) : Z {
    #        requiere: {|notas| > 0}
    #        requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
    #        asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
    #        asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7}
    #        asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
    #    }
    promedio:float = suma_total(notas)/len(notas)
    
    if son_mayoresOiguales_a_cuatro(notas) and promedio>=7:
        return 1
    elif son_mayoresOiguales_a_cuatro(notas) and 4<=promedio<7:
        return 2
    else:
        return 3
    

# # # # # # # # # # # # # # 
#
#         MATRICES 
# 
# # # # # # # # # # # # # #

############################## Ej 5.1 #############################
"""
    Deberias pensar los demas casos. Igual, desde mi perspectiva, este 
    es el ejercicios que sirve, los otros son medio falopa
"""
def pertenece_a_cada_uno_version_1(s:list[list[int]],e:int)->list[bool]:
    """
    problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
        requiere: { True }
        asegura: { |res| ≥ |s|}
        asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e))}
    }
    Nota: Reutilizar la funci´on pertenece() implementada previamente para listas.
    """
    res:list[bool] = []

    for lista in s:
        res.append(pertenece(lista,e))
    return res

############################## Ej 5.2 #############################
def es_matriz(s:list[list[int]])->bool:
    """
    problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
        requiere: { True }
        asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}
    }
    """
    if len(s)<=0 or len(s[0])<=0:
        return False
    else:
        for lista in s:
            if len(s[0]) != len(lista):
                return False
        return True

############################## Ej 5.3 #############################    
def filas_ordenadas(M:list[list[int]],res:list[bool]):
    for fila in M:
        res.append(ordenados(fila))        

############################## Ej 5.4 #############################
def columna(M:list[list[int]],c:int)->list[int]:
    """problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
        requiere: { esMatriz(m)}
        requiere: { c < |m[0]|}
        requiere: { c ≥ 0}
        asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
        el mismo orden que aparecen}
    }
    notar: c es el numero de la columna que quiero
    """
    res:list[int] = []

    for fila in M:
        res.append(fila[c])
    return res

############################## Ej 5.5 #############################
def columna_ordenada(M:list[list[int]])->list[list[int]]:
    """
    problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
        requiere: { esMatriz(m)}
        asegura: { Para toda columna c ∈ m → (res[c] = true ↔ ordenados(columna(m, c))) }
    }
    Nota: Reutilizar la funci´on ordenados() implementada previamente para listas
    """    
    res:list[int] = []
    for columna in M:
        res.append(ordenados(columna))