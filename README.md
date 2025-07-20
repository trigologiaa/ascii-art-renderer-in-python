# ASCII Art Renderer

A Python script that converts images into ASCII art based on pixel brightness.

Users can choose how many ASCII characters to use for brightness levels, optionally resize the image, and save the generated ASCII art to a file.

---

## Table of Contents

- [ASCII Art Renderer](#ascii-art-renderer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [Supported Formats](#supported-formats)
  - [License](#license)
  - [Contribute](#contribute)
  - [Contact](#contact)

---

## Features

- Convert any supported image format to ASCII art.
- Select brightness scale (1-25) for fine or coarse detail.
- Optionally resize the image before rendering.
- Prints ASCII art directly to the console.
- Save ASCII art to a text file (`ascii_art.txt`).
- Cross-platform (Windows, macOS, Linux).

---

## Requirements

- Python 3.8+
- [Pillow](https://pillow.readthedocs.io/en/stable/) (`PIL`)

Install dependencies:

```bash
pip install pillow
```

---

## Installation

Clone this repository:

```bash
git clone https://github.com/trigologiaa/ascii-art-renderer-in-python.git
cd ascii-art-renderer-in-python
```

---

## Usage

Run the script:

```bash
python main.py
```

Follow the prompts:

1. Enter the image file path (supports `.jpg`, `.png`, `.gif`, etc.).
2. Choose brightness scale (1-25).
3. Optionally resize the image (recommended: width ≤ 100 for large images).
4. Optionally save the ASCII art to a file.

---

## Example

Original image:

![example](/assets/example.png)

ASCII Art (Brightness scale: 25, resized to 50x50):

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~ ~ < ~ ~ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 > , - { ~ 0 0 0 0 0 0 0 0 0 < i - " .           ` , ! > 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 "     . . , ! > ~ 0 0 ~ ! "       . " : - - : , `       " i 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 `   { 0 > - `     . `       , i < 0 0 0 0 0 0 0 0 ~ { :     ` { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 . . 0 0 0 0 0 < i - : , ! < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < -     + 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 . . 0 0 0 0 0 0 0 0 0 0 < ` : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 { .   - 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 . . 0 0 0 0 0 0 0 0 0 0 ~ { + < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < `   ! 0 0 0 0 0 0 0 0 0 0 0 0 0
0 ~   ` 0 0 0 0 0 0 0 0 0 0 0 0 > ~ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < .   < 0 0 0 0 0 0 0 0 0 0 0 0
0 ~   ` 0 0 0 0 0 0 0 0 0 0 0 0 ~ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 !   - 0 0 0 0 0 0 0 0 0 0 0 0
0 ~   " 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~ 0 0 0 ` . 0 0 0 0 0 0 0 0 0 0 0 0
0 0 , . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 > > ~ 0 0 +   > 0 0 0 0 0 0 0 0 0 0 0
0 0 >   i 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ! { { { 0 0 >   " 0 0 0 0 0 0 0 0 0 0 0
0 0 0 i . { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 { . 0 ! ! 0 0 0 "   ! 0 0 0 0 0 0 0 0 0 0
0 0 0 0 < , - < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 !   + 0 " ! 0 0 0 {   . ~ 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 i , - < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < + .   : 0 {   > 0 0 0 0 `   + 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 { , : > 0 0 0 0 0 0 0 0 0 0 0 0 +     , { 0 ~ ` . 0 0 0 0 0 +   . ~ 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 i " ` 0 0 0 0 0 0 0 0 0 0 >   + ~ 0 0 0 :   + 0 0 0 0 0 >     i 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 >   + ~ 0 0 0 0 0 0 0 0 - { 0 0 0 0 +   . ~ 0 0 0 0 0 0 .   , 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 < i { ~ 0 0 0 0 0 0 0 { 0 0 0 0 {     { 0 0 0 0 0 0 0 "   . 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < `   - 0 0 0 0 0 0 0 0 "     < 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~ 0 0 0 0 0 0 0 0 0 0 0 ,   " ~ 0 0 0 0 0 0 0 0 "     < 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 > > 0 0 0 0 0 0 0 0 0 i     < 0 0 0 0 0 0 0 0 0 .     ~ 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 > + 0 0 0 0 0 0 0 0 0 "   ! 0 ~ < 0 0 0 0 0 0 >     ` 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 i " 0 0 0 0 0 0 0 0 <   , 0 < " > 0 0 0 0 0 0 ,     + 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 , " 0 0 0 0 0 0 0 0 {   ! - . - 0 0 0 0 0 0 {     . ~ 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 !   + 0 0 0 0 0 0 0 0 >     ` > 0 0 0 0 0 0 < .     { 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 -     < 0 0 0 0 0 0 0 0 ~   ` ~ 0 0 0 0 0 0 > .   . { 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 ,     + 0 0 0 0 0 0 0 0 0 0 , { 0 0 0 0 0 0 !     , < 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 +     , 0 > ~ 0 0 0 0 0 0 0 0 i ~ 0 0 0 0 > "   , { 0 0 > 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 .   ` ~ + > 0 0 0 0 0 0 0 0 0 0 0 0 0 { : ` - < 0 0 0 0 ! 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 <     > - , 0 0 0 0 0 0 0 0 0 0 0 ~ { + ! > 0 0 0 0 0 0 0 + ! 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 >   : i   i 0 0 0 0 0 0 0 0 0 0 0 ~ ~ 0 0 0 0 0 0 0 0 0 0 i   { 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 <   i .   > 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~     + ~ 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 ~ " !     > 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 :     . + 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 + i     i 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < `       " ~ 0 0 0
0 0 0 0 0 0 0 0 0 0 0 { <     + 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~ ! : `   : 0 0 0
0 0 0 0 0 0 0 0 0 0 0 ~ 0 -   - 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 i . ~ 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 {   ! 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 + > 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 {   ~ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 < > 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 , i 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 { > 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

---

## Supported Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`
- `.dds`
- `.pcx`
- `.jp2`
- `.exif`
- `.pnm`
- `.ras`
- `.tga`
- `.xbm`
- `.xpm`

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## Contact

For questions or contributions, open an issue or contact the author.
