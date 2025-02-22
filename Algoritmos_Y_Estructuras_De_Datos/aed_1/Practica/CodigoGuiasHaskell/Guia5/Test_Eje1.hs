import Test.HUnit
import Data.List
import G5_Eje1

-----------------------------
--  TEST EJERCICIO 1 (1)
-----------------------------
--Casos
listaPrueba_1 = [1]
listaPrueba_2 = [1,1,1]
listaPrueba_3 = [0,0,11,1,1,1,5]
listaPrueba_4 = ["1","1","4"]
-- Pruebas longitud []
testSuiteLongitud = test [
    "CasoBase: ListaVacia" ~: (longitud []) ~?= 0,
    "ListaNumeriaUnElemento" ~: (longitud listaPrueba_1) ~?= 1
    ]

-----------------------------
--  TEST EJERCICIO 1 (2)
-----------------------------
-- Casos

-- Pruebas ultimo []
testSuiteUltimo = test[
    "CasoBase: Lista de Un elemento" ~: (ultimo listaPrueba_1) ~?= 1,
    "ListaCuyoFinalEs: 1" ~: (ultimo listaPrueba_2) ~?= 1
    ]
-----------------------------
--  TEST EJERCICIO 1 (3)
-----------------------------
-- Pruebas principio []
{-
testSuitePrincipio = test [

    ]
    -}
-----------------------------
--  TEST EJERCICIO 1 (4)
-----------------------------

------------------------------
--  A EJECUTAR
------------------------------

-- Lista con todos los Test
allTests = test [
    "longitud" ~: testSuiteLongitud,
    "ultimo" ~: testSuiteUltimo
    --"principio" ~: testSuitePrincipio,
    --"reverso" ~: testSuiteReverso
    ]

-- Corre todas las pruebas
testeando = runTestTT allTests
