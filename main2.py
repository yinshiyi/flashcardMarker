import tkinter as tk
from PIL import ImageTk, Image
import random
import os
import datetime

# Function to check if the user's input matches the metadata
def check_input():
    user_input = entry.get().strip().lower()  # Get user's input from the entry widget
    
    # Get the metadata associated with the image
    metadata = image_metadata[current_image]
    
    # Check if the input matches the metadata
    if user_input == metadata:
        result_label.config(text="Correct")
        log_result(current_image, True)
    else:
        result_label.config(text="Incorrect")
        log_result(current_image, False)

    # Show the next image or end the program if all images have been shown
    if len(images_shown) == len(images):
        window.quit()
    else:
        show_next_image()

# Function to show the next image
def show_next_image():
    global current_image
    
    # Select the next image that hasn't been shown yet
    for image in images:
        if image not in images_shown:
            current_image = image
            break
    
    # Load and display the image
    image_path = os.path.join(image_folder, current_image)
    image = Image.open(image_path)
    image = image.resize((300, 200))  # Resize the image to fit the window
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Add the image to the list of shown images
    images_shown.append(current_image)

# Function to log the result in a log file
def log_result(image, is_correct):
    log_file = "log.txt"  # Path to the log file
    
    # Create a log entry with the current timestamp and the image filename
    log_entry = f"{datetime.datetime.now()}: {image} - {'Correct' if is_correct else 'Incorrect'}\n"
    
    # Append the log entry to the log file
    with open(log_file, "a") as file:
        file.write(log_entry)

# Set up the main window
window = tk.Tk()
window.title("Image Verification Program")
window.geometry("400x300")

# Set up the image folder and image list
image_folder = "C:/Users/12130/Pictures/Screenshots"  # Replace with the actual path to your image folder
images = os.listdir(image_folder)
random.shuffle(images)  # Shuffle the list of images

# Set up the image metadata
image_metadata = {
    "image1.jpg": "metadata1",
    "image2.jpg": "metadata2",
    # Add more image metadata entries as needed
}

# Create the image label
image_label = tk.Label(window)
image_label.pack()

# Create the text box and submit button
entry = tk.Entry(window)
entry.pack()
submit_button = tk.Button(window, text="Submit", command=check_input)
submit_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Initialize the list of shown images
images_shown = []

# Show the first image
current_image = None
show_next_image()

# Run the main window loop
window.mainloop()
