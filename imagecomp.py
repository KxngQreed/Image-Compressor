from PIL import Image
import os

def compress_image(input_image_path, output_image_path, max_size_kb):
    img = Image.open(path_to_your_file_goes_here)
    
    # Reduce image size while maintaining aspect ratio
    img.thumbnail((img.width // 2, img.height // 2))

    # Save image with reduced quality
    quality = 85
    while True:
        img.save(output_image_path, "JPEG", quality=quality)
        if os.path.getsize(output_image_path) <= max_size_kb * 1024:
            break
        quality -= 5
        if quality < 10:
            break
    
    print(f"Image saved as {output_image_path} with size {os.path.getsize(output_image_path) / 1024:.2f} KB")

# Example usage
compress_image(r"C:\Users\User\Downloads\Picture.jpg", r"C:\Users\User\Downloads\Pictureoutput.jpg", 250)
