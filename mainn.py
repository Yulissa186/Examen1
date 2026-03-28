from flask import Flask, request
from arbol import Nodo

app = Flask(__name__)

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()

            # Operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)

            # Operador central
            hijo2 = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo2)

            # Operador derecho
            hijo3 = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo3)

            for hijo in [hijo_izquierdo, hijo_central, hijo_derecho]:
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    hijo.set_padre(nodo)
                    nodos_frontera.append(hijo)

            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

    return None


@app.route("/")
def home():
    return '''
    <html>
    <head>
        <title>Puzzle DFS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #fbc2eb, #a18cd1);
                text-align: center;
                padding-top: 50px;
            }
            .contenedor {
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 300px;
                margin: auto;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
            }
            h2 {
                color: #a64ac9;
            }
            input[type="text"] {
                width: 90%;
                padding: 8px;
                margin: 10px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            input[type="submit"] {
                background-color: #d291ff;
                border: none;
                padding: 10px 20px;
                border-radius: 10px;
                color: white;
                cursor: pointer;
                font-weight: bold;
            }
            input[type="submit"]:hover {
                background-color: #a64ac9;
            }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h2>Puzzle DFS</h2>
            <form action="/buscar">
                Estado inicial:<br>
                <input type="text" name="inicio" placeholder="1,2,3,4"><br>
                Estado objetivo:<br>
                <input type="text" name="fin" placeholder="1,2,3,4"><br>
                <input type="submit" value="Resolver">
            </form>
        </div>
    </body>
    </html>
    '''


@app.route("/buscar")
def buscar():
    inicio = request.args.get("inicio")
    fin = request.args.get("fin")

    try:
        estado_inicial = list(map(int, inicio.split(",")))
        solucion = list(map(int, fin.split(",")))
    except:
        return '''
        <h3 style="color:white; text-align:center;">Error: formato incorrecto</h3>
        <body style="background: linear-gradient(135deg, #fbc2eb, #a18cd1);"></body>
        '''

    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    if nodo_solucion is None:
        return '''
        <h3 style="color:white; text-align:center;">No se encontró solución</h3>
        <body style="background: linear-gradient(135deg, #fbc2eb, #a18cd1);"></body>
        '''

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    return f'''
    <body style="background: linear-gradient(135deg, #fbc2eb, #a18cd1); text-align:center; font-family:Arial;">
        <div style="background:white; padding:20px; border-radius:15px; width:60%; margin:auto; margin-top:50px;">
            <h2 style="color:#a64ac9;">Solución encontrada</h2>
            <p style="font-size:18px;">{' → '.join(map(str, resultado))}</p>
            <a href="/" style="text-decoration:none; color:white; background:#d291ff; padding:10px 15px; border-radius:10px;">Volver</a>
        </div>
    </body>
    '''


if __name__ == "__main__":
    app.run()
    