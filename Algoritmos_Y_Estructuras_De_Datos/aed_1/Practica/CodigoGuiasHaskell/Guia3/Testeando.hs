import Guia3_AED1
import Text.Printf

main :: IO ()
main = do   
    putStrLn "-----------------------"
    putStrLn " Testeos de Guia3_AED1 "
    putStrLn "-----------------------"
    printf "\n"
    putStrLn " Testeando Ejercicio 1: "

    let test1Eje1 = f 1 
    printf "\t\t f 1: \t %d \n"  test1Eje1

    let test2Eje1 = f 4 
    printf "\t\t f 4: \t %d \n" test2Eje1

    let test3Eje1 = f 16 
    printf "\t\t f 16: \t %d \n" test3Eje1

    let test5Eje1 = g 8 
    printf "\t\t g 8: \t %d \n"  test1Eje1

    let test6Eje1 = g 16 
    printf "\t\t g 16: \t %d \n" test2Eje1

    let test7Eje1 = g 131 
    printf "\t\t g 131: \t %d \n" test3Eje1

    let test8Eje1 = h 131 
    printf "\t\t g 131: \t %d \n" test3Eje1

{-  CASOS QUE DEBEN ROMPER PARA EL EJERCICIO 1
    --let test4Eje1 = f 0 
    --printf "\t\t f 0: \t %d \n" test4Eje1

    --let test8Eje1 = g 0 
    --printf "\t\t f 0: \t %d \n" test4Eje1
-}
    {-Seguir implementando test, tener en cuenta que 
    ára el uso de Float en printf debemos poner %.2f, para strings %s y para Integer %d-}

    printf "\n"
    putStrLn " Testeando Ejercicio 2: "