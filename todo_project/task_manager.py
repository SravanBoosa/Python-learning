"""
Task Manager Module
Handles all task-related operations
"""

from datetime import datetime


class Task:
    """Represents a single task"""
    
    task_counter = 1
    
    def __init__(self, title, description=""):
        self.id = Task.task_counter
        Task.task_counter += 1
        self.title = title
        self.description = description
        self.completed = False
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_complete(self):
        """Mark task as complete"""
        self.completed = True
    
    def __str__(self):
        status = "✓ COMPLETED" if self.completed else "○ PENDING"
        return f"[{self.id}] {self.title} - {status}\n    Description: {self.description}\n    Created: {self.created_date}"


class TaskManager:
    """Manages a collection of tasks"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description=""):
        """Add a new task"""
        if not title:
            print("Task title cannot be empty!")
            return
        
        task = Task(title, description)
        self.tasks.append(task)
        print(f"\n✓ Task '{title}' added successfully!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\n📋 No tasks yet. Add one to get started!")
            return
        
        print("\n📋 YOUR TASKS:")
        print("-" * 50)
        for task in self.tasks:
            print(task)
            print()
    
    def mark_complete(self, task_id):
        """Mark a task as complete"""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"\n✓ Task '{task.title}' marked as complete!")
                return
        print(f"\n✗ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"\n✓ Task '{task.title}' deleted successfully!")
                return
        print(f"\n✗ Task with ID {task_id} not found!")
    
    def get_completed_count(self):
        """Return count of completed tasks"""
        return sum(1 for task in self.tasks if task.completed)
    
    def get_total_count(self):
        """Return total count of tasks"""
        return len(self.tasks)
