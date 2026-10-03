from task import Tarefa
from database import load_db, save_task, delete_task, update_status, get_task, dump
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/tarefas', methods=['POST'])
def register():
    data = request.get_json()
    task = Tarefa(data['task'], data['text'])
    save_task(task)
    return jsonify(task.to_dict()), 201


@app.route('/tarefas', methods=['GET'])
def list_tasks():
    task_list = [t.to_dict() for t in load_db()]
    return jsonify(task_list), 200


@app.route('/tarefas/<int:id>', methods=['GET'])
def search(id):
    task = get_task(id)
    if task is None:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    return jsonify(task.to_dict()), 200


@app.route('/tarefas/<int:id>', methods=['PUT'])
def update(id):
    task = get_task(id)
    if task is None:
            return jsonify({'erro': 'tarefa não encontrada'}), 404
    data = request.get_json()
    update_status(id, data['status'])
    return jsonify(get_task(id).to_dict()), 200


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def delete(id):
    task = get_task(id)
    if task is None:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    delete_task(id)
    return "", 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
print('App started')