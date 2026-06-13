class Project:
    def __init__(self, id, title, description, due_date, users):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.users = users

    def __str__(self):
        return (f"Project(id={self.id}, title={self.title}, "
                f"description={self.description}, due_date={self.due_date}, users={self.users})")
