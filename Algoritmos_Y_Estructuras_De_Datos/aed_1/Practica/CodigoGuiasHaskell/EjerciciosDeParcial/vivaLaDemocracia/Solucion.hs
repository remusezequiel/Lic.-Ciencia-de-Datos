{-# OPTIONS_GHC -Wno-overlapping-patterns #-}
module Solucion where

type Candidato = String
type Formula = (String,String)
type Formulas = [Formula]
type Votos = [Integer]
type CantTotalVotos = Integer
type Porcentaje = Float
type Recuento = (Candidato,Porcentaje)
type ListaRecuento = [Recuento]
{--
Ejercicio 1 - Votos en Blanco

problema votosEnBlanco(formulas: seq<String×String>, votos: seq<Z>, cantTotalVotos: Z) : Z{
    requiere : {formulasValidas(formulas)}
    requiere : {|formulas| = |votos|}
    requiere : { Todos los elementos de votos son mayores o iguales que 0}
    requiere : { La suma de todos los elementos de votos es menor o igual a cantT otalV otos}
    asegura : {
        res es la cantidad de votos emitidos que no correspondieron a niguna de las fórmulas que se presentaron 
    }
}
--}
recuentoDeVotosPositivos :: Votos -> Integer
recuentoDeVotosPositivos [] = 0
recuentoDeVotosPositivos (x:xs) = x + recuentoDeVotosPositivos xs


votosEnBlanco :: Formulas -> Votos -> CantTotalVotos -> Integer
votosEnBlanco _ votos totalVotos = totalVotos - (recuentoDeVotosPositivos votos)



{--
    Ejercicio 2 - Fórmulas Válidas

    problema formulasValidas(formulas : seq<String×String>) : Bool{
        requiere : {True}
        asegura : {
            (res = true) ↔ formulas no contiene nombres repetidos, es decir que cada candidato está en una única fórmula 
            (no se puede ser candidato a presidente y a vicepresidente ni en la misma fórmula ni en fórmulas distintas)
        }
    }
--}

-- Si esta repetido, devuelve True. 
-- Esto no puede pasar En una Formula
repetidoEnTupla :: Formula -> Bool
repetidoEnTupla (c1,c2) = c1==c2

-- Requiere repetidoEnTupla = False
formulaRepetidaEnFormulas :: Formula -> Formulas -> Bool
formulaRepetidaEnFormulas (cand_A,cand_B) [] = False
formulaRepetidaEnFormulas (cand_A,cand_B) ((c1,c2):cs)
    | cand_A /= c1 && cand_A /= c2 && cand_B /= c1 && cand_B /= c2  =  formulaRepetidaEnFormulas (cand_A,cand_B) cs
    | otherwise = True


formulasValidas :: Formulas -> Bool
formulasValidas [] = True
formulasValidas ((c1,c2):cs)
    | not (repetidoEnTupla (c1,c2)) && not (formulaRepetidaEnFormulas (c1,c2) cs) = formulasValidas cs
    | otherwise = False


{--
    Ejercicio 3 - Porcentaje de Votos
    
    problema porcentajeDeVotos(presidente : String, formulas : seq < String × String >, votos : seq < Z >) : R{
        requiere : {La primera componente de algun elemento de formulas es presidente}
        requiere : {formulasV alidas(formulas)}
        requiere : {|formulas| = |votos|}
        requiere : { Todos los elementos de votos son mayores o iguales que 0}
        requiere : { Hay al menos un elemento de votos que es mayor estricto que 0}
        asegura : {res es el porcentaje de votos que obtuvo la f´ormula encabezada por presidente sobre el total de votos afirmativos }
    }

Para resolver este ejercicio pueden utilizar la siguiente función que devuelve 
como Float la división entre dos números de tipo Int:
division :: Int → Int → Float
division a b = (fromIntegral a) / (fromIntegral b)

--}
division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

porcentaje :: Integer -> Votos-> Porcentaje
porcentaje votos lista_votos = division votos (recuentoDeVotosPositivos lista_votos)

auxPocentajeDeVotos :: Candidato -> Formulas -> Votos -> Votos -> Porcentaje
auxPocentajeDeVotos candidato []  (v:vs) votos = 0.0
auxPocentajeDeVotos candidato ((c11,c12):cs) (v:vs) votos
    | candidato==c11 = (porcentaje v votos) * 100
    | otherwise = auxPocentajeDeVotos candidato cs vs votos

porcentajeDeVotos :: Candidato -> Formulas -> Votos -> Porcentaje
porcentajeDeVotos candidato formulas (v:vs) =  auxPocentajeDeVotos candidato formulas (v:vs) (v:vs)

{--
    Ejercicio 4 - Próximo Presidente
    
    problema proximoPresidente(formulas : seq < String × String >, votos : seq < Z >) : String{
        requiere : {La primera componente de algun elemento de formulas es presidente}
        requiere : {formulasValidas(formulas)}
        requiere : {|formulas| = |votos|}
        requiere : { Todos los elementos de votos son mayores o iguales que 0}
        requiere : { Hay al menos un elemento de votos que es mayor estricto que 0}
        requiere : {|formulas| > 0}
        asegura : {res es el candidato a presidente de formulas m´as votado de acuerdo a los votos contabilizados en votos}
    }
--}

conteoCandidato :: Candidato -> Formulas -> Votos -> Recuento
conteoCandidato c f v = (c, porcentajeDeVotos c f v)

auxlistaConteos :: Formulas -> Formulas -> Votos -> ListaRecuento
auxlistaConteos [] _ _ = []
auxlistaConteos ((c1,c2):cs) f v = [conteoCandidato c1 f v] ++ auxlistaConteos cs f v 

listaConteos :: Formulas -> Votos -> ListaRecuento
listaConteos f v = auxlistaConteos f f v

listaPorcentajes :: ListaRecuento -> [Float]
listaPorcentajes [] = []
listaPorcentajes ((c,p):ls) = p:listaPorcentajes ls

maximo :: [Float] -> Float
maximo [t]  = t
maximo (t1:t2:ts) 
    | t1>=t2 = maximo(t1:ts)
    | otherwise = maximo(t2:ts)

auxEncontrarPresidente :: ListaRecuento -> ListaRecuento -> String
auxEncontrarPresidente [(c,p)] lr = c
auxEncontrarPresidente ((c,p):ls) lr
    | p == maximo(listaPorcentajes lr) = c
    | otherwise = auxEncontrarPresidente ls lr 

proximoPresidente :: Formulas -> Votos-> String
proximoPresidente f v = auxEncontrarPresidente (listaConteos f v) (listaConteos f v)