"""
ASCII Art Renderer

This script converts an input image into an ASCII art representation based on
the brightness of each pixel. Users can select the number of ASCII characters
to use for mapping brightness levels, as well as optionally resize the image.

Dependencies:
    - Pillow (PIL)

Usage:
    Run the script and follow the prompts:
    1. Enter the image file path.
    2. Select the brightness scale (1-25).
    3. Optionally resize the image.
    The ASCII art will be printed to the console.
"""

import os
from typing import List, Tuple
from PIL import Image

# Mapping of brightness scales to ASCII character sets.
#
# Higher keys correspond to more detailed gradients.
ascii_b_scale = {
    "1": " ",
    "2": " .",
    "3": " .0",
    "4": " .:0",
    "5": " .,:0",
    "6": " .,:-0",
    "7": " .,:-+0",
    "8": " .`,:-+0",
    "9": ' .`",:-+0',
    "10": ' .`",:-+~0',
    "11": ' .`",:-+!~0',
    "12": ' .`",:-+!i~0',
    "13": ' .`",:-+!i{~0',
    "14": ' .`",:-+!i{>~0',
    "15": ' .`",:-+!i{><~0',
    "16": ' .`",:-+!i{><~+0',
    "17": ' .`",:-+!i{><~+r0',
    "18": ' .`",:-+!i{><~+rz0',
    "19": ' .`",:-+!i{><~+rz%0',
    "20": ' .`",:-+!i{><~+rz#%0',
    "21": ' .`",:-+!i{><~+rzZ#%0',
    "22": ' .`",:-+!i{><~+rzLZ#%0',
    "23": ' .`",:-+!i{><~+rz|LZ#%0',
    "24": ' .`",:-+!i{><~+rz?|LZ#%0',
    "25": ' .`",:-+!i{><~+rzU?|LZ#%0',
}

# Supported image file extensions for Pillow.
valid_formats = (
    ".dds",
    ".bmp",
    ".exif",
    ".gif",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".jpx",
    ".pcx",
    ".png",
    ".pnm",
    ".ras",
    ".tga",
    ".tif",
    ".tiff",
    ".xbm",
    ".xpm",
)


def calculate_brightness(img_data: List[Tuple[int, int, int]]) -> List[int]:
    """
    Calculate the brightness of each pixel in an RGB image.

    Brightness is computed as a weighted sum of the R, G, and B channels:
    brightness = 0.33*R + 0.5*G + 0.16*B

    Args:
        img_data (list[tuple]): A list of (R, G, B) pixel tuples.

    Returns:
        list[int]: A list of brightness values (0-255) for each pixel.
    """
    px_bright = []
    for px in img_data:
        r, g, b = px
        bright = 0.33 * r + 0.5 * g + 0.16 * b
        px_bright.append(int(round(bright)))
    return px_bright


def render_ascii_art(b_values: List[int], width: int, b_scale: str) -> None:
    """
    Render ASCII art to the console based on pixel brightness.

    Args:
        b_values (list[int]): List of brightness values per pixel.
        width (int): Width of the image (used for line breaks).
        b_scale (str): A string of ASCII characters for mapping brightness.
    """
    scale_length = len(b_scale)
    for i, px in enumerate(b_values):
        if i % width == 0 and i != 0:
            print()
        if px == 0:
            px_index = 0
        else:
            px_index = int(px / (255 / scale_length))
        print(b_scale[px_index], end=" ")


def main() -> None:
    """
    Main entry point for the script.

    Prompts the user for:
        - Image file path
        - Brightness scale (1-25)
        - Whether to resize the image

    Then displays the ASCII art in the console.
    """
    img_path = input("Image path: ")
    if not os.path.isfile(img_path):
        raise FileNotFoundError("File path does not exist.")
    file_ext = os.path.splitext(img_path)[1].lower()
    if file_ext not in valid_formats:
        raise IOError("Unsupported image file format.")
    b_key = input("Brightness scale (1-25): ")
    if b_key not in ascii_b_scale:
        raise ValueError("Brightness scale must be 1-25.")
    b_scale = ascii_b_scale[b_key]
    with Image.open(img_path).convert("RGB") as img:
        print(f"Image size: {img.width}x{img.height}")
        resize_choice = input("Resize image? (Y/n): ").strip().upper()
        if resize_choice == "Y":
            width = int(input("New width: "))
            height = int(input("New height: "))
            img = img.resize((width, height))
        else:
            width, height = img.width, img.height
        data = list(img.getdata())
        b_values = calculate_brightness(data)
        os.system("cls")
        render_ascii_art(b_values, width, b_scale)
    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
