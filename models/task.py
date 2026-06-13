class Task:
    def __init__(self, id, title, status, project, user):
        self.id = id
        self.title = title
        self.status = status
        self.project = project
        self.user = user

    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status}, project={self.project}, user={self.user})"
