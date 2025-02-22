from queue import Queue as Cola

def torneo_de_gallinas(estrategias:dict[str,str])->dict[str,int]:
    res:dict[str,int] = dict()

    for e in estrategias.keys():
        print(e)

    for j1,e1 in estrategias.items():
        res[j1] = 0
        for j2,e2 in estrategias.items():
            if (j1 != j2):
                if (e1== 'me desvio siempre' and e2 == e1):
                    res[j1] -=10
                elif (e1 == 'me desvio siempre' and e2 != e1 ):
                    res[j1] -= 15
                elif (e1 != 'me desvio siempre' and e2 == e1):
                    res[j1] -= 5
                else:
                    res[j1] += 10
    
    return res

def llenar_cola(origen:Cola, destino:Cola):
    while (not origen.empty()):
        destino.put(origen.get())

def reordenar_cola_priorizando_vips(fila_clientes:Cola[tuple[str,str]])->Cola[str]:
    
    cola_vip:Cola[str] =  Cola()
    cola_comun:Cola[str] =  Cola()
    
    res:Cola[str] =  Cola()
    cola_temp:Cola[tuple[str,str]] =  Cola()

    while(not fila_clientes.empty()):
        cliente:tuple[str,str] = fila_clientes.get()
        cola_temp.put(cliente)
        if (cliente[1]=='vip'):
            cola_vip.put(cliente[0])
        else:
            cola_comun.put(cliente[0])
    
    llenar_cola(cola_vip,res)
    llenar_cola(cola_comun,res)
    llenar_cola(cola_temp,fila_clientes)

    return res
    


def palindromo(texto:str)->bool:
    for i in range(len(texto)//2):
        if (texto[i]!=texto[len(texto)-i-1]):
            return False
    return True

def cuantos_sufijos_son_palindromos(texto:str)->int:
    candidato:str = ''
    res:int = 0
    for i in range(len(texto)-1,-1,-1):
        candidato = texto[i] + candidato
        if (palindromo(candidato)):
            res += 1
    return res



def hay_3_letras(tablero:list[list[str]], letra:str)->bool:

    for j in range(len(tablero)):
        for i in range(len(tablero[0])-2):
            if (tablero[i][j] ==  tablero[i+1][j] ==  tablero[i+2][j] == letra):
                return True
    return False

def quien_gano_el_tateti_facilito(tablero:list[list[str]])->int:
    
    hay_3_X = hay_3_letras(tablero,'X')
    hay_3_O = hay_3_letras(tablero,'O')

    if (hay_3_X and hay_3_O):
        return 3
    elif (hay_3_X):
        return 1
    elif (hay_3_O):
        return 2
    else:
        return 0



