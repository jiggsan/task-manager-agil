tasks = []

def add_task(title, priority="Normal"):
    task = {"title": title, "priority": priority}
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def delete_task(title):
    global tasks
    tasks = [t for t in tasks if t["title"] != title]
