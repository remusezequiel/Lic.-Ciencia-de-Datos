module SolucionT1 where

-- Alumno: Ezequiel Remus

{- Ejercicio 1 (2 puntos)

problema maxMovilN (lista: seq⟨Z⟩, n: Z) : Z {
  requiere: {|lista| > 0}
  requiere: {n > 0 y n es menor a la longitud de la lista}
  asegura: {res es el máximo de los últimos n elementos de lista.}
}
-}

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

tomoHastaN :: [t] -> Integer -> [t]
tomoHastaN [] n = []
tomoHastaN (x:xs) 0 = [] 
tomoHastaN (x:xs) n = x:(tomoHastaN xs (n-1))

maximo :: Integer -> Integer -> Integer
maximo x y 
    | x>=y = x
    | otherwise = y

maximoDeLaLista :: [Integer] -> Integer
maximoDeLaLista [x] = x
maximoDeLaLista (x:y:xs) = maximoDeLaLista((maximo x y) : xs)


-- Si le pasamos el n=longitud(x:xs) nos devolvera 0, pues n tiene que ser menor extrito a dicho valor
maxMovilN :: [Integer] -> Integer -> Integer
maxMovilN (x:xs) n 
    | n>0 && n<longitud(x:xs) = maximoDeLaLista (listaFiltrada)
    | otherwise = 0
    where listaFiltrada = tomoHastaN (reverso (x:xs)) n


--------------------------------------------------------------------
{-  Ejercicio 2 (2 puntos)

    problema promedioPrimo (n: Z) : Float {
        requiere: {n > 1}
        asegura: {
            res es el promedio de todos los 
            factores primos de n (distintos o no).
        }
    }
-}

cantidadDivisores :: Integer -> Integer -> Integer
cantidadDivisores 1 m = 1
cantidadDivisores n 0 = 0
cantidadDivisores n m
    | mod n (m) == 0 = 1 + (cantidadDivisores n (m-1))
    | otherwise = cantidadDivisores n (m-1)

esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n 
    | (cantidadDivisores n n) > 2 = False
    | otherwise = True

-- Me da la lista de Primos, pero dada vuelta
listaPrimosEnN :: Integer -> [Integer]
listaPrimosEnN 1 = []
listaPrimosEnN n 
    | esPrimo n == True = n:(listaPrimosEnN (n-1))
    | otherwise = listaPrimosEnN (n-1)

listaPrimosOrdenada :: Integer -> [Integer]
listaPrimosOrdenada 1 = []
listaPrimosOrdenada n = reverso (listaPrimosEnN n)

tomoPrimerElemento :: [t] -> t
tomoPrimerElemento [t] = t
tomoPrimerElemento (x:xs) = x


factoresPrimosAux :: Integer -> [Integer] -> [Integer]
factoresPrimosAux 1 (x:xs) = []
factoresPrimosAux n (x:xs)
    | mod n x == 0 = x:(factoresPrimosAux (n`div`x) (x:xs)) 
    | otherwise = factoresPrimosAux (n) (xs)

factoresPrimos :: Integer -> [Integer]
factoresPrimos 1 = []
factoresPrimos n = factoresPrimosAux n (listaPrimosOrdenada n)

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

promedioPrimo :: Integer -> Float
promedioPrimo 1 = 0
promedioPrimo n = suma/cantFactores 
    where 
        factores = factoresPrimos n
        suma = fromInteger(sumatoria (factores))
        cantFactores = fromInteger (longitud (factores))


--------------------------------------------------------------------
{-  Ejercicio 3 (2 puntos)

    problema letrasIguales (palabra: seq⟨Char⟩) : Z {
        requiere: {True}
        asegura: {
            res es la cantidad de caracteres no blancos repetidos en palabra.
        }
    }
-}

vecesRepetida :: [Char] -> Char -> Integer
vecesRepetida [] c = 0
vecesRepetida [x] c 
    | x == c && x/=' ' = 1
    | otherwise = 0 
vecesRepetida (x:xs) c
    | x/=' ' && x==c = 1 + vecesRepetida xs c
    | otherwise = vecesRepetida xs c

sacarLetra :: [Char] -> Char -> [Char]
sacarLetra [] _ = []
sacarLetra (x:xs) elem 
    | x == elem = sacarLetra xs x
    | otherwise = x:(sacarLetra xs x)

letrasIguales :: [Char] -> Integer
letrasIguales [] = 0
letrasIguales [x] = 0
letrasIguales (x:xs) 
    | (vecesRepetida (x:xs) x) > 1 = 1 + letrasIguales (sacarLetra xs x)
    | otherwise = letrasIguales (xs)


--------------------------------------------------------------------
{-  Ejercicio 4 (3 puntos)

    problema cuantosIguales (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Z⟩{
        requiere: {True}
        asegura: {
            res es igual a la cantidad de caracteres no blancos 
            y distintos que palabra1 y palabra2 tienen en común.}
    }
-}


caracteresEnComun :: [Char] -> [Char] -> [Char]
caracteresEnComun [] [] = []
caracteresEnComun (x:xs) [] = []
caracteresEnComun [] (y:ys) = []
caracteresEnComun [x] [y] 
    | x == y = [x]
    | otherwise = []
caracteresEnComun (x:xs) (y:ys)
    | (vecesRepetida (x:xs) y) > 0 = y:(caracteresEnComun (x:xs) (ys))
    | otherwise = caracteresEnComun (x:xs) (ys)

cuantosIguales :: [Char] -> [Char] -> Integer
cuantosIguales [] [] = 0
cuantosIguales (x:xs) [] = 0
cuantosIguales [] (y:ys) = 0
cuantosIguales (x:xs) (y:ys) = longitud (caracteresEnComun (x:xs) (y:ys))
