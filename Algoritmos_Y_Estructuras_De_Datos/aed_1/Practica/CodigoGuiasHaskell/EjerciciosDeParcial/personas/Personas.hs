module Personas where
 
{--
-- problema personas (relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
--      requiere: {relacionesValidas(relaciones)}
--      asegura: {
--            res tiene exactamente los elementos que figuran en alguna 
--            tupla de relaciones en cualquiera de las dos
--            posiciones, sin repetir}
--}

desrelacionar :: [(String,String)] -> [String]
desrelacionar [] = []
desrelacionar ((p1,p2):ps) = p1:p2:(desrelacionar ps)

contarRepetidos :: String -> [String] -> Integer
contarRepetidos persona [] = 0
contarRepetidos persona (p:ps)
    |p == persona = 1+contarRepetidos persona ps
    |otherwise = contarRepetidos persona ps

sacarRepetido :: [String] -> [String]
sacarRepetido  [] = []
sacarRepetido  (p:ps)
    | (contarRepetidos p (p:ps))>1 = sacarRepetido ps
    | otherwise = p:(sacarRepetido ps)

personas :: [(String,String)] -> [String]
personas [] = []
personas (p:ps) = sacarRepetido (desrelacionar (p:ps))