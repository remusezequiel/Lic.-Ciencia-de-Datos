module G5_Eje3 where

-- Ejercicio 3. Definir las siguientes funciones sobre listas de enteros:

{-  1) 
    problema sumatoria (s: seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { 
            resultado = sum_{i=0}^{|s|-1} s[i]
        }        
-}
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria (xs)

{- 2. productoria :: [Integer] -> Integer seg´un la siguiente especificaci´on:
    
    problema productoria (s: seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { 
            resultado = prod_{i=0}^{|s|-1} s_i
        }
-}
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:xs) = x * productoria (xs)

{- 3. maximo :: [Integer] -> Integer 
    según la siguiente especificación:

    problema maximo (s: seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { 
            resultado ∈ s ∧ todo elemento de s 
            es menor o igual a resultado }
    }
-}
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) 
    | x>=y = maximo (x:xs)
    | otherwise = maximo (y:xs)

{-4. sumarN :: Integer -> [Integer] -> [Integer] 

    según la siguiente especificación:
    problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { True }
        asegura: {
            |resultado| = |s| ∧ cada posición de 
            resultado contiene el valor que hay en 
            esa posición en s sumado n 
        }
    }
-}
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [n+x]
sumarN n (x:xs) = ((n+x):sumarN n xs)

{-5. sumarElPrimero :: [Integer] -> [Integer] 
        según la siguiente especificación:
    
    problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN(s[0], s) }
    }

Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
-}

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x+x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

{-  6. sumarElUltimo :: [Integer] -> [Integer] 
        según la siguiente especificación:

    problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN(s[|s| − 1], s) }
    }
    Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]

-}
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (head (reverso (x:xs))) (x:xs) 

{-  7. pares :: [Integer] -> [Integer] 
        según la siguiente especificación:

        problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
            requiere: { True }
            asegura: {
                resultado sólo tiene los elementos 
                pares de s en el orden dado, respetando 
                las repeticiones
            }
        }
    Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
-}

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | esPar x == True = x : pares (xs)
    | otherwise = pares (xs)
    where 
        esPar n | mod n 2 == 0 = True 
                | otherwise = False

{-  8. multiplosDeN :: Integer -> [Integer] -> [Integer] 
    que dado un número n y una lista xs, devuelve una lista
    con los elementos de xs múltiplos de n.
-}

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) 
    | mod x n == 0 = x : multiplosDeN n (xs)
    | otherwise = multiplosDeN n (xs)

{- 9. ordenar :: [Integer] -> [Integer] 
    que ordena los elementos de la lista en forma creciente. 
    Sugerencia: Pensar como pueden usar la función máximo 
    para que ayude a generar la lista ordenada necesaria.
-}  
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e (xs)


    ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = ordenar (sacoMaximo) ++ [maximo (x:xs)]
    where sacoMaximo = quitar (maximo (x:xs)) (x:xs)