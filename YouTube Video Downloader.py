import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def download_video_with_cookies(url, save_path, cookies_path=None):
    try:
        # We are forming a team for yt-dlp
        command = [
            "yt-dlp",
            "-o", f"{save_path}/%(title)s.%(ext)s",
            url
        ]

        # If the path to cookies is specified, add it to the command
        if cookies_path:
            command.insert(1, "--cookies")
            command.insert(2, cookies_path)

        # We start the download with yt-dlp
        subprocess.run(command, check=True)
        messagebox.showinfo("Успешно", "Видео успешно установлено!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def select_cookies_file(entry):
    filepath = filedialog.askopenfilename(title="Выберите файл cookies", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def select_save_directory(entry):
    directory = filedialog.askdirectory(title="Выберите папку для сохранения")
    entry.delete(0, tk.END)
    entry.insert(0, directory)

def start_download():
    url = url_entry.get()
    save_path = save_path_entry.get() or "."
    cookies_path = cookies_entry.get() or None

    if not url:
        messagebox.showwarning("Внимание", "Пожалуйста, вставьте ссылку на видео.")
        return

    download_video_with_cookies(url, save_path, cookies_path)

# Main window
root = tk.Tk()
root.title("YouTube Video Downloader v1.1")

# Widgets
tk.Label(root, text="Ссылка на YouTube видео:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Файл cookies (опционально):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
cookies_entry = tk.Entry(root, width=50)
cookies_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Выбрать...", command=lambda: select_cookies_file(cookies_entry)).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Папка для сохранения:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
save_path_entry = tk.Entry(root, width=50)
save_path_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Выбрать...", command=lambda: select_save_directory(save_path_entry)).grid(row=2, column=2, padx=5, pady=5)

tk.Button(root, text="Скачать видео", command=start_download).grid(row=3, column=0, columnspan=3, pady=10)

# Starting the main loop
root.mainloop()
