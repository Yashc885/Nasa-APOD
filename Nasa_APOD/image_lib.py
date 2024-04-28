'''
Library of useful functions for working with images.
'''
def main():
    # TODO: Add code to test the functions in this module
    # download_image("https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcQRt_0WRr8Mc016RGaTK8eaiv6dSHKuNjIwdUrnF_7Xa_GdQL9YX9f4le5qucuyVUpKxbo7gqIGC0pZo14")
    # set_desktop_background_image(r"C:\Users\Yash\OneDrive\Desktop\canada\Final Project Script Templates\chapri.webp")
    return

import requests
import ctypes


def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if successful. None, if unsuccessful.
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to download image. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None


def save_image_file(image_data, image_path):
    """Saves image data as a file on disk.

    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str): Path to save image file

    Returns:
        bool: True, if succcessful. False, if unsuccessful
    """
    try:
        with open(image_path, 'wb') as f:
            f.write(image_data)
        return True
    except Exception as e:
        print(f"Error saving image file: {e}")
        return False

def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image on Windows.

    Args:
        image_path (str): Path of image file

    Returns:
        bool: True, if successful. False, if unsuccessful.
    """
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False

def scale_image(image_size, max_size=(800, 600)):
    """Calculates the dimensions of an image scaled to a maximum width
    and/or height while maintaining the aspect ratio  

    Args:
        image_size (tuple[int, int]): Original image size in pixels (width, height) 
        max_size (tuple[int, int], optional): Maximum image size in pixels (width, height). Defaults to (800, 600).

    Returns:
        tuple[int, int]: Scaled image size in pixels (width, height)
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    # NOTE: This function is only needed to support the APOD viewer GUI
    resize_ratio = min(max_size[0] / image_size[0], max_size[1] / image_size[1])
    new_size = (int(image_size[0] * resize_ratio), int(image_size[1] * resize_ratio))
    return new_size

if __name__ == '__main__':
    main()
    