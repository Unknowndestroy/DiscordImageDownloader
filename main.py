import requests
import os
import time

def download_images(channel_id, user_token, max_images):
    headers = {
        'Authorization': user_token
    }
    last_id = None
    images = []

    while len(images) < max_images:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"
        if last_id:
            url += f"&before={last_id}"
        
        response = requests.get(url, headers=headers)
        messages = response.json()
        
        if not messages:
            break

        last_id = messages[-1]['id']
        
        for msg in messages:
            for attachment in msg.get('attachments', []):
                if attachment.get('content_type', '').startswith('image/') and len(images) < max_images:
                    images.append(attachment['url'])
        
        print(f"{len(images)} images found...")
        time.sleep(1.5)

    os.makedirs("discord_images", exist_ok=True)
    print(f"Downloading a total of {len(images)} images...")

    for index, url in enumerate(images, 1):
        head_response = requests.head(url)
        if head_response.status_code == 200:
            response = requests.get(url)
            if response.status_code == 200:
                file_extension = url.split('.')[-1].split('?')[0]
                file_name = f"discord_images/discord_image_{index}.{file_extension}"
                with open(file_name, "wb") as file:
                    file.write(response.content)
        else:
            print(f"Image is invalid or inaccessible: {url}")
    
    print("Download completed.")

if __name__ == "__main__":
    channel_id = input("Enter the channel ID: ")
    user_token = input("Enter your user token: ")
    max_images = int(input("Enter the download limit: "))
    download_images(channel_id, user_token, max_images)
