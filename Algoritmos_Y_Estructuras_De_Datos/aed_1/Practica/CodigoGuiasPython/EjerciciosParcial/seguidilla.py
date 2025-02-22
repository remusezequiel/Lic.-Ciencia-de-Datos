"""2)Seguidilla [2 puntos]

Implementar la función seguidilla() que dada unasecuencia de enteros
calificaciones, y un entero nota_minima, devuelva la cantidad de 
elementos de lasubsecuencia más larga que cumplen que son mayoresoiguales a la nota_minima.
En caso de que esta seguidilla no exista, devolver 0.

    problema seguidilla (in calificaciones: seq⟨Z⟩, in nota_minima: Z): Z {
        requiere: {
            todos los elementos de calificaciones son mayores 
            o iguales a 0 y menores o iguales a 100
        }
        requiere: {
         nota_minima es mayor o igual a 0 y menoroigual a 100
        }
        asegura: {
            res = |subsec| si solo si existe unasubsecuencia de calificaciones
            ( subsec ), y todos los elementos de subsec son mayores o iguales a la
            nota_minima
        }
        asegura: {
            No existe otra subsecuencia decalifi caciones que tenga longitud mayor a res
        }
        asegura: {
            res = 0 si y solo si no hay ningún elemento de 
            calificaciones que sea mayor a nota_minima
        }
    }

    Ejemplo 1: dada los siguientes inputs:
    
    calificaciones = [10,55,60,87,54,98,87,65,55,45,57];
    nota_minima = 60
    se debería devolver
    res = 3,
    que es la longitud de lasubsecuencia [98,87,65]

    Ejemplo 2: dada los siguientes inputs:
    
    calificaciones = [10,55,60,65,54,64,65,55,45,57];
    nota_minima = 70
    
    se debería devolver
    res = 0, 
    ya que no hay ninguna subsecuencia de calificaciones con elementos mayores o iguales a nota_minima
"""
def mayor_a(num1:int,num2:int)->bool:
    if num1>=num2:
        return True
    return False

def maximo(num1:int,num2:int)->int:
    if num1>=num2:
        return num1
    return num2

def seguidilla(calificaciones:list[int], nota_minima:int)->int:
    contador1:int=0
    contador2:int=0
    
    for i in calificaciones:
        if mayor_a(i,nota_minima):
            contador1+=1
        elif not mayor_a(i,nota_minima) and contador1>contador2:
            contador2=contador1
            contador1=0

    return maximo(contador1,contador2)
    
if __name__ == "__main__":

    calificaciones_1 = [10,55,60,87,54,98,87,65,55,45,57]
    nota_minima_1 = 60
    calificaciones_2 = [10,55,60,65,54,64,65,55,45,57]
    nota_minima_2 = 70
    
    print("Ejemplo 1: ",seguidilla(calificaciones_1,nota_minima_1))
    print("Ejemplo 2: ",seguidilla(calificaciones_2,nota_minima_2))
