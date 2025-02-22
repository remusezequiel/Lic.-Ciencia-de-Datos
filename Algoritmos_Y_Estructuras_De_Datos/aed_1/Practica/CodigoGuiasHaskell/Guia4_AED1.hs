-- git config --global --unset user.name
-- git config --global --unset user.email



{-------ejercicios de clase--------}
-- Podemos definir la función dactorial con el siguiente algoritmo recursivo.
-- Tambien estamos utilizando pattern maching
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

-- OtraForma de definirla seria:
fact :: Integer -> Integer
fact n 
    | n == 0 = 1
    | n > 0 = n * fact (n-1)
    



{-  GUIA 4 : RECURSIÓN-}

------------------------------------------------------------
{-
    Ejercicio 1. Implementar la función 
    fibonacci:: Integer ->Integer que devuelve el i-ésimo número de Fibonacci.
    Recordar que la secuencia de Fibonacci se define como:

    problema fibonacci (n: Z) : Z {
        requiere: { n ≥ 0 }
        asegura: { resultado = f ib(n) }
    }

               | 0 si n = 0     
    fib(n) =   | 1 si n = 1
               | fib(n-1) + fib(n-2) en otro caso
-}

-- Vamos a utilizar la función absoluto que hicimos en la Guia 3
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)


------------------------------------------------------------
{- Ejercicio 2. Implementar una función 
    parteEntera :: Float ->Integer 
    
    según la siguiente especificación:

    problema parteEntera (x: R) : Z {
        requiere: { x ≥ 0 }
        asegura: { resultado ≤ x < resultado + 1 }
    }
-}
parteEntera :: Float -> Integer
parteEntera x 
    | x < 1 = 0
    | otherwise = 1 + parteEntera (x-1)

------------------------------------------------------------
{-Ejercicio 3. Especificar e implementar la función 
    esDivisible :: Integer -> Integer -> Bool que dados dos números
    naturales determinar si el primero es divisible por el segundo. 
    No está permitido utilizar las funciones mod ni div.
-}
-- a = k * d

esDivisible :: Integer -> Integer -> Bool
esDivisible a d
    | a < d     = False
    | a == d    = True
    | otherwise = esDivisible (a - d) d

------------------------------------------------------------
{- Ejercicio 4. Especificar e implementar la función 
    sumaImpares :: Integer ->Integer 
    que dado n ∈ N sume los primeros n números impares. 
    
    Por ejemplo: sumaImpares 3 ; 1+3+5 ⇝ 9.
-}
{-
sumaImpares :: Integer ->Integer 
sumaImpares 1 = 1
sumaImpares n
    | n < 0 = 0
    | mod n 2 /= 0 = (sumaImpares (n-1)) + n
    |otherwise = sumaImpares (n-1)
-}

nEsimoImpar :: Integer -> Integer
nEsimoImpar n = (2 * n - 1)

-- Tenemos que tener en cuenta que dado n en N, un numero impar puede expresarse como 2 * n - 1
sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = (nEsimoImpar n) + (sumaImpares (n - 1))

-- Notemos que podemos hacer lo mismo, pero con los pares
nEsimoPar :: Integer -> Integer
nEsimoPar n = (2 * n)

-- Tenemos que tener en cuenta que dado n en N, un numero par puede expresarse como 2 * n
sumaPares :: Integer -> Integer
sumaPares 0 = 0
sumaPares n = (nEsimoPar n) + (sumaPares (n - 1))

------------------------------------------------------------
{-  Ejercicio 5. Implementar la función 
    medioFact :: Integer ->Integer 
    que dado n ∈ N calcula n!! = n (n−2)(n−4) · · · .
    
    problema medioFact (n: Z) : Z {
        requiere: { n ≥ 0 }
        asegura: { resultado = \prod_{i=0}^{(n-1)/2} (n − 2 * i) }
}

Por ejemplo:
    medioFact 10 ; 10 ∗ 8 ∗ 6 ∗ 4 ∗ 2 ; 3840.
    medioFact 9 ; 9 ∗ 7 ∗ 5 ∗ 3 ∗ 1 ; 945.
    medioFact 0 ; 1.

-}
medioFact :: Integer ->Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n 
    | n>0 = n * medioFact(n-2) 

{- Ejercicio 6. Implementar la función 
    
    todosDigitosIguales :: Integer ->Bool 
    
    que determina si todos los dígitos de un
    número natural son iguales, es decir:

    problema todosDigitosIguales (n: Z) : B {
        requiere: { n > 0 }
        asegura: { resultado = true ↔ todos los d´ıgitos de n son iguales }
    }
-}
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n 
    | n < 10 = True
    | (n > 9) && (mod (div n 10) 10 == mod n 10) = todosDigitosIguales (div n 10) 
    | otherwise = False





