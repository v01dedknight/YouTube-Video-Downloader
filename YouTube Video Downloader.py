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
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error has occurred: {e}")

def select_cookies_file(entry):
    filepath = filedialog.askopenfilename(title="Select file cookies", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def select_save_directory(entry):
    directory = filedialog.askdirectory(title="Select a folder to save")
    entry.delete(0, tk.END)
    entry.insert(0, directory)

def start_download():
    url = url_entry.get()
    save_path = save_path_entry.get() or "."
    cookies_path = cookies_entry.get() or None

    if not url:
        messagebox.showwarning("Attention", "Please enter video link.")
        return

    download_video_with_cookies(url, save_path, cookies_path)

# Main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Widgets
tk.Label(root, text="Video link YouTube:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="File cookies (optional):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
cookies_entry = tk.Entry(root, width=50)
cookies_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Choose...", command=lambda: select_cookies_file(cookies_entry)).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Path to save:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
save_path_entry = tk.Entry(root, width=50)
save_path_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Choose...", command=lambda: select_save_directory(save_path_entry)).grid(row=2, column=2, padx=5, pady=5)

tk.Button(root, text="Download video", command=start_download).grid(row=3, column=0, columnspan=3, pady=10)

# Starting the main loop
root.mainloop()