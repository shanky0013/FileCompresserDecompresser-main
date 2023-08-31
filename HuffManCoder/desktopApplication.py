import tkinter as tk
from tkinter import filedialog
import os
import sys
current_dir=os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from compressorDecompressor import HuffmanCode
# Function to process the uploaded file
# this for compression
def process_file(file_path):
    h=HuffmanCode(file_path)
    # Example processing: convert text to uppercase
    processed_file_path=h.fileCompress()
    return processed_file_path

# Function to handle file upload
def upload_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()

    # Check if a file was selected
    if file_path:
        # Process the file
        processed_file_path = process_file(file_path)

        # Show success message
        result_label.config(text=f"File processed and saved as '{processed_file_path}'.")

# Function to handle file download
def download_file():
    # Open file dialog to select a location to save the processed file
    save_path = filedialog.asksaveasfilename(defaultextension=".txt")

    # Check if a location was selected
    if save_path:
        # Get the processed file path
        processed_file_path = result_label.cget("text").split("'")[1]

        # Copy the processed file to the selected location
        os.replace(processed_file_path, save_path)

        # Show success message
        result_label.config(text="File downloaded successfully.")

# Create the main application window
window = tk.Tk()
window.title("File Processor")

# Create the file upload button
upload_button = tk.Button(window, text="Upload File", command=upload_file)
upload_button.pack(pady=10)

# Create the file download button
download_button = tk.Button(window, text="Download File", command=download_file)
download_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the application
window.mainloop()
