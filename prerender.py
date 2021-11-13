import os
import time
import cv2

from img2colorized_ascii import render, convertFrame, printImageASCII
from util.file_utils import writeJSON_File

"""
    Open video, render all the frames
    Then save as json / play
"""

def main():

    clearScreen = "cls"
    pathToVideo = './vid/ricardo.mp4'
    outputFile = './rendered_frames.json'

    vidcap = cv2.VideoCapture(pathToVideo)

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frameAmount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    vidLen = int(frameAmount / fps)

    success, frame = vidcap.read()

    d = {}

    d['fps'] = fps
    d['frame_amount'] = frameAmount

    print(f"FPS: {fps}")
    print(f"Frame amount: {frameAmount}")

    frameCounter = 0
    while (success):
        k = f'frame_{frameCounter}'
        print(f"Rendering ... {k} ({frameCounter + 1} / {frameAmount})")

        img = convertFrame(frame)
        renderedFrame = render(img)
        
        d[k] = renderedFrame

        success, frame = vidcap.read()
        frameCounter += 1
    
    vidcap.release()

    
    # Part that saves the rendered frames
    print(f"Rendered {frameCounter + 1} frame(s)")

    r = writeJSON_File(outputFile, d)
    if (r):
        print("SUCCESS! Saved rendered frames!")
    else:
        print("ERROR! Unable to save rendered frames!")

    print("--- End of Program ---")
    

    """
    # Part that plays the video after rendering
    print("All frames rendered!")

    ignored = input("Press Enter to continue...")
    os.system(clearScreen)

    for k, frame in d.items():
        printImageASCII(frame)
        time.sleep(1 / 60)      # 60 Hz?
    """

if (__name__ == '__main__'):
    main()