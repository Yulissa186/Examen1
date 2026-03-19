# vuelos con busqueda en amplitud 
from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        nodo = nodos_frontera[0]
        # Extraer nodo y anadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo 
        else:
            # Expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            # Se agrego esta parte de codigo .get(dato_nodo, []) ya que es una conexion
            for un_hijo in conexiones.get(dato_nodo, []):
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora' : {'Zacatecas', 'Sinaloa'},
        'Guanajuato' : {'Aguascalientes'},
        'Oaxaca' : {'Queretaro'},
        'Sinaloa' : {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro' : {'Monterrey', 'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'}, 
        'Celaya' : {'Jiloyork', 'Sinaloa'},
        'Zacatecas' : {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey' : {'Zacatecas', 'Sinaloa'},
        'Tamaulipas' : {'Queretaro'},
        #'Queretaro' : {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'} #Se elimina esta linea ya que esta duplicada y asi rompe el codigo
    }

    estado_inicial = 'Jiloyork'
    solucion = 'Zacatecas'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    #Mostrar Resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() !=None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    