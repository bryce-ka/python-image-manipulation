# Collage Creation Python Script

This repository contains a Python script that demonstrates various attempts at creating collages. The script utilizes the `csc121` library for image manipulation. 

## Authors
- Isaac Bynum
- Bryce Anthony

## Installation
To run the script, you need to install the `csc121` library. You can install it using pip:

```
pip install csc121
```

## Usage
The script provides three functions for creating different types of collages: `gradient_blend()`, `mirror()`, and `pencil_sketch()`.

### Gradient Blend
The `gradient_blend()` function smoothly blends the images of Bryce and Jack to create a gradient effect. It combines the red, green, and blue channels of the two images to create a new blended image. The resulting image is saved as `blended.jpeg`.

### Mirror
The `mirror()` function mirrors an image across the y-axis. It prompts the user to enter the name of the file they want to mirror. The script then reads the red, green, and blue channels of the image and mirrors them to create the mirrored effect. The resulting image is saved as `mirrored.jpeg`.

### Pencil Sketch
The `pencil_sketch()` function converts an image to appear as if it were drawn with a pencil. It prompts the user to enter the name of the file they want to convert. The script then reads the red, green, and blue channels of the image and applies a pencil sketch effect by analyzing the grayscale values of neighboring pixels. The resulting image is saved as `sketched.jpeg`.

To use any of the functions, uncomment the function call at the end of the script and run the script.

## Images
The images used in the script can be found in this repository.

Note: Make sure to place the images you want to use in the same directory as the script or provide the correct path when prompted.

Feel free to experiment with different images and modify the script to create your own unique collages!

**Enjoy creating collages!**
