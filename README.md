TaskMate CLI – Project Management Tool

Overview:

TaskMate is a simple command-line project management tool built in Python.  
It allows admins to manage users, projects, and tasks with clear object-oriented design and JSON persistence.


Features:

- Add and list users (with name + email).
- Create projects (title, description, due date).
- Assign users to projects (many-to-many relationship).
- Add tasks to projects (one-to-many relationship).
- Assign tasks to users.
- Mark tasks as complete.
- Data persistence via JSON file.
- CLI commands using `argparse`.

Commands Implemented:

1. add-user to create new users
2. list-users to show all users
3. add-project to create projects with due dates and assigned users
4. list-projects to show all projects
5. list-due-date to sort projects by due date
6. search-projects --user id to filter projects by user
7. add-task to create tasks linked to projects/users
8. list-tasks to show all tasks
