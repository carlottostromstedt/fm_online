import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Function to download and save image
def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

# URL of the webpage
url = "https://yugioh.fandom.com/wiki/Gallery_of_Yu-Gi-Oh!_Forbidden_Memories_cards"

# Fetch HTML content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find parent div element
    parent_div = soup.find('div', class_='mw-parser-output')
    
    # Create folder to save images
    folder_name = "yugioh_images"
    os.makedirs(folder_name, exist_ok=True)
    
    # Iterate through child div elements
    for div in parent_div.find_all('div'):
        # Find image URL
        image_url = div.find('a')['href']
        
        # Find accompanying text
        text = div.find('br').next_sibling.strip()
        
        # Extract filename from URL
        filename = os.path.join(folder_name, f"{text}.jpg")
        
        # Download and save image
        download_image(image_url, filename)
else:
    print("Failed to fetch webpage")
