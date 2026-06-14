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

add-user to create new users
list-users to show all users
add-project to create projects with due dates and assigned users
list-projects to show all projects
list-due-date to sort projects by due date
search-projects --user id to filter projects by user
add-task to create tasks linked to projects/users
list-tasks to show all tasks
