from flask import Flask, request, jsonify
from arbol import Nodo

app = Flask(__name__)

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, []):
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    hijo.set_padre(nodo)  # MUY IMPORTANTE
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None


@app.route("/", methods=["GET"])
def home():
    return '''
    <h2>Buscar ruta de vuelos</h2>
    <form action="/buscar">
        Ciudad inicial: <input type="text" name="inicio"><br><br>
        Destino: <input type="text" name="destino"><br><br>
        <input type="submit" value="Buscar ruta">
    </form>
    '''


@app.route("/buscar", methods=["GET"])
def buscar():
    inicio = request.args.get("inicio")
    destino = request.args.get("destino")

    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro': {'Monterrey', 'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
    }

    nodo_solucion = buscar_solucion_BFS(conexiones, inicio, destino)

    if nodo_solucion is None:
        return "<h3>No se encontró ruta</h3>"

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(inicio)
    resultado.reverse()

    return f"<h3>Ruta encontrada: {' → '.join(resultado)}</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)