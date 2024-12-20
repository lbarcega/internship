import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize BlobServiceClient
connection_string = os.environ.get('AZURE_CONNECTION_STRING')
container_name = os.environ.get('AZURE_CONTAINER_NAME')
    # Setup the blob service client and blob clients
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def upload_blob(file_path):
    blob_name = os.path.basename(file_path)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    messagebox.showinfo("Success", f"File '{blob_name}' uploaded successfully.")

def download_blob(blob_name, download_path):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(download_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    messagebox.showinfo("Success", f"File '{blob_name}' downloaded successfully to '{download_path}'.")

def list_blobs():
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    return [blob.name for blob in blobs]

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        upload_blob(file_path)

def view_image(blob_name):
    download_path = os.path.join(os.getcwd(), blob_name)
    download_blob(blob_name, download_path)
    img = Image.open(download_path)
    img.show()

def create_app():
    root = tk.Tk()
    root.title("Azure Blob Storage Manager")

    upload_button = tk.Button(root, text="Upload Image", command=browse_file)
    upload_button.pack(pady=10)

    list_button = tk.Button(root, text="List Images", command=lambda: show_images(root))
    list_button.pack(pady=10)

    root.mainloop()

def show_images(root):
    top = tk.Toplevel(root)
    top.title("List of Images")

    blobs = list_blobs()
    for blob_name in blobs:
        button = tk.Button(top, text=blob_name, command=lambda name=blob_name: view_image(name))
        button.pack(pady=5)

if __name__ == "__main__":
    create_app()
