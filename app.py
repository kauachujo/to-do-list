from task import Tarefa
from database import load_db, save_task, delete_task, update_status, get_task
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def list_tasks():
    task_list = [t.to_dict() for t in load_db()]
    return jsonify(task_list)

@app.route('/tarefas/<int:id>')
def search(id):
    task = get_task(id)
    if task is None:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    return jsonify(task.to_dict())

@app.route('/tarefas', methods=['POST'])
def register():
    data = request.get_json()
    task = Tarefa(data['task'], data['text'])
    save_task(task)



CORS(app)
print('App started')