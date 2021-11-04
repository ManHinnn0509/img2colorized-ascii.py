# img2colorized-ascii.py

Play video in colorized ASCII art in console

The file [asciify.py][file_asciify.py] in this project is from [this repository][github_asciify], credits to them. (I only added a little bit changes to it for this project)

I added example images & videos which are clips and screenshots from Watch_Dogs & Cyberpunk 2077. I don't own them

## Run this program

### Real-time render & play

Windows: `cls && python img2colorized_ascii.py` <br>
Linux: `clear && python img2colorized_ascii.py`

### Pre-render

First, run `python prerender.py` to pre-render frames. It will save them as json file. (The json file size might be a bit large!)

Then run `python prerender_play.py` to play the "video"

## Requirements / Dependencies

See [requirements.txt][file_requirements]

## How does it works?

Steps:

1) Opens the video from given path
2) Read frame
3) Convert the image (cv2) to PIL image
4) Resize the PIL image
5) Mark down each pixel's color
6) Turn the image to ASCII art
7) Colorized the characters with color
8) Print out the colorized ASCII image
9) Clears previous output
10) Read next frame
11) Back to Step 3

## Why resizing the frame?

This is because the amount of charater per line in console is somehow limited (If I understand correctly) <br>
In my case it's 100 characters per line <br>

I resize the frame's width and height in ratio. <br>
For example, a 1920x1080 image will be resized to 100x56

## Notice

* The height of each output frame is 56
* The speed might be slower since it does all the steps above in real time (If it's not pre-rendered)
* There should be some blinking between each frame

## Planned

I might do these someday but not sure when :P

- [x] [Pre-render frames][file_prerender]

[file_prerender]: ./prerender.py
[file_main_py_file]: ./img2colorized_ascii.py
[file_asciify.py]: ./asciify.py
[file_requirements]: ./requirements.txt
[github_asciify]: https://github.com/RameshAditya/asciify