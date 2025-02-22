def bienvenido(num:int):
    linea:str = '--------------------------'
    print(f'{linea} \n Bienvenido a la Guia {num}! \n{linea}')

def menu(guia:int, name_op:list[str])->int:
    bienvenido(guia)
    
    linea:str = '--------------------------'

    print(f'{linea}\n Lista de Ejercicios \n{linea}')
    for i in range(0,len(name_op)):
        print(f'{i+1}) {name_op[i]}')
    print(f'{len(name_op)+2}) Para salir')    
    option = int(input("Ingrese la opción: "))
    return option