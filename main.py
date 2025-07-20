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
    The ASCII art will be printed to the console and can optionally be saved.
"""

import os
import sys
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

def render_ascii_art(b_values: list[int], width: int, b_scale: str) -> str:
    """
    Generate ASCII art string based on pixel brightness.

    Args:
        b_values (list[int]): List of brightness values per pixel.
        width (int): Width of the image (used for line breaks).
        b_scale (str): A string of ASCII characters for mapping brightness.

    Returns:
        str: The generated ASCII art.
    """
    scale_length = len(b_scale)
    art_lines = []
    line = ""
    for i, px in enumerate(b_values):
        if i % width == 0 and i != 0:
            art_lines.append(line)
            line = ""
        px_index = min(scale_length - 1, int(px / (256 / scale_length)))
        line += b_scale[px_index] + " "
    art_lines.append(line)
    return "\n".join(art_lines)


def main() -> None:
    """
    Main entry point for the script.

    Prompts the user for:
        - Image file path
        - Brightness scale (1-25)
        - Whether to resize the image

    Then displays the ASCII art in the console and offers to save it.
    """
    img_path = input("Image path: ").strip()
    if not os.path.isfile(img_path):
        print("File path does not exist.")
        return
    file_ext = os.path.splitext(img_path)[1].lower()
    if file_ext not in valid_formats:
        print("Unsupported image file format.")
        return
    while True:
        b_key = input("Brightness scale (1-25): ").strip()
        if b_key in ascii_b_scale:
            break
        print("Invalid scale. Enter a number between 1 and 25.")
    b_scale = ascii_b_scale[b_key]
    try:
        with Image.open(img_path).convert("L") as img:
            print(f"Image size: {img.width}x{img.height}")
            resize_choice = input("Resize image? (Y/n): ").strip().upper()
            if resize_choice == "Y":
                width = int(input("New width: "))
                height = int(input("New height: "))
                img = img.resize((width, height))
            else:
                width, height = img.width, img.height
            b_values = list(img.getdata())
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    os.system("cls" if os.name == "nt" else "clear")
    art = render_ascii_art(b_values, width, b_scale)
    print(art)
    save_choice = input("\nSave ASCII art to file? (Y/n): ").strip().upper()
    if save_choice == "Y":
        output_file = "ascii_art.txt"
        try:
            with open(output_file, "w") as f:
                f.write(art)
            print(f"ASCII art saved to '{output_file}'.")
        except IOError as e:
            print(f"Failed to save file: {e}")
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()