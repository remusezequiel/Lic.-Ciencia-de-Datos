module Guia3_AED1 
where

import System.Win32 (SECURITY_ATTRIBUTES(bInheritHandle), cOLOR_ACTIVEBORDER)
import GHC.ResponseFile (escapeArgs)


{- GUIA 3 :  ALGORITMOS Y ESTRUCTURA DE DATOS 1 -}

-----------------------------------------------------------------------------------------------------------------------------------
{-  EJERCICIO 1:
    a)Implementar la función parcial f :: Integer -> Integer definida por extensión de la siguiente manera:
        f(1)=8 ; f(4)=131 ; f(16)=16 

    cuya especificación es la siguiente:
    
    problema f (n: Z) : Z {
        requiere: {n = 1 ∨ n = 4 ∨ n = 16}
        asegura: {(n = 1 → result = 8) ∧ (n = 4 → result = 131) ∧ (n = 16 → result = 16)}
    }

    b) Análogamente, especificar e implementar la función parcial g :: Integer ->Integer
        g(8) = 16
        g(16) = 4
        g(131) = 1
    c) A partir de las funciones definidas en los ítem 1 y 2, implementar las funciones parciales h = f ◦ g y k = g ◦ f
-}

-- OBSERVACIÓN: Las funciones parciales son funciones en las cuales se indefinen para ciertos argumentos.

f :: Integer -> Integer
f n
    | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

g :: Integer -> Integer
g n
    | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

-----------------------------------------------------------------------------------------------------------------------------------
{- Ejercicio 2. ⋆ Especificar e implementar las siguientes funciones, incluyendo su signatura.
    a) absoluto: calcula el valor absoluto de un número entero.
    b) maximoabsoluto: devuelve el máximo entre el valor absoluto de dos números enteros.
    c) maximo3: devuelve el máximo entre tres números enteros.
    d) algunoEs0: dados dos números racionales, decide si alguno de los dos es igual a 0 (hacerlo dos veces, una usando pattern
matching y otra no).
    e) ambosSon0: dados dos números racionales, decide si ambos son iguales a 0 (hacerlo dos veces, una usando pattern matching
y otra no).
    f) mismoIntervalo: dados dos números reales, indica si están relacionados considerando la relación de equivalencia en R
cuyas clases de equivalencia son: (−∞, 3], (3, 7] y (7,∞), o dicho de otra forma, si pertenecen al mismo intervalo.
    g) sumaDistintos: que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).
    h) esMultiploDe: dados dos números naturales, decidir si el primero es múltiplo del segundo.
    i) digitoUnidades: dado un número entero, extrae su dígito de las unidades.
    j) digitoDecenas: dado un número entero mayor a 9, extrae su dígito de las decenas.
-}

absoluto :: Integer -> Integer
absoluto n
    | n >= 0 = n
    | n < 0 = -n

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto a b
    | absoluto a >= absoluto b = a
    | absoluto a < absoluto b = b

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c
    | a > b && a > c = a
    | a < b && b > c = b
    | a < b && b < c = c

algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 a b
    | a /= 0 && b /= 0 = False
    | otherwise = True

ambosSon0 :: Integer -> Integer -> Bool
ambosSon0 a b
    | a == b && a == 0 = True
    | otherwise = False

--mismoIntervalo

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c
    | a == b && a == c = a
    | a == b = a+c
    | a == c = a+b
    | otherwise = a+b+c

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b
    | absoluto a >= absoluto b && mod a b == 0 = True
    | otherwise = False

-- Si a estas dos funciones las haces sin calcular el valor absoluto
-- vas a tener problemas a la hora de tomar el ultimo digito
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (absoluto n) 10

digitoDecenas :: Integer -> Integer
digitoDecenas n = digitoUnidades (div n 10)

-----------------------------------------------------------------------------------------------------------------------------------
{-Ejercicio 3. Implementar una función 

    estanRelacionados :: Integer ->Integer ->Bool
    problema estanRelacionados (a:Z, b:Z) : Bool {
        requiere: {a ̸= 0 ∧ b ̸= 0}
        asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k ̸= 0)}
    }
Por ejemplo:
estanRelacionados 8 2 ⇝ True porque existe un k = −4 tal que 82 + 8 × 2 × (−4) = 0.
estanRelacionados 7 3 ⇝ False porque no existe un k entero tal que 72 + 7 × 3 × k = 0.

-}
estanRelacionados :: Integer -> Integer ->Bool
estanRelacionados a b
    | a == 0 || b == 0 = False
    | mod a b == 0 =  True
    | otherwise = False

