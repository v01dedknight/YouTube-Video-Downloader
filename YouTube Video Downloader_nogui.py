import subprocess

def download_video_with_cookies(url, save_path, cookies_path=None):
    try:
        # Forming a team for yt-dlp
        command = [
            "yt-dlp",
            "-o", f"{save_path}/%(title)s.%(ext)s",
            url
        ]

        # If the path to cookies is specified, add it to the command
        if cookies_path:
            command.insert(1, "--cookies")
            command.insert(2, cookies_path)

        # Start the download with yt-dlp
        subprocess.run(command, check=True)
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video link: ")
    cookies_file = input("Enter the path to the file cookies (For example, cookies.txt), leave blank if not needed: ")
    save_directory = input("Enter the path to save (default current folder): ") or "."
    
    # Pass None if cookies_file is empty
    download_video_with_cookies(video_url, save_directory, cookies_file or None)
