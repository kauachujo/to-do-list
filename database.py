import json
from task import Tarefa

# Carrega todas as tarefas e retorna como uma lista de obj
def load_db():
    try:
        with open('tasks.json', 'r') as file:
            tasks_dict = json.load(file)
            return [Tarefa.from_dict(t) for t in tasks_dict]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def dump(task_list):
    with open('tasks.json', 'w') as file:
            json.dump([t.to_dict() for t in task_list], file, indent=2)

# Gera um id para a tarefa
def gerar_id(task_list):
    if not task_list:
        return 1
    return max(t.id for t in task_list) + 1
    
# Registra uma nova tarefa
def save_task(task):
    task_list = load_db()
    task.id = gerar_id(task_list)
    task_list.append(task)
    dump(task_list)

# Deleta uma tarefa
def delete_task(task_id):
    task_list = load_db()
    task_list = [t for t in task_list if t.id != task_id]
    dump(task_list)

# Atualiza o status
def update_status(task_id, new_status):
    task_list = load_db()

    for t in task_list:
        if t.id == task_id:
            t.status = new_status
            break

    dump(task_list)

# Busca e retorna o obj correspondente
def get_task(task_id):
    task_list = load_db()
    for t in task_list:
        if t.id == task_id:
            return t
    return None