-----------------------------------------------------------------------------------------------------------------------------------
{- Ejercicio 4.⋆ Especificar e implementar las siguientes funciones utilizando tuplas para representar pares, ternas de números.

    a) prodInt: calcula el producto interno entre dos tuplas R × R. 
    b) todoMenor: dadas dos tuplas R×R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada
    correspondiente de la segunda tupla.
    c) distanciaPuntos: calcula la distancia entre dos puntos de R2.
    d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
    e) sumarSoloMultiplos: dada una terna de n´umeros enteros y un natural, calcula la suma de los elementos de la terna que
    son múltiplos del número natural. Por ejemplo:
        sumarSoloMultiplos (10,-8,-5) 2 ⇝ 2
        sumarSoloMultiplos (66,21,4) 5 ⇝ 0
        sumarSoloMultiplos (-30,2,12) 3 ⇝ -18
    f) posPrimerPar: dada una terna de enteros, devuelve la posici´on del primer número par si es que hay alguno, y devuelve
    4 si son todos impares.
    g) crearPar :: a ->b ->(a, b): crea un par a partir de sus dos componentes dadas por separado (debe funcionar para
    elementos de cualquier tipo).
    h) invertir :: (a, b) ->(b, a): invierte los elementos del par pasado como parámetro (debe funcionar para elementos
    de cualquier tipo).
    i) Reescribir los ejercicios prodInt, todoMenor y distanciaPuntos usando el siguiente renombre de tipos: type Punto2D
    = (Float, Float) 
-}

{- (a) 
    prodInt :: (Num, Num) -> (Num, Num) -> Num 
    problema prodInt ((v1:R,v2:R) , (w1:R,w2:R)) : Num {
        requiere: (v1,v2) in R^2 y (w1,w2) in R^2
        asegura: {(res = v1 ∗ w1 + v2 ∗ w2)}
    }
-}

prodInt :: Num a => (a, a) -> (a, a) -> a
prodInt (v1,v2) (w1,w2) = v1*w1 + v2*w2

{- b) 
    todoMenor :: Num a => (a, a) -> (a, a) -> Bool 
    problema todoMenor ((v1:R,v2:R) ; (w1:R,w2:R)) : Bool {
        requiere: (v1,v2) in R^2 y (w1,w2) in R^2
        asegura: {(res = True) sii v1 < v2 y w1 < w2}
    }
-}
todoMenor :: (Num a, Ord a) => (a, a) -> (a, a) -> Bool
todoMenor (v1,v2) (w1,w2)
    | v1 < w1 && v2 < w2 = True
    | otherwise = False

{- c)
    distanciaPuntos :: Num a => (a, a) -> (a, a) -> a
    problema distanciaPuntos ((v1:R,v2:R) ; (w1:R,w2:R)) : Num {
        requiere: (v1,v2) in R^2 y (w1,w2) in R^2
        asegura: {(res = d) sii d*d = (w1 * w1 - v1 * v1) + (w2 * w2 - v2 * v2)}
    }
-}
distanciaPuntos :: (Num a, Floating a) => (a, a) -> (a, a) -> a
distanciaPuntos (v1,v2) (w1,w2) = sqrt ((w1*w1 - v1*v1) + (w2*w2 - v2*v2))

{- d) 
    sumaTerna :: (Integer , Integer , Integer ) -> Integer
    problema sumaTerna (v1:R,v2:R,v3:R) : Floating {
        requiere: (v1,v2,v3) in R^3 
        asegura: {res = v1+v2+v3}
    }
-}
sumaTerna :: (Integer , Integer , Integer ) -> Integer
sumaTerna (v1,v2,v3) = v1+v2+v3

{- e) 
    sumarSoloMultiplos :: (Integer , Integer , Integer ) -> Integer -> Integer
    problema sumarSoloMultiplos ((x:R,y:R,z:R), r:N) : Integer {
        requiere: (x,y,z) in Z^3 && r in N 
        asegura: {(res = {sum(t_i in (t_1,t_2,t_3)} sii mod t_i r == 0 )   }
    }
-}
-- El recomendado por La IA de Bing.Usa listas contraidas
sumarSoloMultiplosBing :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplosBing (x, y, z) n = sum [a | a <- [x, y, z], mod a n == 0]



-- En mi caso, uso directamente las tuplas, pero para eso utilizo 
-- dos funciones auxiliares para llegar al cometido

agregoElTrue :: Integer -> Integer -> Integer
agregoElTrue x n
    | not (esMultiploDe x n) = x
    | otherwise = 0

identificarMultiplos :: (Integer, Integer, Integer) -> Integer -> (Integer, Integer, Integer)
identificarMultiplos (x, y, z) n = (agregoElTrue x n, agregoElTrue y n, agregoElTrue z n)

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) n = sumaTerna( identificarMultiplos (x, y, z) n) 


{- f) 
    posPrimerPar
    problema posPrimerPar ((x:Z,y:Z,z:Z), r:N) : Integer){
        requiere:  (x,y,z) in Z^3 && r in N
        asegura: posición del Primer numero par encontrado. Si todos son pares devuelve 4
    }
-}
esPar :: Integer -> Bool
esPar x
    | mod x 2 == 0 = True
    | otherwise = False

posPrimerPar :: (Integer , Integer, Integer) -> Integer
posPrimerPar (x,y,z)
    | esPar x = 1
    | esPar y = 2
    | esPar z = 3
    | otherwise = 4


{-  g) crearPar IMPLEMENTAR ESPECIFICACIÓN

-}

crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

