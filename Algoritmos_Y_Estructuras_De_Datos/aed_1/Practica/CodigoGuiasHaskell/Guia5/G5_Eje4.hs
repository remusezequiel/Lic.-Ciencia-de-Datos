module G5_Eje4 where

-- Ejercicio 4. a) Definir las siguientes funciones 
--    sobre listas de caracteres, interpretando una 
--    palabra como una secuencia de caracteres sin blancos:

{- a) sacarBlancosRepetidos :: [Char] -> [Char], 
    que reemplaza cada subsecuencia de blancos contiguos 
    de la primera lista por un solo blanco en la lista 
    resultado.
-}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)


{- b) contarPalabras :: [Char] -> Integer, 
    que dada una lista de caracteres devuelve 
    la cantidad de palabras que tiene
-}
contarPalabras :: [Char] -> Integer
contarPalabras texto = contarPalabrasAux texto False 0
  where
    contarPalabrasAux [] _ count = count
    contarPalabrasAux (x:xs) enPalabra count
      | x == ' '  = contarPalabrasAux xs False count
      | enPalabra = contarPalabrasAux xs True count
      | otherwise = contarPalabrasAux xs True (count + 1)

{- c) palabras :: [Char] -> [[Char]], 
    que dada una lista arma una nueva lista con las 
    palabras de la lista original.
-}
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras xs = palabra : palabras resto
  where
    palabra = tomarPalabra xs
    resto = soltarEspacios (soltarPalabra xs) -- Esto basicamente nos da un string con todas las palabras separadas por espacios

-- Función auxiliar para tomar una palabra de la lista
tomarPalabra :: [Char] -> [Char]
tomarPalabra [] = []
tomarPalabra (x:xs)
  | x == ' '  = []
  | otherwise = x : tomarPalabra xs

-- Función auxiliar para soltar una palabra de la lista
soltarPalabra :: [Char] -> [Char]
soltarPalabra [] = []
soltarPalabra (x:xs)
  | x == ' '  = xs
  | otherwise = soltarPalabra xs

-- Función auxiliar para soltar los espacios en blanco al inicio de la lista
soltarEspacios :: [Char] -> [Char]
soltarEspacios [] = []
soltarEspacios (x:xs)
  | x == ' '  = soltarEspacios xs
  | otherwise = x:xs



{- d) palabraMasLarga :: [Char] -> [Char],
     que dada una lista de caracteres devuelve 
     su palabra más larga.
-}
contar :: [Char] -> Integer
contar [] = 0
contar (x:xs) = 1 + contar xs

tomarPalabraMasCuenta :: [Char] -> ([Char],Integer)
tomarPalabraMasCuenta [] = ([],contar [])
tomarPalabraMasCuenta (x:xs)
  | x == ' '  = ([],contar [])
  | otherwise = (tomarPalabra (x:xs), (contar (tomarPalabra (x:xs))))
           
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:xs) 
    | snd (primerPalabra) > snd(siguientePalabra) = fst primerPalabra
    | otherwise = palabraMasLarga (fst siguientePalabra) 
    where primerPalabra = tomarPalabraMasCuenta (x:xs)
          siguientePalabra = tomarPalabraMasCuenta (soltarEspacios (soltarPalabra xs))      

{- e) aplanar :: [[Char]] -> [Char], 
    que a partir de una lista de palabras arma 
    una lista de caracteres concatenándolas.
-}
empiezaConBlanco :: [Char] -> Bool
empiezaConBlanco (x:xs) | x == ' ' = True | otherwise = False

sacoBlanco :: [Char] -> [Char]
sacoBlanco [] = []
sacoBlanco (x:xs)
    | empiezaConBlanco (x:xs) == True = xs
    | otherwise = x:sacoBlanco xs

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) 
    | x /= [' '] = (sacoBlanco x) ++ (aplanar xs)
    | otherwise = aplanar xs

{- f) aplanarConBlancos :: [[Char]] -> [Char], 
    que a partir de una lista de palabras, arma una lista de caracteres
    concatenandolas e insertando un blanco entre cada palabra.
-}
-- Función auxiliar para concatenar dos listas de caracteres
concatenar :: [Char] -> [Char] -> [Char]
concatenar [] ys = ys
concatenar (x:xs) ys = x : concatenar xs ys

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = concatenar x (aplanar xs)

{- g) aplanarConNBlancos :: [[Char]] -> Integer -> [Char], 
    que a partir de una lista de palabras y un entero n,
    arma una lista de caracteres concatenándolas e insertando 
    n blancos entre cada palabra (n debe ser no negativo).
-}
crearNBlancos :: [Char] -> Integer -> [Char]
crearNBlancos [] n 
  | n == 0 = []
  | otherwise = [' '] ++ crearNBlancos [] (n-1) 
crearNBlancos (xs) 0 = (xs) 
crearNBlancos (x:xs) n 
    |x /=  ' '= x:(crearNBlancos xs (n-1))
    |otherwise = crearNBlancos xs n

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] 0 = [] 
aplanarConNBlancos [] n = []
aplanarConNBlancos (x:xs) n = (crearNBlancos (tomarPalabra x) n) ++ aplanarConNBlancos xs n
