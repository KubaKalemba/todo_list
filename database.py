import json
import os


class Database:
    def __init__(self, filename='tasks.json'):
        self.data = None
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_all_tasks(self):
        return self.data

    def add_task(self, task):
        self.data.append(task)
        self.save_data()

    def update_task(self, task_id, updated_task):
        for task in self.data:
            if str(task['id']) == str(task_id):
                task.update(updated_task)
                self.save_data()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.data:
            print(str(task['id']) == str(task_id))
            if str(task['id']) == str(task_id):
                self.data.remove(task)
                self.save_data()
                return True
        return False
