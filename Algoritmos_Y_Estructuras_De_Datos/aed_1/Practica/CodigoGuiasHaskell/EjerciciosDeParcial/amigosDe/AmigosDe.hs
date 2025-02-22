module AmigosDe where
import GHC.Conc (pseq)

type Persona = String
type Relaciones = [(Persona,Persona)] 
type ConjuntoPersonas = [Persona]

{-- 
--  problema amigosDe (personas: String, relaciones: seqhStringxStringi) :seqhStringi {
--      requiere: { relacionesValidas(relaciones) }
--      asegura: { 
            res tiene exactamente los elementos que figuran en las tuplas 
            de relaciones en las que una de sus componentes es persona
        } 
--}

personaEnTupla :: Persona -> Relaciones -> Relaciones
personaEnTupla persona [] = [] 
personaEnTupla persona ((p1,p2):ps)
    | p1==persona = (p1,p2):(personaEnTupla persona ps)
    | p2==persona = (p1,p2):(personaEnTupla persona ps)
    | otherwise = personaEnTupla persona ps

{--
    Toma a una persona que quiere saber con que amigos se relaciona, una relacion
    dada por la funcion "personaEnTupla" y nos da una lista de personas, (las cuales 
    pueden estar repetidas) que se relacionan con esa persona, osea, son amigos 
--}
tomarAmigos :: Persona -> Relaciones -> ConjuntoPersonas
tomarAmigos persona [] = []
tomarAmigos persona ((p1,p2):ps)
    | persona == p1 = p2:(tomarAmigos persona ps)
    | persona == p2 = p1:(tomarAmigos persona ps)
    | otherwise = tomarAmigos persona ps

contadorRepetidos :: Persona -> ConjuntoPersonas -> Integer
contadorRepetidos persona [] = 0
contadorRepetidos persona (p:ps)
    | persona == p = 1 + contadorRepetidos persona ps
    | otherwise = contadorRepetidos persona ps
{--

--}
sacarRepetidos :: ConjuntoPersonas -> ConjuntoPersonas
sacarRepetidos [] = []
sacarRepetidos (p:ps)
    | (contadorRepetidos p ps)>0 = sacarRepetidos ps
    | otherwise = p:(sacarRepetidos ps)

amigosDe :: Persona -> Relaciones -> ConjuntoPersonas
amigosDe persona [] = []
amigosDe persona (p:ps) = sacarRepetidos(tomarAmigos persona (p:ps))