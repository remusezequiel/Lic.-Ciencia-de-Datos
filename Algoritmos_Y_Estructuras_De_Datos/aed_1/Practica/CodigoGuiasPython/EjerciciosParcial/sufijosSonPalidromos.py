"""
3) Sufijos que son palíndromos (2 puntos)

Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.
Se nos pide programar en python la siguiente función:

problema cuantos_sufijos_son_palindromos(in texto:String) : Z {
  requiere: -
  asegura: {
    res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto
  }
}

Nota: un sufijo es una subsecuencia de textoi que va desde una posición cualquiera hasta el al final de la palabra. 
Ej: "Diego", el conjunto de sufijos es: "Diego", "iego","ego","go", "o".
Para este ejercicio no consideraremos a "" como sufijo de ningun texto.
"""

def sufijos_de(texto:str)->list[str]:
    sufijos:list[str] = []
    cadenaAux:str = ""

    for i in range(len(texto)-1,-1,-1):
        cadenaAux = cadenaAux+texto[i]
        sufijos.append(cadenaAux)
    return sufijos

def es_palidromo(texto:str)->bool:
    for indice in range(len(texto)//2):
        if texto[indice]!=texto[len(texto)-indice-1]:
            return False
    return True

def cuantos_sufijos_son_palidromo(texto:str)->int:
    res:int=0
    candidato:str = ""
    for t in range(len(texto)-1,-1,-1):
        candidato = candidato+texto[t]
        if es_palidromo(candidato):
            res+=1
    return res

if __name__ == "__main__":
    palabra_1 = "diego"
    print("Los subfijos de ", palabra_1, "son: ", sufijos_de(palabra_1) )
    print("Cantidad de subfijos palidromos en ", palabra_1, " : ", cuantos_sufijos_son_palidromo(palabra_1))
