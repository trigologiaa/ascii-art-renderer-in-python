# ASCII Art Renderer

A Python script that converts images into ASCII art based on pixel brightness.

Users can choose how many ASCII characters to use for brightness levels and
optionally resize the image before rendering.

---

## Features

- Convert any supported image format to ASCII art.
- Select brightness scale (1-25) for fine or coarse detail.
- Optionally resize the image before rendering.
- Prints ASCII art directly to the console.

---

## Requirements

- Python 3.6+
- [Pillow](https://pillow.readthedocs.io/en/stable/) (`PIL`)

Install dependencies with:

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

1. Enter the image file path (supports `.jpg`, `.png`, `.gif`, etc).
2. Choose brightness scale (1-25).
3. Optionally resize the image (recommended to 50x50).

---

## Example

Original image:

![example](/assets/example.png)

ASCII Art (Brightness scale: 25, resized to 50x50):

```md
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 % # Z Z Z % 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 ? + { U % 0 0 0 0 0 0 0 0 0 Z r { : ` .       . " + ~ | 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 -     ` " + + | # 0 0 Z + :       ` : ! { { i + ,       : r % 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 "   z % ? > , . . ` , .   . ! r L % 0 0 0 0 0 0 0 Z z !     , U 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 " ` % 0 0 0 0 Z z > ! + + Z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Z {     < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 " " 0 0 0 0 0 0 0 0 0 0 Z , i 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? "   { 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 % ` " 0 0 0 0 0 0 0 0 0 0 # ? > L 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Z ,   + 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 # . " 0 0 0 0 0 0 0 0 0 0 0 0 ? # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 L . . Z 0 0 0 0 0 0 0 0 0 0 0 0 
0 #   , 0 0 0 0 0 0 0 0 0 0 0 0 # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 +   { 0 0 0 0 0 0 0 0 0 0 0 0 
0 % . : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # 0 0 0 " ` % 0 0 0 0 0 0 0 0 0 0 0 
0 0 - ` 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | | # 0 0 >   | 0 0 0 0 0 0 0 0 0 0 0 
0 0 ?   z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~ U U U 0 0 ?   - 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 z " U 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 z ` % ~ ~ 0 0 0 :   + 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 | + { Z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 % ~   > 0 : + 0 0 0 z   ` # 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 z + > L 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 L > "   ! 0 U   ? 0 0 0 0 ,   < 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 z + i ? % 0 0 0 0 0 0 0 0 0 0 0 <     + U 0 % " ` % 0 0 0 0 <   ` % 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 z - , 0 0 0 0 0 0 0 0 0 0 ?   < Z 0 0 0 !   < 0 0 0 0 0 |     r 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 |   < # 0 0 0 0 0 0 0 0 { z 0 0 0 0 ~   " # 0 0 0 0 0 % `   ! 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 L r U # 0 0 0 0 0 0 % U 0 0 0 0 U .   z 0 0 0 0 0 0 0 :   " % 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 % 0 0 0 L "   { 0 0 0 0 0 0 0 0 -     Z 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # % 0 0 % 0 0 0 0 0 0 0 +   : % 0 % 0 0 0 0 0 0 :     L 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | | 0 0 0 0 0 0 0 0 0 r   . | 0 0 0 0 0 0 0 0 % `   . Z 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? < 0 0 0 0 0 0 0 0 0 :   + 0 Z Z 0 0 0 0 0 0 ?     , 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 z - 0 0 0 0 0 0 0 0 L   - 0 L : | 0 0 0 0 0 0 !     > 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 + - 0 0 0 0 0 0 0 0 U   + { ` > 0 0 0 0 0 0 U     ` # 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 ~   > 0 0 0 0 0 0 0 0 ?     " ? 0 0 0 0 0 0 L `   . U 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 % {   . Z 0 0 0 0 0 0 0 0 # . , # 0 0 0 0 0 0 | `   ` U 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 % +     ~ 0 % 0 0 0 0 0 0 0 0 + U 0 0 0 0 0 0 +     ! L 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 <     + 0 ? % 0 0 0 0 0 0 0 0 r # 0 0 0 0 ? :   - U 0 0 | 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 % `   " # < ? 0 0 0 0 0 0 0 0 0 % 0 0 0 U ! , > L 0 0 0 0 + % 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 L     ? > + 0 0 0 0 0 0 0 0 0 0 0 # ? ~ ~ ? 0 0 0 0 0 0 0 > + 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 |   i r   z 0 0 0 0 0 0 0 0 0 0 % Z # 0 0 0 0 0 0 0 0 0 0 z . ? 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 L   z `   | 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # .   < # 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 Z : +     ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 !     ` < % 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 % > r     z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Z "       : # 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 U L .   < 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # ~ ! ,   ! 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 Z 0 {   > 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 z ` # 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 U   + 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 > | 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 z . Z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 L | 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 % ! z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 % 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 U ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 % 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
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

## Contact

For questions or contributions, please open an issue or contact the author.
