class Kanban:
    def __init__(self):
        self.columns = {
            "To Do": [],
            "Doing": [],
            "Done": []
        }

    def add_task(self, task):
        self.columns["To Do"].append(task)

    def move_task(self, task, new_status):
        for column in self.columns.values():
            if task in column:
                column.remove(task)
        self.columns[new_status].append(task)
