import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Create main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Frame for task entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

# Entry widget to add tasks
task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)

# Button to add tasks
add_button = tk.Button(entry_frame, text="Add Task", command=add_task, bg="green", fg="white")
add_button.pack(side=tk.LEFT)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Frame for action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button to delete selected task
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.pack(side=tk.LEFT, padx=10)

# Button to clear all tasks
clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, bg="blue", fg="white")
clear_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
