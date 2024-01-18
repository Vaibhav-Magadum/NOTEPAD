import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

def copy_text():
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def cut_text():
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        root.clipboard_clear()
        root.clipboard_append(selected_text)
        text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

def paste_text():
    selected_text = root.clipboard_get()
    text_area.insert(tk.INSERT, selected_text)


root = tk.Tk()
root.title("Notepad")

text_area = tk.Text(root)
text_area.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_bar = tk.Menu(root)
edit_bar.add_command(label="Cut", command=cut_text)
edit_bar.add_command(label="Copy", command=copy_text)
edit_bar.add_command(label="Paste", command=paste_text)  # Add the command for Paste
menu_bar.add_cascade(label="Edit", menu=edit_bar)

root.config(menu=menu_bar)
root.mainloop()

