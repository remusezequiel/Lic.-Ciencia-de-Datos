import math
from menu import menu as menu
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
def perimetro()->float: # Mejor esta versión en un trabajo real
    return 2 * math.pi



###################
#   EJECUCIÓN
###################

if __name__== "__main__":    
    exercise_name = ["imprimir_hola_mundo","imprimir_un_verso","raizDe2","factorial_2","perimetro"]
    option=0
    
    while option<=len(exercise_name)+2:

        option = menu(6,exercise_name)
        if option==1:
            imprimir_hola_mundo()
        elif option==2:
            imprimir_un_verso()
        elif option==3:
            raizDe2()
        elif option==4:
            factorial_2()
        elif option==5:
            perimetro()
        else:
            option=len(exercise_name)+6
    
    