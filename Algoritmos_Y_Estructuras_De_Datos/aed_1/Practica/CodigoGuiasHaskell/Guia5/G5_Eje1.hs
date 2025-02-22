module G5_Eje1 where

--  Ejercicio 1. Definir las siguientes funciones sobre listas:

-- 1) longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos.
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

{- 2. ultimo :: [t] -> t según la siguiente especificación:
        problema ultimo (s: seq⟨T⟩) : T {
            requiere: { |s| > 0 }
            asegura: { resultado = s[|s| − 1] }
        }
-}
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs  

{- 3. principio :: [t] -> [t] según la siguiente especificación:
    
    problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { |s| > 0 }
        asegura: { resultado = subseq(s, 0, |s| − 1) }
    }
-}
principio :: [t] -> t 
principio (x:xs) = x

{- 4. reverso :: [t] -> [t] según la siguiente especificación:
        
    problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: { True }
        asegura: { resultado tiene los mismos elementos que s 
                    pero en orden inverso.}
    }
-}
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]
