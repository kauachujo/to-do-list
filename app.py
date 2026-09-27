import json

class Tarefa():
    def __init__(self, task, text, status='pendente', id=None):
        self.id = id
        self.task = task
        self.text = text
        self.status = status

    def alternar_status(self):
        ordem = ['pendente', 'em progresso', 'concluído']
        indice = ordem.index(self.status)
        if indice + 1 < len(ordem):
            self.status = ordem[indice + 1]
        else:
            self.status = ordem[0]

    def to_dict(self):
        return {'task': self.task, 'info': self.text, 'status': self.status, 'id': self.id}

    @staticmethod
    def from_dict(dados):
        return Tarefa(dados['id'], dados['task'], dados['text'], dados['status'])


# Carrega todas as tarefas e retorna como uma lista de dicts
def load_db():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Gera um id para a tarefa
def gerar_id(task_list):
    if not task_list:
        return 1
    return max(t['id'] for t in task_list) + 1
    

# Salva uma tarefa no json
def save_task(task):
    task_list = load_db()
    task.id = gerar_id(task_list)
    task_list.append(task.to_dict())
    with open('tasks.json', 'w') as file:
        json.dump(task_list, file, indent=2)

while True:
    title = input('title: ')
    text = input('text: ')
    task = Tarefa(title, text)
    save_task(task)