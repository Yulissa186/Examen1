# Puzzle lineal con búsqueda en profundidad 

from arbol import Nodo
def buscar_solucuion_DFS (estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) !=0:
        nodo = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion econtrada
            solucion = True
            return nodo
        else:
            # Expandir nodos hijo
            dato_nodo = nodo.get_datos()

            # Operador izquierdo 
            hijo = [dato_nodo [1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
        
            # Operador Central
            hijo = [dato_nodo [0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            # Operador Derecho 
            hijo = [dato_nodo [0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
        
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__ == "__main__":
    estado_inicial = [3,2,1,4]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucuion_DFS(estado_inicial, solucion)
    # Mostrar la solucion
    resultado = []
    nodo = nodo_solucion 
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

