
class Tarefa():
    def __init__(self, task, text, status='pendente', id=None):
        self.id = id
        self.task = task
        self.text = text
        self.status = status

    def __repr__(self):
        return f'Tarefa: {self.task}, Id: {self.id}'

    def to_dict(self):
        return {'task': self.task, 'text': self.text, 'status': self.status, 'id': self.id}

    @staticmethod
    def from_dict(dados):
        return Tarefa(dados['task'], dados['text'], dados['status'], dados['id'])
