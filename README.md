# Python Plays the Fruit Punch Clown from FNAF 6 (Pizzaria Simulator)

From the video: https://youtu.be/0IA_OfUNCPg

# Dependencies

Python, OpenCV, Pillow, numpy, pynput, pywin32, and pytesseract.

Pytesseract is more complicated, you will probably have to install it from here: https://github.com/UB-Mannheim/tesseract/wiki and if you install the 32-bit version, you will need to change "Program Files" to "Program Files (x86)" in line 14 of "main.py"

# Setup

This project was created with a 1920x1080p resolution in mind. I have tried to make it detect the current resolution and scale everything to match, but this is untested.

This program assumes that the Clown is in the third from the top spot on the left side in the fully upgraded pizzarea, as seen in the video (https://youtu.be/0IA_OfUNCPg). If you want the Clown in a different spot, because the program holds down some movement keys, then clicks in two, precise spots to start the game after a win, you have to:
1. In game, hold down "a", "s", "d", or some combination of those until the Clown is visible on your screen and modify lines 104, 105, 138, and 139 in "main.py", replacing "a" and "s" with the keys your using, unless holding "a" and "s" already does the job.
2. Get the screen position of the Clown, and the "Play" button that pops up after clicking on the Clown. To do this, I recommend taking a screenshot of the game with those two things in place, then use an image editing software, I use Paint.net, to resize the screenshot to 1904x1042 (Weird window border cropping), and get the position of those objects in the resized image. Modify lines 57 and 58 with those coordinates (clown_pos = [scale_width(x), scale_height(y)])

# Stuff Other People Made That I Used

1. windowCapture.py is from: https://www.youtube.com/watch?v=WymCpVUPWQ4 - Learn Code by Gaming https://github.com/learncodebygaming/opencv_tutorials/tree/master/004_window_capture
