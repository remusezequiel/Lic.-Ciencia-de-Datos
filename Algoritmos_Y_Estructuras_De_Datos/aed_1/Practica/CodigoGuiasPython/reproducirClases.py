import webbrowser as web

def reproducir(cursos, opcion_elegida):
    
    for curso,link in cursos.items():
        if curso==opcion_elegida:
            return web.open(link)

def menu(cursos:dict[str,str]):
    print("\tOPCIONES: ")
    print("\nIngrese el nombre de la materia como input\n")
    opcion:int=1
    for curso,link in cursos.items():
        print(str(opcion),") ", curso)
        opcion+=1

if __name__=="__main__":
    # urls:

    cursos:dict[str,str] = {
        "Mate 1: Bonder": "https://www.youtube.com/c/An%C3%A1lisis1ExactasUBA",
        "F1": "https://www.youtube.com/watch?v=RREakbV_cO4&list=PLNbPNPgqTfs4sH3j25Spm9x-VZtX8YyHZ",
        "F2": "https://www.youtube.com/watch?v=DfJJe3KxMIg&list=PLNbPNPgqTfs61WyQYK5eSeLwSApq9oh_e",
        "F3": "https://www.youtube.com/watch?v=BlmzLXI8740&list=PLNbPNPgqTfs64aJF2eh_nCKicMtIh3lRh",
        "P.F3: David": "https://www.youtube.com/playlist?list=PLDs5HxR1M_m_QdTh-bNcrJYsgLHuXFHNo",
        "F4": "https://www.youtube.com/watch?v=wPLGFfnfajU&list=PLNbPNPgqTfs5M3WebWIzu6AkDYHDi-Ew5",
        "MC": "https://www.youtube.com/watch?v=r9mMuzu6NjY&list=PLNbPNPgqTfs6gdtl-OD7utWh_volBkXux",
        "Teo1": "https://www.youtube.com/watch?v=alTBcmeHPvI&list=PLNbPNPgqTfs4sUtdAUJUiV2nS1kjIZMY-",
        "Teo2": "https://www.youtube.com/watch?v=5FBtSlomhpc&list=PLNbPNPgqTfs7RhfLKlMwn8EdWxRxqGOBQ",
        "P.Teo2": "https://www.youtube.com/watch?v=CdTFz0eNtiM&list=PLNbPNPgqTfs6unFcK2r0NGDDOJsRBEedf",
        "Teo3": "https://www.youtube.com/watch?v=kkSTJ7k1mu0&list=PLNbPNPgqTfs41JhSZjGINWnP1LIzmAoK4"
    }
    menu(cursos)
    link = input("Que curso queres Reproducir? ") 
    reproducir(cursos,link)