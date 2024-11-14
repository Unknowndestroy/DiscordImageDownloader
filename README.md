# Discord Image Downloader 📷

An advanced script for downloading images from a Discord channel. This Python-based solution is **Termux-compatible** and **requires root access**, making it a powerful tool for quick and efficient image downloads directly from your mobile or computer.

## Features ✨

- **Effortless Image Download**: Automatically collects and downloads images from any specified Discord channel.
- **Customizable Limits**: Specify the maximum number of images you’d like to download.
- **Root Access Required**: Ensures full compatibility and access for Termux users with root privileges.
- **Error Handling**: Skips and logs any inaccessible or invalid image URLs.

## Requirements 📦

Ensure you have the following before you start:

- **Python 3.x**: Install Python in Termux or your preferred environment.
- **Requests Library**: Install with the following command:   ```pip install requests    ``` 
- ** Root Access**: Necessary to enable full functionality on Termux.
- ** Python Requests Package**

# Installation & Usage 🚀

## Windows
 ```pip install requests``` 
and just run the file. 

 ## Termux: 

- **Clone the Repository:**
 ```
git clone https://github.com/YourUsername/discord-image-downloader.git
cd discord-image-downloader
 ```

- **Run the Script:**
    Start the script with:
     ```python main.py```
          When prompted, enter your Discord Channel ID, User Token, and the Download Limit.  

## Example 📖
 ```python main.py ```
 ```Enter the channel ID: 123456789012345678 ```
 ```Enter your user token: YOUR_USER_TOKEN ```
 ```Enter the download limit: 100 ``` 

The script will then start downloading images and save them to a folder named discord_images in your current directory.

# Compatibility 🛠
- **Operating Systems**: Works on Windows, MacOS, Linux, and Termux (Android).
- **Termux**: Fully compatible but requires root access.

# Important Notes ⚠️
- This script requires **your user token** to access the Discord API. Ensure you keep it secure and avoid sharing it publicly.
- Respect Discord’s rate limits by allowing time between requests. The script includes a small delay to avoid rate limiting.

# *Disclaimer* 📜

*Use this script responsibly and respect Discord’s terms of service. This project is for personal use only and should not be used for any activity that violates Discord's guidelines.*
