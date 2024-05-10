import requests
from io import BytesIO
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox


API_KEY=input("Enter Your API_Key :")
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
d = input("Enter date in YYYY-MM-DD format : ")

def fetch_data_from_api(date: datetime = d):
    try:
        dt = str(date)
        url_for_date = f"{API_URL}&date={dt}"
        response = requests.get(url_for_date)
        response.raise_for_status()
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def show_main_window():
    root = tk.Tk()
    
    root.title("NASA APOD Viewer")

    # Fetch data from NASA APOD API
    data = fetch_data_from_api()
    if data and data.get('url'):
        # Load background image from URL
        response = requests.get(data['url'])
        img = Image.open(BytesIO(response.content))
        img = img.resize((800, 600))  # Resize the image to fit the window
        img_tk = ImageTk.PhotoImage(img)

        # Create a canvas to display the image
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

        # Display title and explanation as labels overlaid on the image
        title = data.get('title', 'Title not available')
        explanation = data.get('explanation', 'Explanation not available')

        label_title = tk.Label(root, text=title, font=("Helvetica", 16, "bold"), bg='white', wraplength=700)
        label_title.place(relx=0.5, rely=0.05, anchor=tk.N, width=700)

        label_explanation = tk.Label(root, text=explanation, font=("Helvetica", 12), bg='white', justify=tk.LEFT, wraplength=700)
        label_explanation.place(relx=0.5, rely=0.1, anchor=tk.N, width=700)

    else:
        messagebox.showerror("Error", "Failed to fetch image and data from API")

    # Function to handle window closing
    def on_closing():
        root.destroy()

    # Bind the closing event to the window
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Run the tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    show_main_window()
