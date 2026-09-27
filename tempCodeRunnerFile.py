def load_db():
    with open('tasks.json', 'r') as file:
        return json.load(file)