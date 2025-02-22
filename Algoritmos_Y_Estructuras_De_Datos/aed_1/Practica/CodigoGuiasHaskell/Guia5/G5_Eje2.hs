module G5_Eje2 where

--Ejercicio 2. Definir las siguientes funciones sobre listas:

{- 1. pertenece :: (Eq t) => t -> [t] -> Bool 
    según la siguiente especificación:
        problema pertenece (e: T, s: seq⟨T⟩) : B {
            requiere: { True }
            asegura: { resultado = true ↔ e ∈ s }
    }
-}
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e xs


{-    
    2. todosIguales :: (Eq t) => [t] -> Bool, 
    que dada una lista devuelve verdadero sii todos sus elementos son iguales.
-}
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = True 
    | otherwise = todosIguales (y:xs)

{- 3. todosDistintos :: (Eq t) => [t] -> Bool 
        según la siguiente especificación:
    
    problema todosDistintos (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
    }
-}
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:y:xs) | x == y = False 
    | otherwise = todosDistintos (y:xs)


{- 4. hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
        problema hayRepetidos (s: seq⟨T⟩) : B {
            requiere: { True }
            asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
        }
-}
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs == True = True
    |otherwise = hayRepetidos xs

{-5. quitar :: (Eq t) => t -> [t] -> [t], 
    que dados un entero x y una lista xs, 
    elimina la primera aparición de x en
    la lista xs (de haberla).-}
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x [y] | x==y = [] | otherwise = [y]
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e (xs)
{- 6.   quitarTodos :: (Eq t ) => t -> [t] -> [t], 
        que dados un entero x y una lista xs, 
        elimina todas las apariciones de x en la    
        lista xs (de haberlas). Es decir:
        
        problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
            requiere: { True }
            asegura: { 
                resultado es igual a s 
                pero sin el elemento e. }
        }
-}
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) 
    | e == x = quitarTodos e xs
    | otherwise = x : quitarTodos e xs

{- 7. eliminarRepetidos :: (Eq t) => [t] -> [t] 
      que deja en la lista una ´unica aparición 
      de cada elemento, eliminando las 
      repeticiones adicionales.
-}
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitarTodos x xs)

{- 8. mismosElementos :: (Eq t) => [t] -> [t] -> Bool, 
    que dadas dos listas devuelve verdadero síi
    ambas listas contienen los mismos elementos, 
    sin tener en cuenta repeticiones, es decir:
    
    problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { 
            resultado = true ↔ todo elemento de s 
                        pertenece r y viceversa}
    }
-}
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos [x] [y] | x==y = True | otherwise = False
mismosElementos (x:xs) (y:ys) 
    | pertenece x (y:ys) = mismosElementos xs (quitar x (y:ys))
    | otherwise = False

{-9. capicua :: (Eq t) => [t] -> Bool 
    según la siguiente especificación:
    
    problema capicua (s: seq⟨T⟩) : B {
        requiere: { True }
        asegura: { (resultado = true) ↔ (s = reverso(s)) }
    }
    
    Por ejemplo: 
    capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true, 
    capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false.
-}    

reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = (reverso (xs) ++ [x])

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs) = (x:xs) == reverso (x:xs)
