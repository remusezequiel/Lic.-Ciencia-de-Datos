module RelacionesValidas where

{--  
--  problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
--      requiere: {True}
--      asegura: {
--            (res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar
--              el orden)
--  }
--}

-- ¿QUE PIDE EL PROBLEMA? -> las tiplas deben ser del tipo: (x1,y1) con x1 != y1 para toda tupla de la lista. 
--                        -> Tampoco tiene que tener tuplas repetidas.
--                        -> No consideramos el orden para las tuplas repetidas. Osea, (x1,y1) != (y1,x1) 
-- relacionesValidas :: [(String,String)]->Bool  



tuplasIgualesEnRelacion :: (String,String) -> [(String,String)] -> Bool
tuplasIgualesEnRelacion (x1,y1) [] = False
tuplasIgualesEnRelacion (x1,y1) ((a,b):xs) 
    | x1==a && b==y1 = True 
    | otherwise = tuplasIgualesEnRelacion (x1,y1) xs

-- Si son distintos, devuelve True
validarRelacion :: (String,String) -> Bool
validarRelacion (x1,y1) = x1 /= y1

relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((t1,t2):ts)
    | validarRelacion (t1,t2) && not(tuplasIgualesEnRelacion (t1,t2) ts) = relacionesValidas (ts)
    | otherwise = False 
