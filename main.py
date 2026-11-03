import tkinter as tk
from tkinter import messagebox, ttk
from Ben_10Gui import ben10_data

def search_item(category, entry):
    name = entry.get()
    items = ben10_data[category]
    if name in items:
        info = items[name]
        result = "\n".join([f"{k}: {v}" if not isinstance(v, list) else f"{k}: {', '.join(v)}" for k, v in info.items()])
        messagebox.showinfo(name, result)
    else:
        messagebox.showerror("Not Found", f"{category[:-1]} not found.")

root = tk.Tk()
root.title("Ben 10 Encyclopedia")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Aliens Tab
alien_tab = tk.Frame(notebook)
notebook.add(alien_tab, text="Aliens")

alien_label = tk.Label(alien_tab, text="Enter Alien Name:")
alien_label.pack()
alien_entry = tk.Entry(alien_tab)
alien_entry.pack()
alien_button = tk.Button(alien_tab, text="Search Alien", command=lambda: search_item("Aliens", alien_entry))
alien_button.pack()

# Characters Tab
char_tab = tk.Frame(notebook)
notebook.add(char_tab, text="Characters")

char_label = tk.Label(char_tab, text="Enter Character Name:")
char_label.pack()
char_entry = tk.Entry(char_tab)
char_entry.pack()
char_button = tk.Button(char_tab, text="Search Character", command=lambda: search_item("Characters", char_entry))
char_button.pack()

# Gadgets Tab
gadget_tab = tk.Frame(notebook)
notebook.add(gadget_tab, text="Gadgets")

gadget_label = tk.Label(gadget_tab, text="Enter Gadget Name:")
gadget_label.pack()
gadget_entry = tk.Entry(gadget_tab)
gadget_entry.pack()
gadget_button = tk.Button(gadget_tab, text="Search Gadget", command=lambda: search_item("Gadgets", gadget_entry))
gadget_button.pack()

root.mainloop()

