import os
from PIL import Image

def convert_png_to_jpg(png_path, jpg_path):
    # Open PNG image
    img = Image.open(png_path)
    # Convert to RGB mode (if PNG has transparency)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    # Save as JPEG
    img.save(jpg_path)

def batch_convert_png_to_jpg(png_folder, jpg_folder):
    # Create output directory if not exists
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)
    # Iterate through PNG files
    for filename in os.listdir(png_folder):
        if filename.endswith('.png'):
            png_path = os.path.join(png_folder, filename)
            jpg_path = os.path.join(jpg_folder, filename.replace('.png', '.jpg'))
            # Convert PNG to JPEG
            convert_png_to_jpg(png_path, jpg_path)

# Specify input and output directories
png_folder = 'static/card_backs'  # Change to your PNG images folder
jpg_folder = 'static/converted_png'  # Change to your output folder

# Convert PNG images to JPEG
batch_convert_png_to_jpg(png_folder, jpg_folder)