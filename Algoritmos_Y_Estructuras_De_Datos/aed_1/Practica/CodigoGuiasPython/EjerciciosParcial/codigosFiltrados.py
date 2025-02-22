"""
1) Códigos filtrados [2 puntos]

El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos 
cuyos código de barras terminan en números primos son especialmente auspiciosos y deben ser destacados
en la tienda. Luego de convencer a su padre de esta idea, solicita una función en python que facilite
esta gestión.

Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código 
de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de 
la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

Nota: un número primo es aquel que solo es divisible por si mismo y por 1. Algunos ejemplos de hasta 
tres dígitos son 2, 3, 4, 101, 103, 107, etc.

problema filtrar_codigos_primos(in codigos_barra: seq<Z>) : seq<Z> {
    requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
    requiere: {No hay elementos repetidos en codigos_barra}
    asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
    asegura: {
        Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo 
        están en res
    }
    asegura: {Todos los elementos de res están en codigos_barra}
}
"""
def tomar_los_ultimos_3_digitos(numero:int)->int:
    return numero-((numero//1000)*1000)

def cantidad_divisores(numero:int)->list[int]:
    divisores:list[int] = list()
    for n in range(1, numero):
        if numero % n == 0:
            divisores.append(n)
    return divisores

def es_primo(numero:int)->bool:
    if len(cantidad_divisores(numero))>2:
        return False
    return True

def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    res:list[int]=list()

    for codigo in codigos_barra:
        if es_primo(tomar_los_ultimos_3_digitos(codigo)):
            res.append(codigo)
    return res



if __name__ == "__main__":
    codigos_barra = [10097,10010,25101,40002107]
    print(filtrar_codigos_primos(codigos_barra))