import argparse
import sys
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_utils import load_data, save_data

def main():
    parser = argparse.ArgumentParser(description="TaskMateManager CLI Tool")
    subparsers = parser.add_subparsers(dest="command")
    
    # Add User
    add_user_parser = subparsers.add_parser("add-user", help="Add a user")
    add_user_parser.add_argument("--name", required=True, help="User name")
    add_user_parser.add_argument("--email", required=True, help="User email")
    
    # List Users
    list_users_parser = subparsers.add_parser("list-users", help="List all users")
    list_users_parser.add_argument("--id", type=int, help="Filter by user ID")
    
    # Add Project
    add_project_parser = subparsers.add_parser("add-project", help="Add a project")
    add_project_parser.add_argument("--title", required=True, help="Project title")
    add_project_parser.add_argument("--description", required=True, help="Project description")
    add_project_parser.add_argument("--due-date", required=True, help="Project due date")
    add_project_parser.add_argument("--user", type=int, nargs="+", required=True, help="User IDs assigned to project")

    # List Projects
    list_projects_parser = subparsers.add_parser("list-projects", help="List all projects or a specific one")
    list_projects_parser.add_argument("--id", type=int, help="Project ID to filter by")

    # Search Projects by user
    search_projects_parser = subparsers.add_parser("search-projects", help="Search projects by user ID")
    search_projects_parser.add_argument("--user", type=int, required=True, help="User ID to filter by")

    # Add Task
    add_task = subparsers.add_parser("add-task", help="Add a task")
    add_task.add_argument("--title", required=True, help="Task title")
    add_task.add_argument("--status", required=True, help="Task status")
    add_task.add_argument("--project", type=int, required=True, help="Project ID")
    add_task.add_argument("--user", type=int, required=True, help="User ID")
    
    # List Tasks
    subparsers.add_parser("list-tasks", help="List all tasks")

    # List projects sorted by due date
    subparsers.add_parser("list-due-date", help="List projects sorted by due date")

    # Complete Task
    complete_task = subparsers.add_parser("complete-task", help="Complete a task")
    complete_task.add_argument("--id", type=int, required=True, help="Task ID")
    
    args = parser.parse_args()
    
    # connect commands to persistence
    data = load_data()

    if args.command == "add-user":
        new_id = len(data["users"]) + 1
        user = {"id": new_id, "name": args.name, "email": args.email}
        data["users"].append(user)
        save_data(data)
        print(f"User '{args.name}' added successfully!")

    elif args.command == "list-users":
        if args.id:
            user = next((u for u in data["users"] if u["id"] == args.id), None)
            if user:
                print(f"{user['id']}: {user['name']} ({user['email']})")
            else:
                print(f"❌ User with ID {args.id} not found.")
        else:
            for u in data["users"]:
                print(f"{u['id']}: {u['name']} ({u['email']})")

    elif args.command == "add-project":
        new_id = len(data["projects"]) + 1
        project = {
            "id": new_id,
            "title": args.title,
            "description": args.description,
            "due_date": args.due_date,
            "users": args.user
        }
        data["projects"].append(project)
        save_data(data)
        print(f"Project '{args.title}' added successfully!")

    elif args.command == "list-projects":
        # Build a lookup dictionary for user IDs → names
        user_lookup = {u["id"]: u["name"] for u in data["users"]}

        if args.id:
            project = next((p for p in data["projects"] if p["id"] == args.id), None)
            if project:
                print(f"Project(id={project['id']}, title={project['title']}, due-date={project['due_date']})")
                print("Users assigned:")
                for uid in project["users"]:
                    print(f"- {uid}: {user_lookup.get(uid, 'Unknown')}")
            else:
                print(f"❌ Project with ID {args.id} not found.")
        else:
            for p in data["projects"]:
                print(f"Project(id={p['id']}, title={p['title']}, due-date={p['due_date']})")
                print("Users assigned:")
                for uid in p["users"]:
                    print(f"- {uid}: {user_lookup.get(uid, 'Unknown')}")
                print()  # blank line between projects

    elif args.command == "search-projects":
        projects = [p for p in data["projects"] if args.user in p["users"]]
        if projects:
            for p in projects:
                print(f"- {p['title']} (due: {p['due_date']})")
        else:
            print(f"No projects for user {args.user}")

    elif args.command == "add-task":
        new_id = len(data["tasks"]) + 1
        task = {
            "id": new_id,
            "title": args.title,
            "status": args.status,
            "project": args.project,
            "user": args.user
        }
        data["tasks"].append(task)
        save_data(data)
        print(f"Task '{args.title}' added successfully!")
        
    elif args.command == "list-tasks":
        # Build lookup dictionaries for user names and project titles
        user_lookup = {u["id"]: u["name"] for u in data["users"]}
        project_lookup = {p["id"]: p["title"] for p in data["projects"]}

        for t in data["tasks"]:
            print(f"Task(id={t['id']}, title={t['title']}, status={t['status']}, "
                  f"project={project_lookup.get(t['project'], 'Unknown')}, "
                  f"user={user_lookup.get(t['user'], 'Unknown')})")

    elif args.command == "list-due-date":
        sorted_projects = sorted(data["projects"], key=lambda p: p["due_date"])
        for p in sorted_projects:
            print(f"Project(id={p['id']}, title={p['title']}, due-date={p['due_date']})")

    elif args.command == "complete-task":
        for t in data["tasks"]:
            if t["id"] == args.id:
                t["status"] = "Done"
                save_data(data)
                print(f"Task {args.id} marked as complete!")
                break
        else:
            print(f"Task with ID {args.id} not found.")
    
    else:
        parser.print_help()


# Entry point 
if __name__ == "__main__":
    main()
