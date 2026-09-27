from task import Tarefa
from database import save_task, delete_task, update_status, get_task

title = input('Nome da tarefa: ')
info = input('Descrição: ')

task = Tarefa(title, info)
save_task(task)
