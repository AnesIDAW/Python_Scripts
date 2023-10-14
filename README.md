# Image Manipulation Script

This an Image Manipulation Python Script that allows you to process a batch of images by resizing, rotating, and saving them in a specified format. 
It leverages the Pillow library for image processing and concurrent execution for faster processing.

## Features

- Resize images to a specified width and height.
- Save images in a user-specified format (JPEG, PNG, or GIF).

## Requirements

- Python 3.6 or higher.
- The Pillow library (PIL).

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AnesIDAW/image-manipulation-script.git
   cd image-manipulation-script
   ```

2. **Install Pillow**:

   If you haven't already installed the Pillow library, you can do so using `pip`:

   ```bash
   pip install Pillow
   ```

3. **Run the Script**:

   The script accepts command-line arguments to specify the input folder, output folder, image size, and format.

   Example:

   ```bash
   python image_manipulation.py --input /path/to/input/folder --output /path/to/output/folder --size 700 400 --format JPEG
   ```

   - `--input`: Path to the input folder containing images.
   - `--output`: Path to the output folder where modified images will be saved.
   - `--size`: Desired image size in WIDTH HEIGHT format.
   - `--format`: Output image format (JPEG, PNG, or GIF).

4. **Review the Results**:

   The script will process the images, and the modified images will be saved in the specified output folder.

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or create a pull request.

```

