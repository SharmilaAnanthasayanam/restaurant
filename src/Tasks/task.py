import uuid

class Tasks:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        task_list = []
        for task in self.tasks:
            task_list.append(task.json())
        return task_list
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return False, "Task not Found"
    
    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, order_id, assignee):
        self.id = str(uuid.uuid4())
        self.order_id = order_id
        self.assignee = assignee

    def json(self):
        return {"task_id": self.id, "order_id": self.order_id, "assignee": self.assignee}





