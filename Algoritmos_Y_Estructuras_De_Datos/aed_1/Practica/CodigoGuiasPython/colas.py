from queue import Queue as Cola
import random

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   Generalidades a la hora de trabajar con Colas (Queue) 
# 
#   -> No hay que olvidarse de que una vez agarrado un item, lo vamos a perder si no 
#   lo cuardamos en una variable auxiliar
# 
#   -> Ante la duda, creas variables para no perder datos
# 
#   -> Recordar que las Colas son TAD del tipo FIFO: First in First out
#   osea, esto se debe a que el siguiente dato entrante "empuja" al primero
#   como una cola.
# #


# ejercicio auxiliar que se suele repetir en varias funciones
# 
def llenar_cola(origen:Cola, destino:Cola):
    while (not origen.empty()):
        destino.put(origen.get())

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    """Genera numeros una cierta cantidad de numeros al azar
    teniendo en cuenta la libreria random, en particular la funcion
    'randit', esta recive dos parametros en este caso
    pasados como "desde" y "hasta", los cuales indican un
    rango en el cual van a vivir estos numeros aleatorios"""
    c = Cola()

    for i in range(cantidad):
        elem = random.randint(desde, hasta)
        c.put(elem)
    return c

# ej 9
def cantidad_elementos(c: Cola) -> int:
    longitud: int = 0
    res: Cola = Cola()
    
    while not(c.empty()):
        elem = c.get()
        longitud += 1
        res.put(elem)

    # Vuelvo a llenar la cola pasada como parametro
    llenar_cola(res,c)
    
    return longitud

# ej 10
def buscar_el_maximo(c: Cola[int]) -> int:
    aux_c: Cola[int] = Cola()
    
    elem: int = c.get()
    current_max: int = elem
    aux_c.put(elem)
    
    while not(c.empty()):
        elem = c.get()
        if elem > current_max:
            current_max = elem
        aux_c.put(elem)

    llenar_cola(aux_c,c)
        
    return current_max

# ej 12
def intercalar(c1: Cola, c2: Cola) -> Cola:
    cola_aux1: Cola = Cola()
    cola_aux2: Cola = Cola()
    res: Cola = Cola()
    while not(c1.empty()) and not(c2.empty()):
        elem = c2.get()
        res.put(elem)
        cola_aux2.put(elem)
        elem = c1.get()
        res.put(elem)
        cola_aux1.put(elem)
    while not(cola_aux1.empty()):
        elem = cola_aux1.get()
        c1.put(elem)
    while not(cola_aux2.empty()):
        elem = cola_aux2.get()
        c2.put(elem)
    return res

# 13.1
def armar_secuencia_de_bingo() -> Cola[int]:
    sec_bingo: Cola[int] = Cola()
    numeros_0_99: list[int] = list(range(0,99))
    random.shuffle(numeros_0_99)
    
    for i in range(99):
        sec_bingo.put(numeros_0_99[i])

    return sec_bingo

# 13.2
def jugar_carton_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cantidad_jugadas: int = 1
    coincidencias: int = 0
    longitud_carton: int = len(carton)
    bolilla: int
    cola_aux = Cola()

    while coincidencias < longitud_carton:
        bolilla: int = bolillero.get()
        if bolilla in carton:
            coincidencias += 1
        cantidad_jugadas += 1
        cola_aux.put(bolilla)

    while not(cola_aux.empty()):
        bolilla = cola_aux.get()
        bolillero.put(bolilla)

    return cantidad_jugadas

# ej 14
def n_pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
    cola_aux: Cola[tuple[int,str,str]] = Cola()
    pacientes_urgentes: int = 0
    paciente: tuple[int,str,str]
    while not(c.empty()):
        paciente = c.get()
        if paciente[0] in [1,2,3]:
            pacientes_urgentes += 1
        cola_aux.put(paciente)
    while not(cola_aux.empty()):
        paciente = cola_aux.get()
        c.put(paciente)
    return pacientes_urgentes

# ej 15
def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    res: Cola[tuple[str,int,bool,bool]] = Cola()
    
    cola_prioridad: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_preferencial: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_resto: Cola[tuple[str,int,bool,bool]] = Cola()
    
    cliente:tuple[str,int,bool,bool] = tuple()
    
    while not(c.empty()):
        cliente = c.get()
        if cliente[3]:
            cola_prioridad.put(cliente)
        if cliente[2] and not cliente[3]:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)
        res.put(cliente)
    while not(res.empty()):
        cliente = res.get()
        c.put(cliente)
    while not(cola_prioridad.empty()):
        cliente = cola_prioridad.get()
        res.put(cliente)
    while not(cola_preferencial.empty()):
        cliente = cola_preferencial.get()
        res.put(cliente)
    while not(cola_resto.empty()):
        cliente = cola_resto.get()
        res.put(cliente)
    return res
    