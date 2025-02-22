module G5_Eje5 where

-- Ejercicio 5 Definir las siguientes funciones sobre listas:

{- 1) sumaAcumulada :: (Num t) => [t] -> [t] 
    según la siguiente especificación:
    
    problema sumaAcumulada (s: seq⟨T⟩) : seq⟨T⟩ {
        requiere: {T es un tipo num´erico}
        requiere: {cada elemento de s es mayor estricto que cero}
        asegura: {
            |s| = |resultado| ∧ el valor en la 
            posición i de resultado es sum_{k=0}^{i} s[k]
        }
Por ejemplo sumaAcumulada [1, 2, 3, 4, 5] es [1, 3, 6, 10, 15].

-}
-- Definición de la función sumaAcumulada
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = sumaAcumuladaAux x xs

-- Función auxiliar para llevar la suma acumulada
sumaAcumuladaAux :: (Num t) => t -> [t] -> [t]
sumaAcumuladaAux acc [] = [acc]
sumaAcumuladaAux acc (x:xs) = acc : sumaAcumuladaAux (acc + x) xs

{-  2) 2. descomponerEnPrimos :: [Integer] -> [[Integer]] 
    seg´un la siguiente especificaci´on:
    
    problema descomponerEnPrimos (s: seq⟨Z⟩) : seq⟨seq⟨Z⟩⟩ {
        requiere: { Todos los elementos de s son mayores a 2 }
        asegura: { |resultado| = |s| }
        asegura: {
            todos los valores en las listas de resultado 
            son números primos}
        asegura: {
            multiplicar todos los elementos en la lista 
            en la posición i de resultado es igual al 
            valor en la posición i de s
        }
}
Por ejemplo descomponerEnPrimos [2, 10, 6] es [[2], [2, 5], [2, 3]].

-}
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

cantidadDeDivisores :: Integer -> Integer
cantidadDeDivisores n = contarDivisores n n

contarDivisores :: Integer -> Integer -> Integer
contarDivisores n 1 = 1
contarDivisores n k
    | n `mod` k == 0 = 1 + contarDivisores n (k - 1)
    | otherwise      = contarDivisores n (k - 1)

esPrimo :: Integer -> Bool
esPrimo 1 = True
esPrimo x 
    | cantidadDeDivisores x > 2 = False   
    | otherwise = True
     
primosDeUnNumero :: Integer -> [Integer]
primosDeUnNumero 1 = []
primosDeUnNumero n 
    | esPrimo n==True = n:primosDeUnNumero (n-1)
    | otherwise = primosDeUnNumero (n-1)

primosDentroDeN :: Integer -> [Integer]
primosDentroDeN n = reverso (primosDeUnNumero n)

--descomponerEnPrimos :: [Integer] -> [[Integer]] 
--descomponerEnPrimos [] = []
--descomponerEnPrimos (x:xs) 
 --   | 