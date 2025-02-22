"""
1)Caminen, chiques, caminen! [2 puntos]
Lita de Lazari fue una conocida ama de casa de ladécada de los 80's y 90's.
Fue, durante muchos años, la presidenta de la Liga deAmas de Casa.
Su fama se debía, principalmente, a que salía portelevisión dando consejos a las amas de casa.
Entre sus frases más famosas está la ya clásica"caminen chicas" (parafraseada y actualizada a lostiempos modernos en el título de este ejercicio).
Esta frase representaba la idea de que, dada la situacióneconómica del país en aquella época (no muy diferentea la actual) la mejor forma de ahorrar era recorrerdiferentes comercios en busca de los mejores precios.
Implementar la función mejores_precios() que dadasdos listas super1 y super2, de igual longitud, dondecada i-ésimo elemento de ambas listas representa elprecio de un mismo producto en dos supermercados,devuelva una lista de igual longitud con el menor preciode cada producto.

problema mejores_precios (in super1:seq⟨String x R⟩,in super2:seq⟨String x R⟩): seq⟨String x R ⟩ {
    requiere:{ |super1| = |super2| }
    requiere: {
        Todos los elementos en las segundas posiciones de las tuplas de super1
        y de super2 son positivos
    }
    requiere: {
        Todos los elementos en las primeras posiciones de las tuplas de
        super1 y de super2 son iguales
    }
    asegura: { |res|=|super1| }
    asegura: {
        Cada posición de |res| contiene una tupla con el nombre del producto 
        correspondiente al de esaposición en super1 y el mínimo valor entre los 
        elementos que se encuentran en esa posición en super1 y super2
    }
}

Por ejemplo, dado
super1
= [("leche", 151.0), ("yerba", 4719.5), ("jabón",269.2)]
super2
= [("leche", 261.2), ("yerba", 3939.1), ("jabón",319.2)]
se debería devolver
res
= [("leche", 151.0), ("yerba",3939.1), ("jabón", 269.2)]
"""

def comparar_tupla(t1:tuple[str,int],t2:tuple[str,int])->tuple[str,int]:
    if t1[1]<=t2[1]:
        return t1
    else:
        return t2
    

def mejores_precios(super1:list[tuple[str,int]], super2:list[tuple[str,int]])->list[tuple[str,int]]:
    res:list[tuple[str,int]]=list()
    
    for indice in range(len(super1)):
        res.append(comparar_tupla(super1[indice],super2[indice]))
    return res    

if __name__ == "__main__":
    super1 = [("leche", 151.0), ("yerba", 4719.5), ("jabón",269.2)]
    super2 = [("leche", 261.2), ("yerba", 3939.1), ("jabón",319.2)]
    
    print(mejores_precios(super1,super2))