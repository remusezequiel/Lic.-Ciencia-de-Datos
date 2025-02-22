"""
    EJERCICIO 1
"""
############################## Ej1.1 ##############################

def imprimir_hola_mundo():
    print("Hola mundo")
    
def imprimir_hola_mundo_alternativo(): # Cumple la especificación? Sí :)
    print("Hola mundo")
    while True:
        pass

############################## Ej1.2 ##############################
def imprimir_un_verso():
    print("What else should I be?\nAll Apologies")    

############################## Ej1.3 ##############################
def raizDe2(): 
    return round(math.sqrt(2),4) 

############################## Ej1.4 ##############################
def factorial_2():
    return math.factorial(2)

def factorial (n:int)->int:
    if n==0 or n==1:
        return 1
    else: 
        return n * factorial(n-1)

def factorial_2_mia()->int:
    return factorial(2)
############################## Ej1.5 ##############################

def perimetro()->float:
    return 2 * 3.14159265358979323846

import math
def perimetro_alternativo()->float: # Mejor esta versión en un trabajo real
    return 2 * math.pi

"""
    EJERCICIO 2
"""
############################## Ej2.1 ##############################
def imprimir_saludo(nombre:str)->str:
    print("Hola",nombre )
############################## Ej2.2 ##############################
"""Pensar como aplicar la aproximaciòn de Bakhshali"""
def raiz_cuadrada_de(n:int)->float:
    pass

############################## Ej2.3 ##############################
def fahenheit_a_celsius(temp_far:float)->float:
    return ((temp_far-32)*5)/9
############################## Ej2.4 ##############################
def imprimir_dos_veces(estribillo:str)->str:
    return 2*estribillo
############################## Ej2.5 ##############################
""" Nos va a devolver True si son multiplos. 
para eso se fija si el resto de dividir n en m
es nulo"""
def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0


############################## Ej2.6 ##############################
def es_par(n:int)->bool:
    return n%2==0
############################## Ej2.7 ##############################
def cantidad_de_pizzas(comensales:int,min_cant_porciones:int)->int:
    res = 0
    p=1
    condicion = comensales*min_cant_porciones
    while condicion>8:
        if condicion >= 8:
            res=1+res
        condicion=condicion-8
    p=res    
    return res


"""
    EJERCICIO 3
"""
############################## Ej 3.1 ##############################
def alguno_es_0(num1:float, num2:float)->bool:
    return num1==0 or num2==0

############################## Ej 3.2 ##############################
def ambos_son_0(num1:float, num2:float)->bool:
    return num1==0 and num2==0

############################## Ej 3.3 ##############################
def longitud(cadena:str)->int:
    contador=0
    for i in cadena:
        contador+=1
    return contador
def es_nombre_largo(nombre: str) -> bool:
    # return 3 <= len(nombre) and len(nombre) <= 8
    return 3<=longitud(nombre)<=8 

############################## Ej 3.4 ##############################
def es_bisiesto(anio:int)->bool:
    return (es_multiplo_de(anio,4) and not(es_multiplo_de(anio,100))) or es_multiplo_de(anio,400)

"""
    EJERCICIO 4
"""
def peso_pino(altura:float)->float:
    """
    param: altura en metros
    asegura: 3kg x centimetro hasta arboles de 3 metros.
    asegura: 2 kg por cada centimetro para arboles de mas de 3 metros. 
    """
    if altura<=3:
        return altura*100*3
    else:
        return altura*100*2

def es_peso_util(peso:float)->bool:
    return 400<=peso<=1000

def sirve_pino(altura:float)->bool:
    return 400<=peso_pino(altura)<=1000


"""
    EJERCICIO 5
"""
############################## Ej5.1 ##############################
def devolver_el_doble_si_es_par(un_numero: int) -> int: 
    if un_numero % 2 == 0:
        return un_numero * 2
    return un_numero

