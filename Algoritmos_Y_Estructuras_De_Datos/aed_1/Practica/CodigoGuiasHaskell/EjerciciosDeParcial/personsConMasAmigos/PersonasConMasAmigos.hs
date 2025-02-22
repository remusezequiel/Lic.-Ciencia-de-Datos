module PersonasConMasAmigos where
{--
--  problema personaConMasAmigos (relaciones: seq(StringxString)) : String {
--      requiere: { relaciones no vacía }
--      requiere: { relacionesValidas(relaciones) }
--      asegura: { res es el Strings que aparece más veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
--}

type Persona = String
type Personas = [String]
type Relaciones = [(String,String)]
{--
enCuantasTuplasEsta :: Persona -> Relaciones -> Integer
enCuantasTuplasEsta persona [] = 0
enCuantasTuplasEsta persona ((p1,p2):ps)
    | persona == p1 || persona == p2 = 1 + enCuantasTuplasEsta persona ps
    | otherwise = enCuantasTuplasEsta persona ps

--listaDeAparicionesDeCadaPersona :: Relaciones -> (Persona,Integer)
--}

tuplasEnLaQueApacere :: Persona -> Relaciones -> Relaciones
tuplasEnLaQueApacere persona [] = []
tuplasEnLaQueApacere persona ((p1,p2):ps)
    | persona == p1 || persona == p2 = (p1,p2):pasoRecursivo
    | otherwise = pasoRecursivo
        where pasoRecursivo = tuplasEnLaQueApacere persona ps

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

cuantasVecesAparece :: Relaciones -> [(Persona,Integer)]
cuantasVecesAparece [] = []
cuantasVecesAparece ((p1,p2):ps) = (p1,longitud(primera)):(p2,longitud(segunda)):(cuantasVecesAparece ps)
    where
        primera = tuplasEnLaQueApacere p1 ((p1,p2):ps)
        segunda = tuplasEnLaQueApacere p2 ((p1,p2):ps)

personaQueMasAparece :: [(Persona,Integer)] -> Persona
personaQueMasAparece [(persona,cantidad)] = persona
personaQueMasAparece ((persona1,cantidad1):(persona2,cantidad2):ps) 
    | cantidad1>=cantidad2 = personaQueMasAparece ((persona1,cantidad1):ps)
    | otherwise = personaQueMasAparece ((persona2,cantidad2):ps)


personaConMasAmigos :: Relaciones -> String  
personaConMasAmigos [(p1,p2)] = p1
personaConMasAmigos ((p1,p2):ps) = personaQueMasAparece(cuantasVecesAparece ((p1,p2):ps))