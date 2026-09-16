import os
import customtkinter as ctk
from tkinter import messagebox


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My To-Do List")
        self.geometry("500x600")

        self.todo = ToDoList()

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="TO-DO LIST",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=20)

        # Entry
        self.task_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter a task...",
            width=350
        )
        self.task_entry.pack(pady=10)

        # Add button
        self.add_button = ctk.CTkButton(
            self,
            text="Add Task",
            command=self.add_task
        )
        self.add_button.pack(pady=10)

        # Task frame
        self.task_frame = ctk.CTkScrollableFrame(
            self,
            width=400,
            height=400
        )
        self.task_frame.pack(pady=20)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()

        if task:
            self.todo.add_task(task)
            self.task_entry.delete(0, "end")
            self.refresh_tasks()
        else:
            messagebox.showwarning(
                "Empty Task",
                "Please enter a task."
            )

    def complete_task(self, index):
        self.todo.complete_task(index)
        self.refresh_tasks()

    def delete_task(self, index):
        self.todo.delete_task(index)
        self.refresh_tasks()

    def refresh_tasks(self):

        # Remove old widgets
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Create task widgets
        for i, task in enumerate(self.todo.tasks):

            frame = ctk.CTkFrame(self.task_frame)
            frame.pack(fill="x", pady=5, padx=5)

            status = "✓" if task["done"] else "○"

            label = ctk.CTkLabel(
                frame,
                text=f"{status} {task['task']}",
                anchor="w"
            )
            label.pack(
                side="left",
                padx=10,
                pady=10,
                expand=True,
                fill="x"
            )

            if not task["done"]:
                done_button = ctk.CTkButton(
                    frame,
                    text="Done",
                    width=60,
                    command=lambda i=i: self.complete_task(i)
                )
                done_button.pack(side="right", padx=5)

            delete_button = ctk.CTkButton(
                frame,
                text="Delete",
                width=60,
                command=lambda i=i: self.delete_task(i)
            )
            delete_button.pack(side="right", padx=5)


app = App()
app.mainloop()
    
def view_tasks(self):
        if not self.tasks:
            print("NO TASKS YETT!!!")
            return
        