import argparse
import os

def main():
    manager = TaskMateManager()
    parser = argparse.ArgumentParser(description="TaskMate CLI")
    subparsers = parser.add_subparsers(dest='command')
    
    #Add User.
    add_user = subparsers.add_parser("add_user", help="Add a user")
    add_user.add_argument("--name", required=True, help="User name")
    add_user.add_argument("--email", required=True, help="User email")
    
    #List Users.
    list_users = subparsers.add_parser("list_users", help="List all users")
    
    #Add Project.
    add_project = subparsers.add_parser("add_project", help="Add a project")
    add_project.add_argument("--title", required=True, help="Project title")
    add_project.add_argument("--description", required=True, help="Project description")
    
    #Add Task.
    add_task = subparsers.add_parser("add_task", help="Add a task")
    add_task.add_argument("--title", required=True, help="Task title")
    add_task.add_argument("--project-id", type=int, required=True, help="Project ID")
    add_task.add_argument("--user", type=int, required=True, help="User ID")
    
    #Finish Task.
    finish_task = subparsers.add_parser("finish_task", help="finish a task")
    finish_task.add_argument("--task-id", type=int, required=True, help="Task ID")
    
    args = parser.parse_args()
    
    if args.command == "add_user":
        manager.add_user(args.name, args.email)
    elif args.command == "list_users":
        manager.list_users()
    elif args.command == "add_project":
        manager.add_project(args.title, args.description, args.user)
    elif args.command == "add_task":
        manager.add_task(args.title, args.project_id, args.user)
    elif args.command == "finish_task":
        manager.finish_task(args.task_id)
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()