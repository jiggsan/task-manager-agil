class Task:
    def __init__(self, title, status="To Do"):
        self.title = title
        self.status = status

    def __repr__(self):
        return f"{self.title} - {self.status}"
