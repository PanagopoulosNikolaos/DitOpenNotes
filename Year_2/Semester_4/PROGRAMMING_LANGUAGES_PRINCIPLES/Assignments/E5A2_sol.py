import csv
import tkinter as tk
from tkinter import messagebox, ttk


class ContactManager:
    """
    Manages a list of contacts with full CRUD and persistence features in a GUI.

    Provides a graphical interface to add, view, update, delete, and restore deleted
    contacts, saving the state to a CSV file.
    - __init__: Initializes the contact list and sets up the application.
    - createWidgets: Builds the GUI components.
    - loadContacts: Reads contact list from a CSV file.
    - saveContacts: Writes the contact list to a CSV file.
    - addContact: Initiates addition of a new contact.
    - editContact: Initiates editing of a selected contact.
    - createDialog: Opens a form for creating/updating a contact.
    - displayContacts: Refreshes the tree view display.
    - deleteContact: Moves a contact to deleted list and updates tree view.
    - showRetrieveDialog: Opens dialog to restore deleted contacts.
    """

    def __init__(self, root: tk.Tk):
        """
        Initializes the ContactManager.

        Args:
            root (tk.Tk): The root Tkinter window object.
        """
        self.root = root
        self.root.title("Διαχείριση Επαφών")
        # Load the contacts from CSV during initialization.
        self.contacts = self.loadContacts()
        self.deleted_contacts = []
        self.createWidgets()
        # Centers the window on the screen.
        self.root.eval("tk::PlaceWindow . center")

    def createWidgets(self) -> None:
        """
        Builds and packs the GUI components of the application.
        """
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Configures the tree view displaying contacts.
        self.tree = ttk.Treeview(
            tree_frame, columns=("lastname", "firstname", "phone"), show="headings"
        )
        self.tree.heading("lastname", text="Επώνυμο")
        self.tree.heading("firstname", text="Όνομα")
        self.tree.heading("phone", text="Τηλέφωνο")
        self.tree.column("lastname", width=120)
        self.tree.column("firstname", width=120)
        self.tree.column("phone", width=120)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            tree_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Connects the scrollbar to scroll vertically through the tree view.
        self.tree.configure(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Creates control buttons for contact actions.
        tk.Button(btn_frame, text="Προσθήκη Επαφής", command=self.addContact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(btn_frame, text="Επεξεργασία Επαφής", command=self.editContact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(btn_frame, text="Διαγραφή Επαφής", command=self.deleteContact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(
            btn_frame, text="Ανάκτηση Επαφής", command=self.showRetrieveDialog
        ).pack(side=tk.TOP, fill=tk.X)
        tk.Button(btn_frame, text="Αποθήκευση Επαφών", command=self.saveContacts).pack(
            side=tk.TOP, fill=tk.X
        )

        # Performs initial population of the contacts.
        self.displayContacts()

    def loadContacts(self) -> list:
        """
        Loads and sorts contact details from contacts.csv.

        Returns:
            list: A list of contact tuples sorted alphabetically.
        """
        try:
            with open("contacts.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                return sorted(
                    [tuple(contact) for contact in reader], key=lambda x: x[0].lower()
                )
        except FileNotFoundError:
            return []

    def saveContacts(self) -> None:
        """
        Saves current contacts alphabetically to contacts.csv.
        """
        with open("contacts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for contact in sorted(self.contacts, key=lambda x: x[0].lower()):
                writer.writerow(contact)
        messagebox.showinfo("Επιτυχία!", "Οι επαφές αποθηκεύτηκαν στο αρχείο.")

    def addContact(self) -> None:
        """
        Triggers dialog opening for creating a new contact.
        """
        self.createDialog("Νέα Επαφή")

    def editContact(self) -> None:
        """
        Triggers dialog opening for editing a selected contact.
        """
        try:
            selected_item = self.tree.selection()[0]
            contact = self.tree.item(selected_item, "values")
            self.createDialog("Επεξεργασία Επαφής", contact)
        except IndexError:
            messagebox.showerror("Σφάλμα!", "Δεν έχει επιλεγεί καμία επαφή")

    def createDialog(self, title: str, contact: tuple = None) -> None:
        """
        Creates and positions a dialog window for contact details.

        Args:
            title (str): Title of the popup window.
            contact (tuple): Target contact tuple to edit, or None.
        """
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry(
            "+{}+{}".format(self.root.winfo_x() + 50, self.root.winfo_y() + 50)
        )
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.focus_set()

        tk.Label(dialog, text="Επώνυμο:").pack()
        last_name_entry = tk.Entry(dialog)
        last_name_entry.pack(fill=tk.X)
        last_name_entry.insert(0, contact[0] if contact else "")

        tk.Label(dialog, text="Όνομα:").pack()
        first_name_entry = tk.Entry(dialog)
        first_name_entry.pack(fill=tk.X)
        first_name_entry.insert(0, contact[1] if contact else "")

        tk.Label(dialog, text="Τηλέφωνο:").pack()
        phone_number_entry = tk.Entry(dialog)
        phone_number_entry.pack(fill=tk.X)
        phone_number_entry.insert(0, contact[2] if contact else "")

        def saveContact() -> None:
            """
            Validates and saves the input values into contact list.
            """
            last_name = last_name_entry.get()
            first_name = first_name_entry.get()
            phone_number = phone_number_entry.get()
            if last_name and first_name and phone_number:
                new_contact = (last_name, first_name, phone_number)
                if contact:
                    idx = self.contacts.index(contact)
                    self.contacts[idx] = new_contact
                else:
                    self.contacts.append(new_contact)
                self.displayContacts()
                dialog.destroy()
            else:
                messagebox.showerror(
                    "Σφάλμα!",
                    "Παρακαλώ εισάγετε όλες τις λεπτομέρειες της επαφής",
                    parent=dialog,
                )

        tk.Button(dialog, text="Αποθήκευση", command=saveContact).pack()

    def displayContacts(self) -> None:
        """
        Refreshes treeview content with alphabetically sorted contacts list.
        """
        self.tree.delete(*self.tree.get_children())
        for contact in sorted(self.contacts, key=lambda x: x[0].lower()):
            self.tree.insert("", tk.END, values=contact)

    def deleteContact(self) -> None:
        """
        Deletes the selected contact, storing it in deleted contacts history.
        """
        try:
            selected_item = self.tree.selection()[0]
            contact = self.tree.item(selected_item, "values")
            self.deleted_contacts.append(contact)
            self.contacts.remove(contact)
            self.tree.delete(selected_item)
        except IndexError:
            messagebox.showerror("Σφάλμα!", "Δεν έχει επιλεγεί καμία επαφή")

    def showRetrieveDialog(self) -> None:
        """
        Displays dialog allowing recovery of recently deleted contacts.
        """
        if not self.deleted_contacts:
            messagebox.showinfo(
                "Πληροφορία", "Δεν υπάρχουν διαγραμμένες επαφές για ανάκτηση."
            )
            return

        retrieve_window = tk.Toplevel(self.root)
        retrieve_window.title("Ανάκτηση Επαφής")
        retrieve_window.geometry("300x300+450+450")

        list_frame = tk.Frame(retrieve_window)
        list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(list_frame)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.configure(yscrollcommand=scrollbar.set)

        for idx, contact in enumerate(self.deleted_contacts):
            listbox.insert(tk.END, f"{idx+1}. {contact[0]} {contact[1]} - {contact[2]}")

        def retrieveSelectedContact() -> None:
            """
            Restores the selected contact from the deleted history.
            """
            selected_idx = listbox.curselection()
            if selected_idx:
                selected_contact = self.deleted_contacts.pop(selected_idx[0])
                self.contacts.append(selected_contact)
                self.displayContacts()
                retrieve_window.destroy()
            else:
                messagebox.showerror("Προσοχή!", "Δεν έχετε επιλέξει καμία επαφή")

        retrieve_button = tk.Button(
            retrieve_window,
            text="Ανάκτηση Επιλεγμένης Επαφής",
            command=retrieveSelectedContact,
        )
        retrieve_button.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == "__main__":
    root_window = tk.Tk()
    app = ContactManager(root_window)
    root_window.mainloop()
