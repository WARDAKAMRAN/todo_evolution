"""CLI menu interface for the Todo application."""

from typing import Optional
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from ..services.todo_service import TodoService
from ..models.todo_task import TodoTask
from ..core.exceptions import TaskNotFoundError, EmptyTitleError


console = Console()


class TodoMenu:
    """Provides the CLI menu interface for interacting with TodoService."""

    def __init__(self, service: TodoService):
        """Initialize the menu with a TodoService instance."""
        self.service = service

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\nTodo CLI Application")
        print("====================")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Completion")
        print("6. Exit")
        print()

    def get_user_choice(self) -> int:
        """Get and validate user menu choice."""
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
                return self.get_user_choice()
        except ValueError:
            print("Please enter a valid number.")
            return self.get_user_choice()

    def add_task(self) -> None:
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional): ")

        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except EmptyTitleError as e:
            print(f"Error: {e}")

    def list_tasks(self) -> None:
        """Handle listing all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.service.list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Create a rich table with enhanced formatting
        table = Table(title="Todo Tasks", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Status", min_width=8)
        table.add_column("Title", min_width=15)
        table.add_column("Description", min_width=20)

        for task in tasks:
            status = "[green]Done[/green]" if task.completed else "[red]Todo[/red]"
            description = task.description if task.description else "[italic](none)[/italic]"
            table.add_row(
                str(task.id),
                status,
                task.title,
                description
            )

        console.print(table)

    def update_task(self) -> None:
        """Handle updating an existing task."""
        print("\n--- Update Task ---")

        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        # Check if task exists
        try:
            current_task = self.service.get_task(task_id)
        except TaskNotFoundError:
            print(f"Error: Task with ID {task_id} does not exist.")
            return

        print(f"Current title: {current_task.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()

        print(f"Current description: {current_task.description}")
        new_description = input("Enter new description (or press Enter to keep current): ")

        # Prepare update parameters
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description != "" else None

        try:
            updated_task = self.service.update_task(
                task_id,
                title=title_to_update,
                description=description_to_update
            )
            print(f"Task {updated_task.id} updated successfully!")
        except EmptyTitleError as e:
            print(f"Error: {e}")

    def delete_task(self) -> None:
        """Handle deleting a task."""
        print("\n--- Delete Task ---")

        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        success = self.service.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def toggle_completion(self) -> None:
        """Handle toggling task completion status."""
        print("\n--- Toggle Task Completion ---")

        try:
            task_id = int(input("Enter task ID to toggle: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        try:
            updated_task = self.service.toggle_completion(task_id)
            status = "completed" if updated_task.completed else "incomplete"
            print(f"Task {updated_task.id} is now {status}.")
        except TaskNotFoundError:
            print(f"Error: Task with ID {task_id} does not exist.")

    def run(self) -> None:
        """Run the main application loop."""
        print("Welcome to the Todo CLI Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.list_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.toggle_completion()
            elif choice == 6:
                print("Thank you for using Todo CLI. Goodbye!")
                break

            # Pause to let user see results before showing menu again
            input("\nPress Enter to continue...")