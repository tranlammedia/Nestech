import tkinter as tk

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # Create a listbox to display the to-do items
        self.listbox = tk.Listbox(master, height=10, width=50)
        self.listbox.pack()

        # Create an entry widget to input new to-do items
        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        # Create a button to add new to-do items
        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.pack()

        # Create a button to delete selected to-do items
        self.delete_button = tk.Button(master, text="Delete Item", command=self.delete_item)
        self.delete_button.pack()

        # Create a button to clear all to-do items
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_items)
        self.clear_button.pack()

    def add_item(self):
        # Get the text entered in the entry widget
        item = self.entry.get()
        if item:
            # Add the item to the listbox
            self.listbox.insert(tk.END, item)
            # Clear the entry widget
            self.entry.delete(0, tk.END)

    def delete_item(self):
        # Get the index of the selected item
        selection = self.listbox.curselection()
        if selection:
            # Delete the selected item from the listbox
            self.listbox.delete(selection)

    def clear_items(self):
        # Delete all items from the listbox
        self.listbox.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()
