from tkinter import *
import apod_desktop
import image_lib
import apod_api

# Initialize the image cache
apod_desktop.init_apod_cache()

# Create the GUI
root = Tk()
root.geometry('600x400')

# Get the APOD image URL
apod_info = apod_api.get_apod_info("2024-04-16")
if apod_info is not None:
    image_url = apod_api.get_apod_image_url(apod_info)
    if image_url is not None:
        # Download the image
        image_data = image_lib.download_image(image_url)
        if image_data is not None:
            # Save the image to disk
            image_path = "apod.jpg"
            image_lib.save_image_file(image_data, image_path)

            # Set the image as the desktop background
            image_lib.set_desktop_background_image(r"C:\Users\Yash\OneDrive\Desktop\canada\Final Project Script Templates\apod.jpg")

            # Display the image in the GUI
            # image = PhotoImage(file=image_path)
            # label = Label(root, image=image)
            # label.pack()

root.mainloop()