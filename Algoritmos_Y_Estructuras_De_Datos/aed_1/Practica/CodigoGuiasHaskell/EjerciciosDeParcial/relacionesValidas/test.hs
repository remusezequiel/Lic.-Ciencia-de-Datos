import Test.HUnit
import Data.List
import RelacionesValidas

testTuplasIgualesEnRelacion :: Test
testTuplasIgualesEnRelacion = test[
    "Lista vacia: No hay concidencia => no hay iguales" ~: tuplasIgualesEnRelacion ("A","B") [] ~?= False,
    "Tuplas iguales: un solo elemento en lista" ~: tuplasIgualesEnRelacion ("A","B") [("A","B")] ~?= True,
    "Tuplas iguales: 2 elementos en lista igual adelante" ~: tuplasIgualesEnRelacion ("A","B") [("A","B"),("C","B")] ~?= True,
    "Tuplas iguales: 2 elementos en lista igual atras" ~: tuplasIgualesEnRelacion ("A","B") [("C","B"),("A","B")] ~?= True,
    "Tuplas iguales: 3 elementos en lista" ~: tuplasIgualesEnRelacion ("A","B") [("C","B"),("C","D"),("A","B")] ~?= True  
    ]

testRelacionesValidas = test[
    "Relacion Valida: 2" ~: relacionesValidas [("A","B"),("B","A")] ~?= True,
    "Relacion Valida: 3" ~: relacionesValidas [("A","B"),("B","A"),("C","A")] ~?= True,
    "Relacion invalida: misma al principio y final" ~: relacionesValidas [("A","B"),("B","A"),("A","B")] ~?= False,
    "Relacion invalida: pegadas adelante" ~: relacionesValidas [("A","B"),("A","B"),("B","A")] ~?= False,
    "Relacion invalida: pegadas final" ~: relacionesValidas [("B","A"),("A","B"),("A","B")] ~?= False
    ]

todosLosTests :: Test
todosLosTests = test [
    "testTuplasIgualesEnRelacion" ~: testTuplasIgualesEnRelacion,     
    "testRelacionesValidas" ~: testRelacionesValidas
    ]

runTest :: IO Counts
runTest = runTestTT todosLosTests