{- h) invertir IMPLEMENTAR ESPECIFICACIÓN

-}
invertir :: (a, b) -> (b, a)
invertir (x, y) = (y, x)

{- i) Reescribir los ejercicios prodInt, todoMenor y distanciaPuntos usando el siguiente renombre de tipos: type Punto2D
    = (Float, Float) 

        IMPLEMENTAR ESPECIFICACIÓN

    -}
------------------------------------------------------------------------------------------
{-Ejercicio 5. Implementar la función todosMenores :: (Integer, Integer, Integer) ->Bool
    problema todosMenores (t : Z × Z × Z) : Bool {
        requiere: {True}
        asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
    }
    problema f_ej5 (n: Z) : Z {
        requiere: {True}
        asegura: {(n ≤ 7 → res = n2) ∧ (n > 7 → res = 2n − 1)}
    }
    problema g_ej5 (n: Z) : Z {
        requiere: {True}
        asegura: {Si n es un n´umero par, entonces res = n/2, en caso contrario, res = 3n + 1}
    }
-}

esNumeroPar :: Integer -> Bool
esNumeroPar n 
    | mod (absoluto n) 2 == 0 = True
    | otherwise = False

f_ej5 :: Integer -> Integer
f_ej5 n 
    | n <= 7 = n * n
    | otherwise = 2 * n - 1

g_ej5 :: Integer -> Integer
g_ej5 n 
    | esNumeroPar n == True = div n 2
    | otherwise = 3 * n + 1 

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (t1, t2, t3)
    | (f_ej5 t1 > g_ej5 t1) && (f_ej5 t2 > g_ej5 t2) && (f_ej5 t3 > g_ej5 t3) = True
    | otherwise = False

------------------------------------------------------------------------------------------
{- Ejercicio 6. Usando los siguientes tipos:
type Anio = Integer
type EsBisiesto = Bool

Programar una función bisiesto :: Anio -> EsBisiesto según la siguiente especificaci´on:
    problema bisiesto (año: Z) : Bool {
        requiere: {True}
        asegura: {res = false ↔ año no es múltiplo de 4, o a˜no es múltiplo de 100 pero no de 400}
    }

Por ejemplo:
bisiesto 1901 ⇝ False, bisiesto 1904 ⇝ True,
bisiesto 1900 ⇝ False, bisiesto 2000 ⇝ True.

-}

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto n 
    | not (esMultiploDe n 4) || ( esMultiploDe n 100 && not(esMultiploDe n 400)) = False
    | otherwise = True

------------------------------------------------------------------------------------------
{-Ejercicio 7. a) Implementar una funci´on:
distanciaManhattan:: (Float, Float, Float) ->(Float, Float, Float) ->Float
    problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
        requiere: {True}
        asegura: {res = \sum_{i=0}^{2} |pi − qi|}
}

Por ejemplo:
distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8

b) Reimplementarla teniendo en cuenta el siguiente tipo: 
type Coordenada3d = (Float, Float, Float)

-}


{- --VERSION SIN type
sumaTernaReal :: (Float, Float, Float) -> ( Float, Float, Float)
sumaTernaReal (v1,v2,v3) = v1+v2+v3

resta :: Float -> Float
resta x y = x - y

absolutoReal :: Float -> Float
absolutoReal n
    | n >= 0 = n
    | n < 0 = -n
distanciaManhattan :: (Float, Float, Float) -> ( Float, Float, Float) -> ( Float, Float, Float)
distanciaManhattan (a, b, c) (x, y, z) = sumaTernaReal ( absolutoReal (resta a x),  absolutoReal (resta b y), absolutoReal (resta c z))
-}

type Coordenada3d = (Float, Float, Float)


sumaTernaReal :: Coordenada3d -> Float
sumaTernaReal (v1,v2,v3) = v1+v2+v3

resta :: Float -> Float -> Float
resta x y = x - y

absolutoReal :: Float -> Float
absolutoReal n
    | n >= 0 = n
    | n < 0 = -n

distanciaManhattan :: Coordenada3d -> Coordenada3d -> Float
distanciaManhattan (a, b, c) (x, y, z) = sumaTernaReal ( absolutoReal (resta a x),  absolutoReal (resta b y), absolutoReal (resta c z))



{-Ejercicio 8. Implementar una funci´on 
    comparar :: Integer ->Integer ->Integer
    
    problema comparar (a:Z, b:Z) : Z {
        requiere: {True}
        asegura: {(res = 1 ↔ sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
        asegura: {(res = −1 ↔ sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
        asegura: {(res = 0 ↔ sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
    }
    
    problema sumaUltimosDosDigitos (x: Z) : Z {
        requiere: {True}
        asegura: {res = (|x| mod 10) + (⌊(|x|/10)⌋ m´od 10)}
    }

Por ejemplo:
comparar 45 312 ⇝ -1 porque 45 ≺ 312 y 4 + 5 > 1 + 2.
comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45.

-}

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos n = digitoUnidades n + digitoDecenas n  

comparar :: Integer -> Integer -> Integer 
comparar a b 
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | otherwise = 0