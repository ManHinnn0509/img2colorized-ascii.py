import os
import time

from img2colorized_ascii import printImageASCII
from util.file_utils import readJsonFile

def main():

    clearScreen = "cls"
    os.system(clearScreen)

    jsonFileName = 'rendered_frames.json'
    if (jsonFileName not in os.listdir()):
        print("Pre-rendered frames (json file) not found!")
        return
    
    d = readJsonFile(jsonFileName)

    fps = d.pop('fps', None)
    frameAmount = d.pop('frame_amount')

    for k, v in d.items():
        printImageASCII(v)
        # time.sleep(1 / fps)

    print("--- End of Program ---")

if (__name__ == '__main__'):
    main()