{-Ejercicio 7. Implementar la función 
    iesimoDigito :: Integer ->Integer ->Integer 
    que dado un n ∈ Z mayor o igual
    a 0 y un i ∈ Z mayor o igual a 1 menor o igual a 
    la cantidad de dígitos de n, devuelve el i-ésimo dígito de n.
    
    problema iesimoDigito (n:Z, i:Z) : Z{
        requiere : {n >= o y 1<=i<=cantDigitos(n)}
        asegura : {resultado = (n div 10**(cantDigitos(n)-i)) mod 10}
    }

    problema cantDigitos (n:Z) : N {
        requiere : {n>=0}
        asegura : { n=0 -> resultado = 1} 
        asegura : {n not= 0 -> (n div 10^(resultado−1) > 0 ∧ n div 10^(resultado) = 0)}
    }

-}    

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
cantDigitos n | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n 1 = div n (10 ^ ((cantDigitos n)-1))
iesimoDigito n i = iesimoDigito (mod n (10 ^ ((cantDigitos n)-1))) (i-1)

{-  Ejercicio 8. 
    Especificar e implementar la función 
    sumaDigitos :: Integer -> Integer 
    que calcula la suma de dígitos de un número natural. 
    Para esta función pueden utilizar div y mod.

-}
sumaDigitos :: Integer -> Integer
sumaDigitos 1 = 1
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

{-
    Ejercicio 9. 
    Especificar e implementar una función 
    
    esCapicua :: Integer ->Bool 
    que dado n ∈ N≥0 determina si n es un número capicúa.
-}

sacarPrimeroYultimo :: Integer -> Integer
sacarPrimeroYultimo n = div (mod n (10^((cantDigitos n)-1))) 10

esCapicuaProfes :: Integer -> Bool
esCapicuaProfes n 
    | 0 <= n && n < 10 = True
    | 10 <= n && n < 100 = (iesimoDigito n 1) == (iesimoDigito n 2)
    | otherwise = primero == ultimo && esCapicuaProfes (sacarPrimeroYultimo n)
    where primero = (iesimoDigito n 1)
          ultimo = mod n 10

{- REPENSAR! 
    el 1001 no funciona
    el 10001 no funciona
-}
esCapicua :: Integer -> Bool
esCapicua n 
    | cantDigitos n == 1 = True
    | iesimoDigito n 1 /= iesimoDigito n (cantDigitos n) = False 
    | (cantDigitos n /= 1) && (primero == ultimo) = esCapicua (sacarPrimeroYultimo n)    
    where primero = iesimoDigito n 1
          ultimo = iesimoDigito n (cantDigitos n)


{- Ejercicio 10 -}
f1 :: Integer -> Integer
f1 0 = 1
f1 1 = 2
f1 n = 2^n + f1 (n-1)

f2 :: Integer -> Float -> Float
f2 1 q = 1
f2 n q | n>1 = q^n + f2 (n-1) q
 | otherwise = 0     

f3 :: Integer -> Float -> Float
f3 0 q = 1
f3 n q = q^(2*n) + f3 (n-1) q

{-  REPENSAR ESTA GAROMPA
f4 :: Integer -> Float -> Float
f4 0 q = 1
f4 n q = (q^(2*n) + f4 (n-1) q) - f2 (n) q 
f4 :: Integer -> Float -> Float
f4 n q = f3 n q - f2 (n-1) q
-}

{-Ejercicio 11. a) Especificar e implementar una funci´on eAprox :: Integer ->Float que aproxime el valor del n´umero e
a partir de la siguiente sumatoria:
    e(n) = \sum_{i=0}^{n}1/i!
b) Definir la constante e :: Float como la aproximaci´on de e a partir de los primeros 10 t´erminos de la serie anterior.
¡Atenci´on! A veces ciertas funciones esperan un Float y nosotros tenemos un Int. Para estos casos podemos utilizar la
funci´on fromIntegral :: Int ->Float definida en el Preludio de Haskell.
-}
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = (1/(fromIntegral (factorial n)) + eAprox (n-1))

e :: Float
e = eAprox 10


{-Ejercicio 12. Para n ∈ N se define la siguiente definici´on recursiva: 
a1 = 2, an = 2+ 1/(an−1)

 Utilizando esta sucesión, especificar e implementar una función 
 raizDe2Aprox :: Integer ->Float que dado n ∈ N devuelva la aproximaci´on de
2^(1/2) definida por 2^(1/2) ≈ an−1.

Por ejemplo:
raizDe2Aprox 1 ⇝ 1
raizDe2Aprox 2 ⇝ 1,5
raizDe2Aprox 3 ⇝ 1,4
-}

--Primero defino an
an :: Integer -> Float
an 1 = 2
an n = 2 + (1/(an (n-1)))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (an n) -1


{-Ejercicio 13. Implementar: f(n,m) = \sum_{i=1}^{n}(\sum_{j=1}^{m} i j)-}

{-
f2 :: Integer -> Float -> Float
f2 1 q = 1
f2 n q | n>1 = q^n + f2 (n-1) q
 | otherwise = 0
-}
sumatoria :: Float -> Float -> Float
sumatoria x 1 = x
sumatoria x n = x + sumatoria x (n-1)

fnm :: Float -> Integer -> Float
fnm n m = sumatoria (f2 m n) n 