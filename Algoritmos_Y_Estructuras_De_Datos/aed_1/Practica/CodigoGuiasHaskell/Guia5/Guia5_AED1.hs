-------------------------
-- GUIA 5 COMPLETA
-------------------------
-- Ejercicio 1
-- a)
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- b)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs  

-- c)
principio :: [t] -> t 
principio (x:xs) = x

-- d)
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]

-- Ejercicio 2

-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e xs

-- 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y) | x \= y = False 
    | otherwise = todosIguales (y:xs)

-- 3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:y:xs) | x == y = False 
    | otherwise = todosDistintos (y:xs)

-- 4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs == True = True
    |otherwise = hayRepetidos xs

-- 5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e (xs)

-- 6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitar e xs
                | otherwise = x : quitar e (xs)

-- 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitarTodos x xs)

-- 8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos [x] [y] | x==y = True | otherwise = False
mismosElementos (x:xs) (y:ys) 
    | pertenece x (y:ys) = mismosElementos xs (quitar x (y:ys))
    | otherwise = False

-- 9)
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = (reverso (xs) ++ [x])

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs) = (x:xs) == reverso (x:xs)

-- Ejercicio 3
-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria (xs)

-- 2)
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:xs) = x * productoria (xs)

-- 3)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) 
    | x>=y = maximo (x:xs)
    | otherwise = maximo (y:xs)

-- 4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [n+x]
sumarN n (x:xs) = ((n+x):sumarN n xs)
-- 5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x+x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (head (reverso (x:xs))) (x:xs) 
-- 7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | esPar x == True = x : pares (xs)
    | otherwise = pares (xs)
    where 
        esPar n | mod n 2 == 0 = True 
                | otherwise = False

-- 8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) 
    | mod x n == 0 = x : multiplosDeN n (xs)
    | otherwise = multiplosDeN n (xs)
-- 9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = ordenar (sacoMaximo) ++ [maximo (x:xs)]
    where sacoMaximo = quitar (maximo (x:xs)) (x:xs)

-- Ejercicio 4
-- 1)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

-- 2)
contarPalabras :: [Char] -> Integer
contarPalabras texto = contarPalabrasAux texto False 0
  where
    contarPalabrasAux [] _ count = count
    contarPalabrasAux (x:xs) enPalabra count
      | x == ' '  = contarPalabrasAux xs False count
      | enPalabra = contarPalabrasAux xs True count
      | otherwise = contarPalabrasAux xs True (count + 1)

-- 3)
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

-- 4)
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
-- 5)
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

-- 6)
-- Función auxiliar para concatenar dos listas de caracteres
concatenar :: [Char] -> [Char] -> [Char]
concatenar [] ys = ys
concatenar (x:xs) ys = x : concatenar xs ys

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = concatenar x (aplanar xs)

-- 7)
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
------------------- enLosContactos -------------------

type Texto = [Char]
type Nombre = Texto
type Telefono =Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((nombreContacto, _):contactos) | nombre == nombreContacto = True
                                                      | otherwise = enLosContactos nombre contactos
-- Código alternativo: '= nombre == nombreContacto || enLosContactos nombre contactos'

{- Ejemplo de ejecución:
enLosContactos "Pepe" [("Ana", "1243"), ("Beto", "5678")]
--> enLosContactos "Pepe" [("Beto", "5678")]
--> enLosContactos "Pepe" []
--> False
-}

------------------- agregarContacto -------------------

agregarContacto :: Contacto -> ContactosTel -> ContactosTel -- asumamos que no hay dos contactos con el mismo nombre
agregarContacto contacto [] = [contacto]
agregarContacto (nombre,telefono) ((cNombre,cTelefono):contactos) | nombre == cNombre = (nombre,telefono) : contactos
                                                                  | otherwise = (cNombre,cTelefono) : agregarContacto (nombre,telefono) contactos












