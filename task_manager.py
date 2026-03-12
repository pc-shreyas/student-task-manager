import json

def add_task(task):
    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    tasks.append({"task": task, "done": False})

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)