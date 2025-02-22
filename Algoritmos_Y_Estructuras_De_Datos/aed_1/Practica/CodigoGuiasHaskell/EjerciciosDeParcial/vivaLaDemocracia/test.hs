import Test.HUnit
import Data.List
import Solucion

-- Test Ejercicio 1
testVotosEnBlanco = test[
    "Todos En Blanco" ~: votosEnBlanco [] [] 2 ~?= 2,
    "Pruebita: " ~: votosEnBlanco [("Milei","Adorni"),("Cristina","Axel")] [5,5] 10 ~?= 0
    ]
-- Test Ejercicio 2
testFormulasValidas = test[
    "Sin Formulas" ~: formulasValidas [] ~?= True,
    "No valida: formula unica" ~: formulasValidas [("Milei","Milei")] ~?= False,
    "No valida: formula doble" ~: formulasValidas [("Milei","Adorni"),("Cristina","Axel"),("Milei","Villaruel")] ~?= False,
    "Valida: " ~: formulasValidas [("Milei","Adorni"),("Cristina","Axel")] ~?= True
    ]
-- Test Ejercicio 3
testPorcentajeDeVotos = test[
    "prueba 1" ~: porcentajeDeVotos "Milei" [("Milei","Adorni"),("Cristina","Axel")] [5,5] ~?= 0.5
    ]
-- Test Ejercicio 4


-- Lista a correr
todosLosTest = test[
    "testVotosEnBLanco" ~: testVotosEnBlanco,
    "testFormulasValidas" ~: testFormulasValidas,
    "testPorcentajeDeVotos" ~: testPorcentajeDeVotos
    ] 
-- Ejecutar
runTest = runTestTT todosLosTest
