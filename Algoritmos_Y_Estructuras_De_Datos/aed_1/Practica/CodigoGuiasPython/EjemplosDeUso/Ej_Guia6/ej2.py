from menu import menu as menu
import math as mates

"""
    EJERCICIO 2
"""
############################## Ej2.1 ##############################
def imprimir_saludo(nombre:str)->str:
    print("Hola",nombre )
############################## Ej2.2 ##############################
"""Pensar como aplicar la aproximaciòn de Bakhshali"""
def raiz_cuadrada_de(n:int)->float:
    return mates.sqrt(n)
############################## Ej2.3 ##############################
def farenheit_a_celsius(temp_far:float)->float:
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
    res = 1
    p=1
    condicion = comensales*min_cant_porciones
    while condicion>8:
        if condicion >= 8:
            res=1+res
        condicion=condicion-8
    p=res    
    return res


###################
#   EJECUCIÓN
###################

if __name__ == "__main__":
    exercise_name = ["imprimir_saludo","raiz_cuadrada_de","farenheit_a_celsius",
                     "imprimir_dos_veces","es_multiplo_de","es_par", "cantidad_de_pizzas"]
    option=0
    
    while option<=len(exercise_name)+2:

        option = menu(6,exercise_name)
        if option==1:
            name:str = input("Introduci tu nombre: ")
            imprimir_saludo(name)
        elif option==2:
            num = float(input("Decime un número: "))
            print(raiz_cuadrada_de(num))
        elif option==3:
            temperatura = float(input("Decime una temperatura en Farenheit: "))
            t = farenheit_a_celsius(temperatura)
            print(f'La temperatura en celsius es: {t} °C')
        elif option==4:
            estribo:str = input("Decime un estribillo: ")
            print(imprimir_dos_veces(estribo))
        elif option==5:
            num_1 = int(input("Decime un numero: "))
            num_2 = int(input("Decime otro numero: "))
            if es_multiplo_de(num_1,num_2):
                print("Son multiplos.")
            else:
                print("No son multiplos.")
        elif option==6:
            num = int(input("Decime un numero: "))
            if es_par(num):
                print("El numero es par.")
            else:
                print("El numero no es par.")
        elif option==7:
            comensales:int = int(input("Decime un la cantidad de comensales: "))
            min_porciones:int = int(input("Decime el minimo de porciones que come cada uno: "))
            
            res:int = cantidad_de_pizzas(comensales,min_porciones)
            
            print(f'Tenes que comprar {res} pizzas.')
        else:
            option=len(exercise_name)+6









