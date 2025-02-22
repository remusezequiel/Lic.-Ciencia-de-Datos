"""
2) Cambios de stock de stock_productos [2 puntos]

En la veterinaria "Exacta's pets", al finalizar cada día, el personal registra en papeles los nombres y
la cantidad actual de los productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección
de la veterinaria han pedido desarrollar una solución en Python que les permita analizar las
fluctuaciones del stock.

Se pide implementar una función que reciba una lista de tuplas, donde cada tupla contiene el nombre de 
un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario 
que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico
registrado.

problema stock_productos(in stock_cambios: seq<<String X Z>>): dict<String, <Z X Z>>{
    requiere: {Todos los elementos de stock_cambios están formados por un string no vacío y un entero >= 0}
    asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un
    producto)}
    asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios}
    asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor 
    cantidad de ese producto en stock_cambios y como segundo valor el mayor}
}
"""
def pertenece(diccionario: dict[str, tuple[int,int]],producto:str)->bool:
    for nombre, t in diccionario.items():
        if producto==nombre:
            return True
    return False

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    resultado = {}

    for nombre, cantidad in stock_cambios:
        if pertenece(resultado,nombre):
            min_cantidad, max_cantidad = resultado[nombre] # hago que el primer elem de la tupla que es valor sea min_c y el segundo max_c y que ambos tengan el valor de la cantidad ya cargada
            if cantidad < min_cantidad: # comparo las cantidades de acuerdo a lo que va ingresando
                min_cantidad = cantidad
            if cantidad > max_cantidad:
                max_cantidad = cantidad
            resultado[nombre] = (min_cantidad, max_cantidad)

        else:
            resultado[nombre] = (cantidad, cantidad)
    return resultado

if __name__=="__main__":
    stock_cambios = [("producto1", 5), ("producto2", 3), ("producto1", 2), ("producto2", 8)]
    print(stock_productos(stock_cambios)) # -> {'producto1': (2, 5), 'producto2': (3, 8)})