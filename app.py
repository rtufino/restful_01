#!venv/bin/python
from flask import Flask
from flask_restful import Api
from servicios import ListaTareas, Tarea

app = Flask(__name__)
api = Api(app)

api.add_resource(ListaTareas, '/api/v1.0/tareas')
api.add_resource(Tarea, '/api/v1.0/tareas/<int:tarea_id>')


@app.route('/')
def index() -> str:
    return "Hola mundo!"


if __name__ == '__main__':
    app.run(debug=True)
