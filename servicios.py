from flask_restful import Resource, abort, request

TAREAS = [
    {
        'id': 1,
        'titulo': 'Aprender Flask Restful',
        'descripcion': 'Hacer un ejemplo básico con Flask y RESTful.',
        'hecho': False
    },
{
        'id': 2,
        'titulo': 'Aprender Docker',
        'descripcion': 'Entender la tecnología y estudiar un ejemplo.',
        'hecho': False
    },
    {
        'id': 3,
        'titulo': 'Aprender Google Cloud',
        'descripcion': 'Crear una cuenta en GCP y empezar hacer pruebas.',
        'hecho': False
    }
]


def obtener_indice_tarea(tarea_id):
    i = 0
    for tarea in TAREAS:
        if tarea['id'] == tarea_id:
            return i
        i += 1
    abort(404, message="Tarea con id={} no existe".format(tarea_id))


class ListaTareas(Resource):
    def get(self):
        # $ curl -i -X GET http://localhost:5000/api/v1.0/tareas
        return {"tareas": TAREAS}, 200

    def post(self):
        # $ curl -i -H "Content-Type: application/json" -X POST -d '{"titulo":"Investigar SOAP","descripcion":"Buscar
        # información sobre esta tecnología"}' http://localhost:5000/api/v1.0/tareas
        if not request.is_json:
            abort(404, message="La petición no se encuentra en formato application/json")
        tarea = {
            'id': TAREAS[-1]['id'] + 1,
            'titulo': request.json['titulo'],
            'descripcion': request.json['descripcion'],
            'hecho': False
        }

        TAREAS.append(tarea)

        return {'tarea': tarea}, 200


class Tarea(Resource):
    def get(self, tarea_id):
        # $ curl -i -X GET http://localhost:5000/api/v1.0/tareas/2
        posicion = obtener_indice_tarea(tarea_id)
        return {"tarea": TAREAS[posicion]}, 200

    def put(self, tarea_id):
        # $ curl -i -H "Content-Type: application/json" -X PUT -d '{"titulo":"Aprender SOAP","descripcion":"Buscar
        # información sobre esta tecnología","hecho":true}' http://localhost:5000/api/v1.0/tareas/1
        if not request.is_json:
            abort(404, message="La petición no se encuentra en formato application/json")
        posicion = obtener_indice_tarea(tarea_id)
        TAREAS[posicion]['titulo'] = request.json['titulo']
        TAREAS[posicion]['descripcion'] = request.json['descripcion']
        TAREAS[posicion]['hecho'] = request.json['hecho']

        return {"tarea": TAREAS[posicion]}, 200

    def delete(self, tarea_id):
        posicion = obtener_indice_tarea(tarea_id)
        del TAREAS[posicion]
        return {'message': 'OK'}, 201
