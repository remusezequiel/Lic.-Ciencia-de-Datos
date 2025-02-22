
## Recordar: 
#   LIFO (Last in first out): Pila -> LifoQueue
# 
#   FIFO (First in First out): Cola -> Queue

"""
2) Cola en el Banco (1 puntos)
En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. 
Los clientes son representados por las tuplas (nombre, tipo afiliado) donde la primera 
componente es el nombre y el tipo afiliado puede ser "comun" o "vip".

Se nos pide implementar una función en python que dada una cola de clientes del banco, 
devuelva una nueva cola con los mismos clientes pero en donde los clientes vip estan 
primero que los clientes comunes manteniendo el orden original de los clientes vips y los comunes entre sí.


problema reordenar_cola_priorizando_vips (in filaClientes: Cola⟨String x String⟩) : Cola⟨String⟩ {
  requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
  requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip" }
  requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí }
  asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
  asegura: {|res| = |filaCliente|}
  asegura: {res no tiene elementos repetidos}
  asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
  asegura: {
    Para todo cliente c1 y cliente c2 de tipo "comun" pertenecientes a filaClientes 
    si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res
  }
  asegura: {
    Para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes si c1 aparece antes que c2 en 
    filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res
  }
}
"""
from queue import Queue as Cola

def llenar_cola(origen:Cola, destino:Cola):
    while (not origen.empty()):
        destino.put(origen.get())

def reordenar_cola_priorizando_vips(fila_clientes:Cola[tuple[str,str]])->Cola[str]:
    
    cola_vip:Cola[str] =  Cola()
    cola_comun:Cola[str] =  Cola()
    
    res:Cola[str] =  Cola()
    cola_temp:Cola[tuple[str,str]] =  Cola()

    while(not fila_clientes.empty()):
        # Tomo el cliente
        cliente:tuple[str,str] = fila_clientes.get()
        # lo ponco en la cola temporal
        cola_temp.put(cliente)
        # Si es vip, pongo el nombre en la cola_vip
        if (cliente[1]=='vip'):
            cola_vip.put(cliente[0])
        else:
            # Sino en la cola comun
            cola_comun.put(cliente[0])
    
    # lleno primero resultado con la cola vip
    llenar_cola(cola_vip,res)
    # despues con la cola resultado
    llenar_cola(cola_comun,res)
    # y por ultimo, vuelvo a llenar la fila_clientes con los elementos de la cola temporal
    llenar_cola(cola_temp,fila_clientes)

    return res


if __name__ == "__main__":

    filaClientes:Cola[tuple[str,str]] = Cola[("Juan","vip"),("Carlos","comun"),("pepe","vip"),("pedro","vip"),("chola","vip")]
    
    
    print("reordenada: ", reordenar_cola_priorizando_vips(filaClientes))
    print("filaClientes: ", filaClientes)