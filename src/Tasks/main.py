from flask import Flask, request, url_for, redirect
import task
import json

app = Flask("SS Restaurant Task Manager")

tasks = task.Tasks()

employees = {
    "emp1": "busy",
    "emp2" : "available"
}

def find_employees():
    for emp, avl in employees.items():
        if avl == "available":
            return emp

@app.route("/tasks", methods=["GET", "POST"])
def list_tasks():
    if request.method == "GET":
        return tasks.list_tasks()
    elif request.method == "POST":
        body = json.loads(request.data)
        new_task = task.Task(body["order_id"], find_employees())
        tasks.add_task(new_task)
        return redirect(url_for('get_task', task_id=new_task.id))
    
@app.route("/task/<task_id>")
def get_task(task_id):
    return tasks.get_task(task_id).json()

app.run(port='8081', debug=True)
    



