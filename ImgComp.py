import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def compress_image(image_path, output_path, quality):
    """
    Compresses an image and saves it to the specified output path.
    
    :param image_path: The path to the image to compress.
    :type image_path: str
    :param output_path: The path to save the compressed image to.
    :type output_path: str
    :param quality: The quality of the compressed image (1-95).
    :type quality: int
    """
    image = Image.open(image_path)
    image.save(output_path, optimize=True, quality=quality)

root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename()
dir = os.path.dirname(image_path)
fname = os.path.basename(image_path)
output_path = dir + "/compressed_" + fname
#output_path = filedialog.asksaveasfilename(defaultextension='.jpg')
print("Quality range: 1-95")
quality = int(input("Enter the desired quality: ")) 
compress_image(image_path, output_path, quality)
