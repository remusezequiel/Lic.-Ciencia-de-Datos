import random
import typing
from queue import LifoQueue as Pila
from queue import Queue as Cola

# EJERCICIO 1
# 1)
def pertenece(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if(e == s[i]):
            return True
    return False

def pertenece2(s: list[int], e: int)-> bool:
    longitud = len(s) - 1

    while(longitud >= 0):
        if(s[longitud] == e):
            return True
        longitud -= 1
    return False

print(pertenece([1,2,3], 4))
print(pertenece([1,2,3], 2))
print(pertenece2([1,2,3], 4))
print(pertenece2([1,2,3], 2))

# 2)
def divide_a_todos(s: list[int], e: int) -> bool:
    indice = len(s) - 1 

    while(indice >= 0):
        if(s[indice] % e != 0):
            return False
        indice -= 1
    return True

print(divide_a_todos([2,4,6], 2))
print(divide_a_todos([2,5,6], 2))
print(divide_a_todos([3,4,6], 2))
print(divide_a_todos([24,36,48], 12))
print(divide_a_todos([12,25,48], 12))
print(divide_a_todos([7,9,13], 2))

# 3) 
def suma_total(s: list[int]) -> int:
    total: int = 0   # la suma empieza en el 0, y despues voy sumando los valores de la lista
    indiceActual: int = 0

    while(indiceActual < len(s)):
        valorActual: int = s[indiceActual]
        total += valorActual
        indiceActual += 1   # me muevo un lugar en la lista
    return total

# otra opcion:
# def suma_total(s: list[int]) -> int:
#     total: int = 0
#     for i in range(0, len(s)):
#         total += s[i]
#     return total

print(suma_total([1,2,3]))

# 4)
def maximo(s: list[int]) -> int:
    maximo: int = s[0]

    for i in range(len(s)):
        if s[i] > maximo:
            maximo = s[i]
    return maximo

# 5) 
def minimo(s: list[int]) -> int:
    minimo: int = s[0]

    for i in range(len(s)):
        if s[i] < minimo:
            minimo = s[i]
    return minimo

# 6) 
def ordenados(s: list[int]) -> bool:
    indice_mayor = len(s) - 1
    indice_menor = indice_mayor - 1

    while(indice_menor >= 0):
        if s[indice_menor] < s[indice_mayor]:   # se recorre la lista de atras hacia adelante
            return True
        return False

print(ordenados([2,3,4]))
print(ordenados([2,4,3]))
print(ordenados([12,13,14,100,99]))
print(ordenados([3,2,1]))
print(ordenados([1,2,4,8]))

# 7)
def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        maximo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] > maximo:
                maximo = s[i]
                indice = i
        return indice
    
print(pos_maximo([1,2,4,56,2]))
print(pos_maximo([56,2,4,56,2]))

# 8) 
def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        minimo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] <= minimo:
                minimo = s[i]
                indice = i
        return indice
    
print(pos_minimo([1,2,4,56,2]))
print(pos_minimo([56,2,4,56,2]))

# 9)
def longitudes(s: list[str]) -> bool:
    for i in range (0, len(s)):
        if (len(s[i])) > 7:
            return True
    return False

print(longitudes(['termo', 'gato', 'tener', 'jirafas']))
print(longitudes(['termo', 'gato', 'tener', 'jirafitas']))

# 10)
def palindromos(palabra: str) -> bool:
    indice: int = 0
    
    while indice < len(palabra):
        if palabra[indice] != palabra[len(palabra) - 1 - indice]:
            return False
        indice += 1
    return True

print(palindromos("hannah"))
print(palindromos("agus"))

# 11)
def num_iguales(s: list[int]) -> bool:
    indice: int = 0
    indice_mayor: int = 1
    contador_iguales: int = 0

    while indice_mayor < len(s):
        if s[indice] == s[indice_mayor]:
            contador_iguales += 1
            if contador_iguales == 2:
                return True
            indice += 1
            indice_mayor += 1
        else:
            contador_iguales = 0
            indice += 1
            indice_mayor += 1
    return False
    
print(num_iguales([1,1,1,56,2]))
print(num_iguales([1,2,4,4,2,56,2]))

