import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning


def runExercise() -> None:
    """
    Runs the to-do list GUI application.
    """

    def addTask() -> None:
        """
        Adds a task to the listbox if it is not empty or a duplicate.
        """
        task = entry_task.get()
        if task == "":
            showwarning(title="Σφάλμα!", message="Θα πρέπει να εισάγετε μια εργασία")
        elif task in tasks.get():
            showwarning(title="Σφάλμα!", message="H εργασία ήδη υπάρχει στη λίστα")
        else:
            listbox_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)

    def deleteTask() -> None:
        """
        Deletes the selected task from the listbox.
        """
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except IndexError:
            showwarning(title="Σφάλμα!", message="Θα πρέπει να επιλέξετε μια εργασία")

    # Creates the main window.
    root = tk.Tk()
    root.title("Λίστα εργασιών")
    tasks = tk.Variable(value=[])

    # Creates a frame container for the listbox and scrollbar.
    frame_tasks = ttk.Frame(root)
    frame_tasks.pack()

    # Initializes the listbox displaying the tasks.
    listbox_tasks = tk.Listbox(
        frame_tasks, height=10, width=50, listvariable=tasks
    )
    listbox_tasks.pack(side=tk.LEFT)

    # Configures the scrollbar to navigate the listbox.
    scrollbar_tasks = ttk.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    # Creates the entry field for new tasks.
    entry_task = ttk.Entry(root)
    entry_task.pack(fill="x", expand=True)

    # Places the button to trigger task addition.
    button_add_task = ttk.Button(root, text="Νέα εργασία", command=addTask)
    button_add_task.pack(fill="x", expand=True)

    # Places the button to trigger task deletion.
    button_delete_task = ttk.Button(root, text="Διαγραφή εργασίας", command=deleteTask)
    button_delete_task.pack(fill="x", expand=True)

    # Centers the window on the screen and begins the event loop.
    root.eval("tk::PlaceWindow . center")
    root.mainloop()


if __name__ == "__main__":
    runExercise()
