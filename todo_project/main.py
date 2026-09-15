"""
Simple To-Do List Application
A basic project to manage daily tasks
"""

from task_manager import TaskManager


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("       TO-DO LIST APPLICATION")
    print("="*40)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("="*40)


def main():
    """Main application loop"""
    task_manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            task_manager.add_task(title, description)
            
        elif choice == "2":
            task_manager.view_tasks()
            
        elif choice == "3":
            task_manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_complete(task_id)
            except ValueError:
                print("Invalid ID! Please enter a number.")
                
        elif choice == "4":
            task_manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid ID! Please enter a number.")
                
        elif choice == "5":
            print("\nThank you for using To-Do List! Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