# 12)
def vocales_distintas(s: str) -> bool:
    vocales: list[str] = ['a','e','i','o','u']
    vocales_palabra: list[str] = []

    for i in range(len(s)):
        if s[i] in vocales and s[i] not in vocales_palabra:
            vocales_palabra.append(s[i])
    
    if len(vocales_palabra) >= 3:
        return True
    return False
    
print(vocales_distintas('agustina'))
print(vocales_distintas('alamo'))

# 13) 
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

print(sec_ordenada([1,2,3,0,1,2,3,4,0,1,2,3]))
print(sec_ordenada([0,1,2,0,10,11,12,13]))
print(sec_ordenada([0,1,2,3,0,1,2,3,0,1,2,3]))

# 14)
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

print(cant_digitos_impares([57, 2383, 812, 246]))
print(cant_digitos_impares([22,46,88,26]))
print(cant_digitos_impares([22,46,88,26,77,54]))

# EJERCICIO 2
# 1)
def posiciones_pares(lista: list[int]) -> list[int]:
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista[i] = 0
    return lista

a : list[int] = [3,3,3,3,3,3]
print(a)
print(posiciones_pares(a)) 
print(a)

# 2)
def posiciones_pares2(lista: list[int]) -> list[int]:
    res = lista.copy()
    for i in range(0, len(res)):
        if i % 2 == 0:
            res[i] = 0
    return res

a : list[int] = [3,3,3,3,3,3]
print(a)
print(posiciones_pares2(a)) 
print(a)

# 3)
def sin_vocales(palabra: str) -> str:
    vocales: list[str] = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for i in palabra:
        if i in vocales:
            palabra = palabra.replace(i, "")
    return palabra

# 4)
def reemplaza_vocales(palabra: str) -> str:
    vocales: list[str] = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for i in palabra:
        if i in vocales:
            palabra = palabra.replace(i, "_")
    return palabra

# 5)
def dar_vuelta_str2(palabra: str) -> str:
    palabra_invertida: str = ""
    i: int = 0

    while i < len(palabra):
        letra = palabra[len(palabra) - 1 - i]
        palabra_invertida += letra
        i += 1
    return palabra_invertida

# 6)
def pertenece_mas_de_una_vez(palabra: str, letra: str) -> bool:
    repeticiones: int = 0

    for i in range(0, len(palabra)):
        if letra == palabra[i]:
            repeticiones += 1
    
    if repeticiones > 1:
        return True
    return False

def eliminar_repetidos(palabra: str) -> str:
    palabra_sin_repetidos: str = ""
    indice: int = 0

    while indice < len(palabra):
        if pertenece_mas_de_una_vez(palabra, palabra[indice]):
            palabra_sin_repetidos = palabra_sin_repetidos + ""
            indice += 1
        else:
            palabra_sin_repetidos = palabra_sin_repetidos + palabra[indice]
            indice += 1
    return palabra_sin_repetidos

# EJERCICIO 3
# hago una funcion que indique si todas las notas de la lista estan aprobadas
def notas_aprobadas(notas: list[int]) -> bool:
    indice: int = 0

    while indice < len(notas):
        if notas[indice] >= 4:
            indice += 1
            return True
        return False

# hago una funcion que sume la cantidad de notas de la lista
def notas_totales(notas: list[int]) -> bool:
    indice: int = 0
    cantidad_de_notas: int = 0

    while indice < len(notas):
        if 0 <= notas[indice] <= 10:
            cantidad_de_notas += 1
            indice += 1
    return cantidad_de_notas

# hago una funcion que me indique el promedio de notas de la lista
def promedio(notas: list[int]) -> float:
    indice: int = 0
    suma_total_notas: int = 0

    while indice < len(notas):
        suma_total_notas += notas[indice]
        indice += 1
    return (suma_total_notas/notas_totales(notas))

def aprobado(notas: list[int]) -> int:
    if notas_aprobadas(notas) and promedio(notas) >= 7:
        return 1
    elif notas_aprobadas(notas) and 4 <= promedio(notas) < 7:
        return 2
    elif notas_aprobadas(notas) == False or promedio(notas) < 4:
        return 3

print(aprobado([7,8,9,10]))
print(aprobado([5,6,7]))
print(aprobado([1,10,10]))
print(aprobado([1,2,3]))

