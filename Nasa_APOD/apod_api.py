'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''

def main():
    # TODO: Add code to test the functions in this module
    return

import requests
import image_lib
from datetime import datetime

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date or str): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    if isinstance(apod_date, str):
        apod_date = datetime.strptime(apod_date, "%Y-%m-%d")

    params = {
        "date": apod_date.strftime("%Y-%m-%d"),
        "thumbs": True
    }

    url = "https://api.nasa.gov/planetary/apod?api_key=OQYV0KWCqZXwadM2xYBodjpky8fEp0ImwNQyDaDD"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get APOD info. Status code:", response.status_code)
        return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    media_type = apod_info_dict.get("media_type")

    if media_type == "image":
        image_url = apod_info_dict.get("hdurl")
    elif media_type == "video":
        image_url = apod_info_dict.get("thumbnail_url")
    else:
        print("Invalid media type:", media_type)
        return None

    return image_url

if __name__ == '__main__':
    main()