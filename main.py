import tkinter as tk
from PIL import ImageTk, Image

# Function to check if the user's input is correct
def check_input():
    user_input = entry.get().strip().lower()  # Get user's input from the entry widget
    
    # Check if the input is correct
    if user_input == "correct":
        result_label.config(text="Correct")
    else:
        result_label.config(text="Error! The correct input is 'correct'.")

# Create the main window
window = tk.Tk()
window.title("Fellowship Program")
window.geometry("2000x1000")

# Load and display the image
image_path = "C:/Users/12130/Pictures/Screenshots/Screenshot (382).png"  # Replace with the actual path to your image
image = Image.open(image_path)
image = image.resize((300, 200))  # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack()

# Create the text box and submit button
entry = tk.Entry(window)
entry.pack()
submit_button = tk.Button(window, text="Submit", command=check_input)
submit_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main window loop
window.mainloop()