# EJERCICIO 4
def movimientos_bancarios(historial: list[(str, int)]) -> int:
    saldo: int = 0
    
    for operacion in historial:
        if operacion[0] == "I":
            saldo += operacion[1]
        elif operacion[0] == "R":
            saldo -= operacion[1]
    return saldo

print(movimientos_bancarios([('I',2000), ('R', 20),('R', 1000),('I', 300)]))

# EJERCICIO 5
# 1)
def pertenece (e: int, l: list[int]) -> bool:
    for i in range(len(l)):
        if e == l[i]:
            return True
    return False

def pertenece_a_cada_uno_version_1(s: list[int], e: int, res: list[bool]) -> None:
    res.clear()
    for i in range(len(s)):
        res.append(pertenece(e, s[i]))
    return res

print(pertenece_a_cada_uno_version_1([[4,5,6], [7,8,10], [4,4,4]], 4, [True, False, True]))

# 2)
def pertenece (e: int, l: list[int]) -> bool:
    for i in range(len(l)):
        if e == l[i]:
            return True
    return False 

def pertenece2 (e: int, l: list[int]) -> bool:   # otra forma de hacer el pertenece 
    for elem in l:
        if e == elem:
            return True

def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    # respuesta_parcial = False
    # for i in range(len(s)):
    #     if pertenece (e, s[i]):
    #         respuesta_parcial = pertenece(e, s)
    #     else:
    #         respuesta_parcial = False
    #     res.append(respuesta_parcial)
    for i in range(len(s)):
        res.append(pertenece(e, s[i]))
    return res

res = [False, True, False]
s = [[1, 2, 3], [2, 3, 4], [1]]
e = 4
print(pertenece_a_cada_uno_version_2(s, e, res))

# EJERCICIO 6
# 1)
def es_matriz(s: list[list[int]]) -> bool:
    indice: int = 0

    while indice < len(s):
        if len(s[0]) != len(s[indice]):
            return False
        else:
            indice += 1
    return True

# 2)
def filas_ordenadas(m: list[int], res: list[bool]) -> None: 
    res: list[bool] = []
    indice = 0

    while indice < len(m):
        res.append(ordenados(m[indice]))
        indice += 1
    return res

m = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
res = [True, True, True]
print(filas_ordenadas(m, res))

a = [[3,2,1], [1,2,3], [4,5,6], [7,8,9]]
res = [False, True, True, True]
print(filas_ordenadas(a, res))

z = [[1,2], [2,3], [3,4], [2,1]]
res = []
print(filas_ordenadas(z, res))

