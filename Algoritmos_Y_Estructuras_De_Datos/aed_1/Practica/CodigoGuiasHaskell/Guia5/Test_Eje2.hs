import Test.HUnit
import Data.List
import G5_Eje2

-----------------------------
--  TEST EJERCICIO 2 (1)
-----------------------------

testSuitePertenece = test [
    casoBase ~: (pertenece 1 []) ~?= False,
    estaAlPrincipioInteger~: (pertenece 1 [1,3,2]) ~?= True,
    estaEnMedioInteger~: (pertenece 1 [3,1,2]) ~?= True,
    estaAlFinalInteger~: (pertenece 1 [3,2,1]) ~?= True,
    estaAlPrincipioString~: (pertenece "1" ["1","3","2"]) ~?= True,
    estaEnMedioString~: (pertenece "1" ["3","1","2"]) ~?= True,
    estaAlFinalString~: (pertenece "1" ["3","2","1"]) ~?= True,
    noEstaInteger~: (pertenece 1 [3,2]) ~?= False,
    noEstaString~: (pertenece "1" ["1","3","2"]) ~?= False
    ]


------------------------------
--  A EJECUTAR
------------------------------

-- Lista con todos los Test
allTests = test [
    "pertenece" ~: testSuitePertenece,
    ]

-- Corre todas las pruebas
testeando = runTestTT allTests
