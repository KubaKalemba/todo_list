from datetime import datetime


class TaskManager:
    currId = 0

    def __init__(self, database):
        self.db = database

    def create_task(self, title, description):
        task = {
            'id': TaskManager.currId,
            'title': title,
            'description': description,
            'created_at': datetime.now().isoformat(),
            'status': 'do zrobienia'
        }
        self.db.add_task(task)
        TaskManager.currId += 1
        return task

    def list_tasks(self, status=None):
        tasks = self.db.get_all_tasks()
        if status:
            tasks = [task for task in tasks if task['status'] == status]
        return tasks

    def update_task(self, task_id, title=None, description=None, status=None):
        updated_task = {}
        if title:
            updated_task['title'] = title
        if description:
            updated_task['description'] = description
        if status:
            updated_task['status'] = status
        return self.db.update_task(task_id, updated_task)

    def delete_task(self, task_id):
        return self.db.delete_task(task_id)
