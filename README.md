# Image Compression Script

This project contains a Python script for compressing images, reducing their file size while maintaining the aspect ratio. The script utilizes the Pillow library to handle image processing and allows you to specify the maximum desired file size.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To use this script, you need to have Python installed on your machine along with the Pillow library. Follow these steps to set up your environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/image-compression-script.git
   cd image-compression-script
   ```

2. **Install the required dependencies**:
   ```bash
   pip install Pillow
   ```

## Usage

Here's how to use the image compression script:

1. **Prepare your images**: Place the images you want to compress in a directory.

2. **Run the script**: Use the script to compress an image, specifying the input image path, output image path, and the maximum desired file size in KB.

### Example

```python
from PIL import Image
import os

def compress_image(input_image_path, output_image_path, max_size_kb):
    img = Image.open(input_image_path)
    
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
compress_image(r"C:\Users\User\Downloads\BrettPP.jpg", r"C:\Users\User\Downloads\BrettPPoutput.jpg", 250)
```

## Features

- Compress images to a specified maximum file size.
- Maintain the aspect ratio of images during compression.
- Adjust image quality to achieve desired file size.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -m 'Add feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Open a pull request**.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or issues, you can reach out to:
- **Email**: kingqreed@outlook.com
- **Twitter**: [@kxngqreed](https://twitter.com/kxngqreed)
