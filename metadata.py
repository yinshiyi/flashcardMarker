import os
import csv

# Set up the image folder
image_folder = "images"  # Replace with the actual path to your image folder

# Get the list of image filenames
images = os.listdir(image_folder)

# Create the CSV file and write the image filenames
csv_file = "metadata/metadata.csv"  # Path to the output CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["filename"])  # Write the header row
    for image in images:
        writer.writerow([image])  # Write each image filename

print(f"CSV file '{csv_file}' generated successfully.")
