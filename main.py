import os
import requests
from datetime import datetime

def fetch_apod(api_key, date=None):
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    
    if date:
        params["date"] = date
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def set_background(image_url):
    # Command to set the desktop background, might need modification based on your OS
    command = f"gsettings set org.gnome.desktop.background picture-uri {image_url}"
    os.system(command)

def main(api_key):
    today = datetime.now().strftime("%Y-%m-%d")
    apod_data = fetch_apod(api_key, today)
    
    if apod_data:
        image_url = apod_data.get("hdurl")
        set_background(image_url)
        print("Desktop background set successfully!")
    else:
        print("Failed to fetch APOD data")

if __name__ == "__main__":
    API_KEY = "YOUR_NASA_API_KEY"
    main(API_KEY)
