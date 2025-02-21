# YouTube Video Downloader (nogui Version)

This is a simple command-line application written in Python. It allows you to download YouTube videos using yt-dlp, with optional support for cookies files to handle age-restricted content.

## Features

- Download Videos by URL: Just provide the YouTube link and save the video to your computer.  
- Optional Cookies File: Specify a cookies.txt file if needed, for example, for age-restricted videos.  
- Custom Save Directory: Choose where the video will be saved or use the current folder by default.  
- Lightweight and Fast: No graphical interface, just a quick and efficient download process.

## Requirements

- Python 3.x  
- yt-dlp utility  

### Installation

1. Install `yt-dlp` if it is not already installed:  

pip install yt-dlp

2. Clone or download this repository.

## Usage

1. Run the script:  

python "YouTube Video Downloader_nogui.py"

2. Follow the prompts:  

- Enter the YouTube video link.  
- *(Optional)* Specify the path to the cookies.txt file if needed, or just press Enter to skip.  
- Specify the save directory or press Enter to use the current folder.  

## Frequently Asked Questions

### What is `cookies.txt` and why do I need it?  

cookies.txt is needed if the video is age-restricted or requires authentication.  
You can generate this file using a browser extension like cookies.txt exporter or similar tools.  
The file helps the application access YouTube servers with your authenticated session, allowing it to bypass restrictions.

## License

This application is provided "as is" and is free to use.  
The developer is not responsible for the use of this software for unlawful purposes.  