# 3)
def columna(s: list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    
    for fila in s:
        elemento: int = fila[c]
        res.append(elemento)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(columna(m1, 0)) # [1,4,12]
print(columna(m1, 2)) # [3,6,9]

# 4)
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []

    for i in range(len(m[0])): # como es matriz da igual el indice que tome
        if ordenados(columna(m, i)):
            res.append(True)
        else:
            res.append(False)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(columnas_ordenadas(m1))
m2 = [[1,4,5,6],
      [0,7,8,9],
      [3,8,6,1]]
print(columnas_ordenadas(m2))

# 5)
def transponer(m: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []

    for i in range(len(m[0])):
        fila = columna(m,i)
        res.append(fila)
    return res

m1 = [[1,2,3],
      [4,5,6],
      [12,8,9]]
print(transponer(m1))
m2 = [[1,4,5,6],
      [0,7,8,9],
      [3,8,6,1]]
print(transponer(m2))
m3 = [[1,2,3],
      [4,5,6],
      [7,8,9],
      [10,11,12]]
print(transponer(m3))

# 6)
# hago una funcion auxiliar que me diga si en alguna de las filas hay tres letras iguales consecutivas de forma horizontal
def alineados_en_fila(m: list[list[str]], letra: str) -> bool:
    for fila in m:
        contador: int = 0
        indice: int = 0
        indice_siguiente: int = 1
        while indice_siguiente < len(fila):
            elemento: str = fila[indice]
            if elemento == letra and fila[indice_siguiente] == letra:
                contador += 1
                if contador == 2:
                    return True
                else:
                    indice += 1
                    indice_siguiente += 1
            else:
                indice += 1
                indice_siguiente +=1
    return False

m1 = [['c','c','c'],
      ['b','c','d']]
print(alineados_en_fila(m1, 'c'))
m2 = [['c','h','c'],
      ['b','c','d']]
print(alineados_en_fila(m2, 'c'))

# hago una funcion auxiliar similar a columna que me diga si hay tres letras iguales consecutivas en forma vertical
def letras_verticales(s: list[list[str]], letra: str) -> bool:
    res: list[int] = []
    
    for fila in s:
        for i in range(len(fila)):
            if fila[i] == letra:
                res.append(i)
    
    if len(res) == 3:
        return True
    else:
        return False
    
m1 = [['x','h','l'],
      ['x','n','z'],
      ['x','o','y']]
print(letras_verticales(m1,'x'))
m2 = [['x','h','l'],
      ['o','n','z'],
      ['x','o','y']]
print(letras_verticales(m2,'x'))
m3 = [['u','h','l'],
      ['v','n','z'],
      ['z','o','y']]
print(letras_verticales(m3,'x')) 

# hago una funcion auxiliar que me diga si hay tres letras iguales en forma diagonal
def diagonales(s: list[list[int]], letra: str) -> bool:
    res: list[int] = []

    for fila in s:
        for i in range(len(fila)):
            if fila[i] == letra:
                res.append(i)
    
    contador: int = 0
    indice: int = 0
    indice_mayor: int = 1
    while indice_mayor < len(res):
        if res[indice] + 1 == res[indice_mayor] or res[indice] - 1 == res[indice_mayor]:
            contador += 1
            indice += 1
            indice_mayor += 1
            if contador == 2:
                return True
        else:
            return False

m1 = [['x','o','l'],
      ['u','x','n'],
      ['q','w','x']]
print(diagonales(m1,'x'))
m2 = [['x','o','l'],
      ['u','z','n'],
      ['q','w','x']]
print(diagonales(m2,'x'))
m3 = [['t','o','x'],
      ['u','x','n'],
      ['x','w','l']]
print(diagonales(m3,'x'))

def quien_gana_tateti(m: list[str]) -> int:
    if alineados_en_fila(m, 'O') or letras_verticales(m, 'O') or diagonales(m, 'O'):
        return 0
    elif alineados_en_fila(m, 'X') or letras_verticales(m, 'X') or diagonales(m, 'X'):
        return 1
    else:
        return 2
    
t1 = [['O','','X'],
      ['O','',''],
      ['O','X','']] #0
print(quien_gana_tateti(t1))
t2 = [['O','','X'],
      ['','X',''],
      ['X','','']] #1
print(quien_gana_tateti(t2))

# EJERCICIO 7
# 1)
def construir_lista() -> list[str]:
    lista: list[str] = []
    nombre = input("Indique el nombre: ")
    
    while nombre != "listo":
        lista.append(nombre)
        nombre = input("Indique el nombre: ")
    return lista

print(construir_lista())

# 2)
def monedero_electronico() -> None:
    monedero = 0
    operacion = ""
    historial: list[(str, int)] = []
    
    while operacion != "X":
        operacion = input("Indique la operación ('C': cargar, 'D': descontar, 'X': finalizar): ")
        if operacion == "C":
            monto = int(input("Indique el monto para la operación: "))
            monedero += monto
            historial.append(("C", monto))
        elif operacion == "D":
            monto = int(input("Indique el monto para la operación: "))
            monedero -= monto
            historial.append(("D", monto))
    print("Su dinero es de $"+str(monedero)+".")
    return("Su historial de operaciones es "+str(historial)+".")

print(monedero_electronico())

# 3)
# aca la re vivi jajajaj, seguro se puede hacer una versión más simple
def siete_y_medio() -> None:
    suma_numeros = 0
    numero_aleatorio = ""
    eleccion = ""
    historial: list[int] = []

    while eleccion != "P":  
        if suma_numeros < 7.5:
            eleccion = input("¿Desea sacar una carta o plantarse? ('C': sacar otra carta, 'P': plantarse): ")
            if eleccion == "C":
                numero_aleatorio = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
                print("Su carta es "+str(numero_aleatorio)+"")
                historial.append(numero_aleatorio)
                if (numero_aleatorio == 10 or numero_aleatorio == 11 or numero_aleatorio == 12):
                    suma_numeros += 0.5
                    if suma_numeros == 7.5:
                        print("¡Ganaste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                    elif suma_numeros > 7.5:
                        print("¡Perdiste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                else:
                    suma_numeros += numero_aleatorio
                    if suma_numeros == 7.5:
                        print("¡Ganaste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
                    elif suma_numeros > 7.5:
                        print("¡Perdiste el juego! Tu puntaje es de "+str(suma_numeros)+".")
                        return("Las cartas que te tocaron fueron: "+str(historial)+".")
    print("¡Terminó el juego! Tu puntaje fue de "+str(suma_numeros)+".")
    return("Las cartas que te tocaron fueron: "+str(historial)+".")      

print(siete_y_medio())

# 4)
def al_menos_una_mayus(contraseña: str) -> bool:
    res = False
    for letra in contraseña:
        if 'A' <= letra <= 'Z':
            res = True
    return res

def al_menos_una_minus(contraseña: str) -> bool:
    res = False
    for letra in contraseña:
        if 'a' <= letra <= 'z':
            res = True
    return res

def al_menos_un_numero(contraseña: str) -> bool:
    res = False
    for num in contraseña:
        if '0' <= num <= '9':
            res = True
    return res

def fortaleza(contraseña: str) -> str:
    if al_menos_una_mayus(contraseña) and al_menos_una_minus(contraseña) and al_menos_un_numero(contraseña) and len(contraseña) > 8:
        return "VERDE"
    elif len(contraseña) < 5:
        return "ROJA"
    else:
        return "AMARILLA"
    

##############
#   GUIA 8
##############
# import random

# PILAS
# EJERCICIO 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila = Pila()  # creo una pila vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

p = generar_nros_al_azar(3, 1, 10)
print(p.queue)   # la funcion queue devuelve los elementos de la pila como si fuese una lista

# EJERCICIO 2
def cantidad_elementos(p: Pila) -> int:
    cantidad: int = 0
    pila_clonada: Pila = Pila()
    otra_pila: Pila = Pila()
    
    while not p.empty():
        elem: int = p.get()
        pila_clonada.put(elem)
        otra_pila.put(elem)
    
    while not otra_pila.empty():
        otra_pila.get()
        cantidad += 1
    
    while not pila_clonada.empty():
        p.put(pila_clonada.get())
    
    return cantidad

p: Pila = generar_nros_al_azar(3, 1, 9)
print(p.queue)
print(cantidad_elementos(p))
print(p.queue)
m: Pila = generar_nros_al_azar(5, 1, 100)
print(m.queue)
print(cantidad_elementos(m))
print(m.queue)

# EJERCICIO 3 
def buscar_el_maximo(p: Pila[int]) -> int:
    pila_copiada: Pila = Pila()
    max: int = p.get()
    pila_copiada.put(max)

    while not p.empty():
        elem: int = p.get()
        pila_copiada.put(elem)
        if elem > max:
            max = elem
    
    while not pila_copiada.empty():
        p.put(pila_copiada.get())

    return max

p = generar_nros_al_azar(4, 1, 100)
print(p.queue)
print(buscar_el_maximo(p))
print(p.queue)

# EJERCICIO 4
def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    pila_copiada: Pila = Pila()
    maximo = p.get()
    pila_copiada.put(maximo)

    while not p.empty():
        elemento = p.get()
        pila_copiada.put(elemento)
        if elemento[1] > maximo[1]:
            maximo = elemento
    
    while not pila_copiada.empty():
        elemento = pila_copiada.get()
        p.put(elemento)

    return maximo

p = Pila()
p.put(("juan", 5))
p.put(("ale", 4))
p.put(("nico", 9))
print(p.queue)
print(buscar_nota_maxima(p))
print(p.queue)
p2 = Pila()
p2.put(("juan", 5))
p2.put(("ale", 4))
p2.put(("nico", 9))
p2.put(("jorge", 1))
print(p2.queue)
print(buscar_nota_maxima(p2))
print(p2.queue)

# EJERCICIO 6
def evaluar_expresion(expresion: str) -> float:
    tokens = expresion.split(" ")
    operadores: Pila = Pila()

    for token in tokens:
        if token in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            operadores.put(token)
        elif token in ["+", "-", "*", "/"]:
            n1 = int(operadores.get())
            n2 = int(operadores.get())
            if token == "+":
                operadores.put(n2 + n1)
            if token == "-":
                operadores.put(n2 - n1)
            if token == "*":
                operadores.put(n2 * n1)
            if token == "/":
                operadores.put(n2 / n1)
    return operadores.get()

expresion = "3 4 + 5 * 2 -"
print(evaluar_expresion(expresion))
expresion2 = "10 2 + 3 / 2 - 3 +"
print(evaluar_expresion(expresion2))

# EJERCICIO 7
def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_res: Pila = Pila()

    while not p1.empty() and not p2.empty():
        elemento1 = p1.get()
        elemento2 = p2.get()
        pila_res.put(elemento1)
        pila_res.put(elemento2)
    return pila_res.queue

p1 = Cola()
p1.put("hola")
p1.put("estas")
p1.put("re")
print(p1.queue)
p2 = Cola()
p2.put("como")
p2.put("yo")
p2.put("bien")
print(p2.queue)
print(intercalar(p1,p2))

# COLAS
# EJERCICIO 8
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()  # creo una Cola vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        c.put(n)
    return c

c = generar_nros_al_azar(4, 1, 200)
print(c.queue)

# EJERCICIO 9
def cantidad_elementos(c: Cola) -> int:
    cantidad: int = 0
    cola_clonada: Cola = Cola()
    otra_cola: Cola = Cola()
    
    while not c.empty():
        elem: int = c.get()
        cola_clonada.put(elem)
        otra_cola.put(elem)
    
    while not otra_cola.empty():
        otra_cola.get()
        cantidad += 1
    
    while not cola_clonada.empty():
        c.put(cola_clonada.get())
    
    return cantidad

c = generar_nros_al_azar(5, 1, 23108)
print(c.queue)
print(cantidad_elementos(c))
print(c.queue)

# EJERCICIO 10
def buscar_el_maximo(c: Cola[int]) -> int:
    max: int = c.get()
    elem: int
    cola_copiada: Cola = Cola()

    cola_copiada.put(max)

    while not c.empty():
        elem = c.get()
        if elem > max:
            max = elem
        cola_copiada.put(elem)

    while not cola_copiada.empty():
        c.put(cola_copiada.get())
    
    return max

c = generar_nros_al_azar(5, 1, 10)
print(c.queue)
print(buscar_el_maximo(c))
print(c.queue)

# EJERCICIO 11
def buscar_nota_minima(c: Cola[tuple[str, int]]) -> tuple[str, int]:
    cola_copiada: Cola = Cola()
    minimo = c.get()
    cola_copiada.put(minimo)

    while not c.empty():
        elemento = c.get()
        cola_copiada.put(elemento)
        if elemento[1] < minimo[1]:
            minimo = elemento
    
    while not cola_copiada.empty():
        elemento = cola_copiada.get()
        c.put(elemento)

    return minimo

c = Cola()
c.put(("juan", 5))
c.put(("ale", 4))
c.put(("nico", 9))
print(c.queue)
print(buscar_nota_minima(c))
print(c.queue)
c2 = Cola()
c2.put(("juan", 5))
c2.put(("ale", 4))
c2.put(("nico", 9))
c2.put(("jorge", 1))
print(c2.queue)
print(buscar_nota_minima(c2))
print(c2.queue)

# EJERCICIO 12
def intercalar(c1: Cola, c2: Cola) -> Cola:
    cola_res: Cola = Cola()

    while not c1.empty() and not c2.empty():
        elemento1 = c1.get()
        elemento2 = c2.get()
        cola_res.put(elemento1)
        cola_res.put(elemento2)
    return cola_res.queue

c1 = Cola()
c1.put("hola")
c1.put("estas")
c1.put("re")
print(c1.queue)
c2 = Cola()
c2.put("como")
c2.put("yo")
c2.put("bien")
print(c2.queue)
print(intercalar(c1,c2))

# EJERCICIO 13
# 1)
def armar_secuencia_bingo() -> Cola[int]:
    cola: Cola = Cola()   # creo una cola vacia
    lista: list[int] = list(range(0, 99))   # creo una lista con numeros del 0 al 99
    random.shuffle(lista)   # mezclo los numeros de la lista al azar

    for i in range(0, 99):
        cola.put(lista[i])
    return cola
    
# 2)
def crear_carton_de_bingo() -> list[int]:
    carton: list[int] = []
    lista_de_numeros: list[int] = list(range(0, 99))
    random.shuffle(lista_de_numeros)
    
    for i in range(0, 12):
        carton.append(lista_de_numeros[i])
    return carton

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cantidad_jugadas: int = 0
    cantidad_sin_marcar: int = len(carton)
    bolillero_copia: Cola = Cola()
    
    print(bolillero.queue)   # ver el bolillero antes de ser modificado
    while not bolillero.empty():
        num: int = bolillero.get()
        bolillero_copia.put(num)   # pongo en una copia del bolillero los numeros que saco del bolillero original
    
    while cantidad_sin_marcar != 0:
        num: int = bolillero_copia.get()
        if num in carton:
            cantidad_sin_marcar -= 1
            cantidad_jugadas += 1
            bolillero.put(num)
        else:
            cantidad_jugadas += 1 
            bolillero.put(num)
    
    while not bolillero_copia.empty():
        num: int = bolillero_copia.get()
        bolillero.put(num)   # vuelvo a poner los elementos de bolillero en la cola original
        
    print(carton)
    print(bolillero.queue)
    
    return cantidad_jugadas

print(jugar_carton_de_bingo(crear_carton_de_bingo(), armar_secuencia_bingo()))

# EJERCICIO 14
def n_pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int:
    urgentes: list[int] = [1, 2, 3]
    contador_urgentes: int = 0
    cola_copiada: Cola = Cola()

    while not c.empty():
        paciente = c.get()
        cola_copiada.put(paciente)
        if paciente[0] in urgentes:
            contador_urgentes += 1
    
    while not cola_copiada.empty():
        paciente = cola_copiada.get()
        c.put(paciente)

    return contador_urgentes

c: Cola = Cola()
c.put([1, "Ana", "Traumatologia"])
c.put([4, "Mercy", "Cardiologia"])
c.put([2, "Roadhog", "Endocrinologia"])
c.put([3, "Venture", "General"])
c.put([10, "Dva", "Cirugia"])
c.put([1, "Brigitte", "Traumatologia"])
print(c.queue)
print(n_pacientes_urgentes(c))
print(c.queue)

# EJERCICIO 15
def atencion_a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    cola_copiada: Cola = Cola()
    cola_copiada_aux: Cola = Cola()
    clientes_prioridad: Cola = Cola()
    clientes_preferencial: Cola = Cola()
    clientes_sin_prioridad: Cola = Cola()
    orden: Cola = Cola()

    while not c.empty():
        cliente = c.get()
        cola_copiada.put(cliente)
        cola_copiada_aux.put(cliente)

    while not cola_copiada.empty():
        cliente = cola_copiada.get()
        if cliente[3] == True:
            clientes_prioridad.put(cliente)
        elif cliente[2] == True:
            clientes_preferencial.put(cliente)
        else:
            clientes_sin_prioridad.put(cliente)
    
    while not clientes_prioridad.empty():
        orden.put(clientes_prioridad.get())

    while not clientes_preferencial.empty():
        orden.put(clientes_preferencial.get())

    while not clientes_sin_prioridad.empty():
        orden.put(clientes_sin_prioridad.get())

    while not cola_copiada_aux.empty():
        cliente = cola_copiada_aux.get()
        c.put(cliente)

    return orden.queue

c: Cola = Cola()
c.put(["ana", 9999, True, True]) #1
c.put(["dva", 9999, True, False]) #3
c.put(["mercy", 9999, False, False]) #5
c.put(["genji", 9999, False, True]) #2
c.put(["hanzo", 9999, True, False]) #4
c.put(["pharah", 9999, False, False]) #6
print(c.queue)
print(atencion_a_clientes(c))
print(c.queue)

# DICCIONARIOS
# EJERCICIO 16
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    res: dict[int, int] = {}   # creo un diccionario vacio
    archivo = open(nombre_archivo, "r")
    palabras_archivo: list[str] = archivo.read().split()   # .split() divide las palabras de un string
    archivo.close()
    
    for palabra in palabras_archivo:
        if len(palabra) not in res.keys():
            res[len(palabra)] = 1
        else:
            res[len(palabra)] += 1
    return res

# EJERCICIO 18
def cantidad_de_apariciones(nombre_archivo: str) -> dict:
    frecuencia: dict[str, int] = {}   # creo un diccionario vacio
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()   # separo lineas en palabras indivicuales
        for palabra in palabras:
            if palabra not in frecuencia:
                frecuencia[palabra] = 1
            else:
                frecuencia[palabra] += 1
    archivo.close()
    return frecuencia

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    frecuencia = cantidad_de_apariciones(nombre_archivo)
    palabra_mas_frecuente: str = ""
    frecuencia_maxima: int = 0

    for palabra, frecuencia in frecuencia.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            palabra_mas_frecuente = palabra
    return palabra_mas_frecuente

# EJERCICIO 20
inventario: dict = {}
inventario_aux: dict = {}

# 1) 
def agregar_producto(inventario: dict[str, dict[int, int]], nombre: str, precio: int, cantidad: int) -> None:
    if nombre not in inventario.keys():
        inventario_aux = {
            "precio": precio,
            "cantidad": cantidad,
    }
        inventario[nombre] = inventario_aux

# 2)
def actualizar_stock(inventario: dict, nombre: str, cantidad: str) -> None:
    if nombre in inventario.keys():
        inventario[nombre]["cantidad"] = cantidad

# 3)
def actualizar_precios(inventario: dict, nombre: str, precio: int) -> None:
    if nombre in inventario.keys():
        inventario[nombre]["precio"] = precio

# 4)
def calcular_valor_inventario(inventario: dict) -> float:
    valor_total_inventario: int = 0

    for producto in inventario.values():
        valor_total_inventario += producto["precio"] * producto["cantidad"]
    return valor_total_inventario

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)

# ARCHIVOS
# EJERCICIO 21
# 1)
def contar_lineas(nombre_archivo:str) -> int:   # el parámetro que recibe es el nombre del archivo
    arch = open(nombre_archivo, "r")   # primero hay que abrir el archivo
  # tmb se puede poner arch: typing.IO = open(nombre_archivo,"r"), declara el tipo de dato del archivo (IO) 
    cant_lineas: int
    lineas: list[str] = arch.readlines()
    cant_lineas = len(lineas)
    arch.close()   # debo cerrar el archivo y despues poner el return 
    return cant_lineas

# una forma de abrir el archivo
# archivitouwu = "/home/Estudiante/Escritorio/Practica8/archivitouwu"  # "copiar ruta de acceso"
# print(contar_lineas(archivitouwu))
# otra forma de abrir el archivo    

# 2)
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        if linea.count(palabra) >= 1:
            return True
    return False
    arc.close()

# 3)
def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    apariciones: int = 0

    for linea in lineas:
        apariciones += linea.count(palabra)
    archivo.close()
    return apariciones

# EJERCICIO 22
def es_comentario(linea: str)-> bool:
    i: int = 0 

    while (i < len(linea) and linea[i] == ' '):   # i < len(linea) es por si hay una linea con todos blancos, se puede indefinir sino
        i += 1
    return i < len(linea) and linea[i] == '#'  # va a ser true si la linea cumple con todo esto

print(es_comentario("#hla"))
print(es_comentario("     #ajkfhas"))
print(es_comentario("hola"))

def clonar_sin_comentarios(nombre_archivo: str) -> None:
    arch: typing.IO = open(nombre_archivo,"r")
    arch_clonado: typing.IO = open("clonado.txt","w")   # si hago open(nombre_archivo,"w") y nombre_archivo no existe, se crea uno nuevo
    lineas: list[str] = arch.readlines()

    for linea in lineas:
        if (not es_comentario(linea)):
            arch_clonado.write(linea)
    arch.close()
    arch_clonado.close()

# EJERCICIO 23
def invertir_lineas(nombre_archivo: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "r")
    archivo_clonado: typing.IO = open("reverso.txt", "w")
    lineas: list[str] = archivo.readlines()

    for i in range(-1, -(len(lineas)) - 1, -1):
        archivo_clonado.writelines(lineas[i] + "\n")
    archivo.close()
    archivo_clonado.close()

# EJERCICIO 24
def implementar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "a")

    archivo.write("\n" + frase)
    archivo.close()

# EJERCICIO 25
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = [frase + "\n"] + archivo.readlines()
    archivo.close()
    archivo: typing.IO = open(nombre_archivo, "w")

    for linea in lineas:
        archivo.write(linea)
    archivo.close()