import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from pathlib import Path
import shutil
import threading


def run_organizer(selected_path,progress_bar):
    base_dir = Path(selected_path)
    files = [f for f in base_dir.iterdir() if f.is_file()]
    total_files = len(files)

    if total_files == 0:
        messagebox.showinfo("Done", "There are no files to organize.")
        return

    FILE_CATEGORIES = {".pdf": "Documents", ".txt": "Documents", ".jpg": "Images", ".png": "Images", ".zip": "Archives"}

    for index, file_path in enumerate(files):

        ext = file_path.suffix.lower()
        folder_name = FILE_CATEGORIES.get(ext, "Others")
        target_dir = base_dir / folder_name
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(target_dir / file_path.name))

        progress = ((index + 1) / total_files) * 100
        progress_bar['value'] = progress


    messagebox.showinfo("Success", "Files organized successfully!")

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        thread = threading.Thread(target=run_organizer, args=(folder_selected,progress_bar))
        thread.start()


root = tk.Tk()
root.title("File Organizer Pro")
root.geometry("400x150")

progress_bar = ttk.Progressbar(root, orient = "horizontal", mode = "determinate")
progress_bar.pack(pady=20)

btn = tk.Button(root, text="Select Folder & Organize", command=select_folder)
btn.pack()

root.mainloop()