def devolver_el_doble_si_es_par_alternativo(un_numero: int) -> int:
    if un_numero % 2 == 0:
        un_numero = un_numero * 2
    return un_numero 

# Ambas alternativas son válidas. Es muy 'de juguete' el ejemplo preferir una. 
# No tiene nada de malo a priori usar más de un return, hay casos donde es más claro y casos que no.
############################## Ej5.2 ##############################
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) ->int:
    if es_par(numero):
        return numero
    else:
        return numero+1
############################## Ej5.3 ##############################
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
    if es_multiplo_de(numero,3):
        return 2*numero
    elif es_multiplo_de(numero,9):
        return 3*numero
    else:
        return numero
############################## Ej5.4 ##############################
def lindo_nombre(nombre:str)->str:
    if len(nombre)>=5:
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
############################## Ej5.5 ##############################
def elRango(numero:int)->str:
    n = abs(numero)
    if n<5:
        return "Menor a 5"
    elif 10<=n<=20:
        return "El numero esta entre 10 y 20"
    else:
        return "Mayor a 20"

        
        
############################## Ej5.6 ##############################
def accion_segun_sexo_y_edad(sexo:str,edad:int)->str:
    if sexo.lower()=="m" and 18<edad<65:
        return "Anda a laburar"
    elif sexo.lower()=="f" and edad>=60:
        return "Andá de vacaciones"
    else:
        return "Andá de vacaciones"

"""
    EJERCICIO 6
"""
############################## Ej6.1 ##############################
def del_1_al_10():
    cont=0
    while cont<=10:
        cont+=1
        print(cont)

############################## Ej6.2 ##############################

def ej_6_2():
    actual: int = 10
    while actual <= 40:
        print(actual)
        actual += 2 # también se puede ir sumando 1 y preguntando con un if si imprimir o no, está es más corta
        
def ej_6_2_alternativa_con_for():
    for i in range(10, 40+1, 2): # notar que el 'hasta' es no inclusivo!
        print(i)
        
############################## Ej6.3 ##############################
def escribe_eco_10_veces():
    cont=0
    while cont<=10:
        cont+=1
        print("eco")

############################## Ej6.4 ##############################
def ej_6_4(numero: int):
    while numero >= 1:
        print(numero)
        numero -= 1
    print('Despegue')
    
def ej_6_4_alternativa_con_for(numero: int):
    for i in range(numero, 0, -1): # Vamos 'incrementando -1' hasta llegar al 0
        print(i)
    print('Despegue')

############################## Ej6.5 ##############################
def viaje_en_el_tiempo_1(partida:int, llegada:int):
    contador = partida
    while contador>llegada:
        contador-=1
        print("Viajó un año al pasado, estamos en el año: ", contador)
    

############################## Ej6.6 ##############################
def viaje_en_el_tiempo_2(partida:int):
    contador = partida
    while contador>-384:
        contador-=20
        if contador>=0:
            print("Viajó un año al pasado, estamos en el año: ", contador)
        else :
            print("Viajó un año al pasado, estamos en el año: ", abs(contador), " a.C.")

"""
    EJERCICIO 7
"""
############################## Ej7 ##############################

# Ya lo metimos en el anterior

############################## Ej8 ##############################

def ejemploReturn(xArgumento: int) -> int:
    print("En ejemploReturn: ", xArgumento)
    xArgumento = xArgumento + 40
    return xArgumento

def ejemploVarGlobal():
    global xGlobal
    print("En ejemploVarGlobal: ", xGlobal)
    xGlobal = xGlobal + 30
    
"""
xGlobal: int = 1
xGlobal = ejemploReturn(xGlobal)
print("En codigo libre: ", xGlobal)
ejemploVarGlobal()
print("En codigo libre: ", xGlobal)
xGlobal = ejemploReturn(xGlobal)
print("En codigo libre: ", xGlobal)
ejemploVarGlobal()
print("En codigo libre: ", xGlobal)
"""
