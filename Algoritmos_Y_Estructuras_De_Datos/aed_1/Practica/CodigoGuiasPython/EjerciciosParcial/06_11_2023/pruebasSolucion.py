import solucion as sol


if __name__ == "__main__":
    # Ejercicio 1
    print("Pruebas: Ejercicio 1")
    s = [-1, 1, 0, 5, -7, 0, 3]
    n = 2
    elem = 0
    print(sol.ind_nesima_aparicion(s,n,elem))
    print(sol.alt_ind_nesima_aparicion(s,n,elem))

    # Ejercicio 2
    print("\nPruebas: Ejercicio 2")
    s1 = [1, 3, 0, 1]
    s2 = [4, 0, 2, 3]
    print(sol.mezclar(s1,s2))

    # Ejercicio 3
    print("\nPruebas: Ejercicio 3")
    caballos= ["linda", "petisa", "mister", "luck" ]
    carreras= {
        "carrera1":["linda", "petisa", "mister", "luck"],
        "carrera2":["petisa", "mister", "linda", "luck"]
    }
    print(sol.frecuencia_posiciones_por_caballo(caballos,carreras))

    # Ejercicio 4
    print("\nPruebas: Ejercicio 4")
    m = [[1,2,4,2,1],[-5,4,3,4,-5],[0,1,1,1,0]]
    print(sol.matriz_capicua(m))
