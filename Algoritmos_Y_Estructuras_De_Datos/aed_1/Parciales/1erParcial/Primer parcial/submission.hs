module SolucionT1 where

{--
    Alumno: Ezequiel Remus
--}


-- Ejercicio 1
{--
problema maximoActual (lista: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {|lista| > 0}
  asegura: {|res|= |lista|}
  asegura: {Cada uno de los elementos de res se obtienen 
  como el maximo entre los elementos de lista para la misma posición y las anteriores.}
}

Ejemplo: dada la lista [1,3,2,5,1] debe devolver [1,3,3,5,5] 
--}

maximoActual:: [Integer] -> [Integer]
maximoActual [x] = [x]
maximoActual (x:y:xs) 
    | x>y = x:(maximoActual (x:xs))
    | otherwise = x:(maximoActual (y:xs))


-- Ejercicio 2
{--
2) Ejercicio 2 [2 puntos]

problema primosRepetidos (n: Z) : Z {
  requiere: {n > 0}
  asegura: {
    (res es la cantidad de factores primos 
     que se repiten en la factorización.}
}
Ejemplo: El número 36, cuya descomposición en primos es 2 x 2 x 3 x 3, 
tiene repetidos 2 y 3 entre su descomposición, luego la función debe devolver 2. 
--}
-- cantidadDivisores :: Integer -> Integer -> Integer




factorizar :: Integer -> Integer -> [Integer]
factorizar 1 _ = []
factorizar m d 
    | mod m d == 0 = d:(factorizar (div m d) d)
    | otherwise = factorizar m (d+1)

contarApariciones :: Integer -> [Integer] -> Integer
contarApariciones _ [] = 0
contarApariciones n (x:xs)
    | n==x = 1 + contarApariciones n xs
    | otherwise = contarApariciones n xs

sacar :: Integer -> [Integer] -> [Integer]
sacar _ [] = [] 
sacar n (x:xs)
    | contarApariciones n (x:xs) > 0 = sacar n xs
    | otherwise = x:sacar n xs

contarRepeticiones :: [Integer]  -> Integer
contarRepeticiones [] = 0
contarRepeticiones [x] = 0 
contarRepeticiones (x:xs) 
    | contarApariciones x (x:xs) >1 = 1 + contarRepeticiones (sacar x xs) 
    | otherwise = contarRepeticiones xs 

primosRepetidos :: Integer -> Integer
primosRepetidos n = contarRepeticiones (factorizar n 2) 
                


-- Ejercicio 3
{--
problema palabraCapicua (palabra: seq⟨Char⟩) : Bool {
  requiere: {palabra es una secuencia de caracteres sin blancos y no vacia}
  asegura: {
    (res = true <=> la palabra se puede leer de igual modo de adelante
     para atrás que de atrás para adelante.
  }
}

Por ejemplo: la palabra "anana". 
--}
reverso :: [Char] -> String
reverso [] = ""
reverso (x:xs) = (reverso xs) ++ [x]

palabraCapicua :: String -> Bool
palabraCapicua cadena = cadena == (reverso cadena)



-- Ejercicio 4
{--
problema cuantosDistintos (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Z⟩{
  requiere: {|palabra1| > 0 y |palabra2| > 0}
  asegura: {res es igual a la cantidad de caracteres en
   que palabra1 y palabra2 difieren sin contar repetidos.}
}

Ejemplo: las palabras "casa" y "materias" difieren en las letras c, m, t, e, r y i, la función debe devolver 6. 
--}
longitud :: (Eq t) => [t] ->  Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

sacarIguales :: (Eq t)=> t -> [t] ->  [t] 
sacarIguales t [] = []
sacarIguales t (x:xs) 
    | t == x = sacarIguales t xs
    | otherwise = x:(sacarIguales t xs)

sacarTodasLasIguales :: (Eq t)=> [t] -> [t] ->  [t] 
sacarTodasLasIguales [] []  = []
sacarTodasLasIguales (x:xs) []   = []
sacarTodasLasIguales [] (y:ys)  = []
sacarTodasLasIguales [x] (y:ys) = sacarIguales x (y:ys)  
sacarTodasLasIguales (x:xs) (y:ys) = sacarTodasLasIguales xs (sacarIguales x (y:ys))

cuantosDistintos :: String -> String -> Integer
cuantosDistintos p1 p2 = longitud (sacarTodasLasIguales p1 p2) + longitud (sacarTodasLasIguales p2 p1)  