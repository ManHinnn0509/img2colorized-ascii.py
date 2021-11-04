import sys

import cv2
import numpy as np

from PIL import Image

from asciify import do
from util.color_utils import colorizeString, genANSI_TextTrueColorCode, genANSI_BackTrueColorCode

def main():

    # img = Image.open('./img2.png')
    # printImageASCII(img)

    pathToVideo = './vid/watch_dogs_intro.mp4'
    vidcap = cv2.VideoCapture(pathToVideo)
    success, frame = vidcap.read()

    while (success):
        # Convert frame to PIL Image
        imgPIL = convertFrame(frame)

        s = render(imgPIL)
        printImageASCII(s)

        success, frame = vidcap.read()
    
    vidcap.release()

def convertFrame(frame) -> Image:
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgPIL = Image.fromarray(img)

    return imgPIL

def render(img):
    """
        Takes a input of PIL Image \n
        Returns rendered colorized ASCII art of the input image
    """

    # Fixed size
    newSize = (100, 56)
    img = img.resize(newSize)

    # img.show()

    rgb = img.convert("RGB")
    # print(f'Size = {rgb.size}')

    W = rgb.size[0]
    H = rgb.size[1]

    # [[0 for x in range(cols_count)] for x in range(rows_count)]
    imgColors = [[0 for x in range(newSize[0])] for x in range(newSize[1])]

    # When accessing:
    # imgColors[row][col] <- row = h | col = w

    # Save the color of each pixel
    for h in range(0, H):
        for w in range(0, W):
            pixel = rgb.getpixel((w, h))
            imgColors[h][w] = pixel

    # Converts the frame (Image object) into ASCII art
    asciiImg = do(img)
    lines = asciiImg.split("\n")

    # bgColor = (0, 0, 0)
    # backColorCode = genANSI_BackTrueColorCode(bgColor[0], bgColor[1], bgColor[2])

    s = ""
    for l in range(0, len(lines)):
        line = lines[l]
        for i in range(0, len(line)):
            color = imgColors[l][i]
            char = line[i]

            colorCode = genANSI_TextTrueColorCode(color[0], color[1], color[2])
            c = colorizeString(
                char,
                colorCode
                # backColorCode
            )

            # print(c, end='')
            s += c
        
        # print("")
        s += "\n"
    
    return s

def printImageASCII(s: str):
    
    linesAmount = len(s.split("\n")) + 1
    print(s)

    # Erase the previous output
    # From: https://www.daniweb.com/programming/software-development/threads/428136/clear-the-screen-without-os-library
    for _ in range(linesAmount):
        sys.stdout.write("\x1b[1A\x1b[2K") # move up cursor and delete whole line

if (__name__ == '__main__'):
    main()