# YouTube Video Downloader  

This is a simple Python application with a graphical interface created using the tkinter library. It allows you to download YouTube videos using yt-dlp.  

## Features  

- Download videos by URL: Enter the YouTube video link and download it to your computer.  
- Use a cookies file (optional): If needed, specify a cookies file for video downloading.  
- Choose a save directory: Select where the video will be saved.  
- Simple and intuitive interface.  

## Requirements *(Not required for the ".exe" file)*  

- Python 3.x  
- Installed yt-dlp utility  
- tkinter library (included in the standard Python library)  

## Installation and Launch *(Not required for the ".exe" file)*  

1. Install yt-dlp if it is not already installed:  

pip install yt-dlp

2. Download or clone the application's code.  

3. Run the application:  

python "YouTube Video Downloader.py"

## Usage  

1. Enter the YouTube video link.  
2. *(Optional)* Specify a cookies file if necessary.  
3. Choose a directory to save the video.  
4. Click the "Download Video" button.  

## License  

This application is provided "as is" and is free to use.  

## Frequently Asked Questions  

What is `cookies.txt`?  

Answer: cookies.txt is needed if the video is age-restricted.  
This file can be downloaded independently using browser extensions that download cookies.txt.
The file is used by the program when accessing YouTube servers to verify age and gain access to the video.  
