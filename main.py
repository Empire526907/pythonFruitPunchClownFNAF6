# Be sure to install these if you don't have them!
import cv2 as cv
from PIL import Image
import numpy as np
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import pytesseract

# Included
import time
from windowCapture import WindowCapture

# Install from https://github.com/UB-Mannheim/tesseract/wiki and set install file path below ↓ (Probably just change "Program Files" to "Program Files (x86)" if it doesn't already work)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# wincap = WindowCapture('HelloPython – main.py')
wincap = WindowCapture("Freddy Fazbear's Pizzeria Simulator")
# wincap = WindowCapture("Screenshot (3252).png - paint.net 4.2.8")
# wincap.list_window_names()

starting_w = 1904
starting_h = 1042


def scale_width(res_input):
    scale_to = wincap.w
    return round(scale_to / starting_w * res_input)


def scale_height(res_input):
    scale_to = wincap.h
    return round(scale_to / starting_h * res_input)


keyboard = KeyboardController()
mouse = MouseController()
middle_width = 1000
x1 = 0
y1 = 640
w1 = (1920 - middle_width) / 2
h1 = 200
x2 = x1 + w1 + middle_width
y2 = y1
w2 = w1
h2 = h1
# FINISHED! Button
x3 = 1569
y3 = 950
w3 = 297
h3 = 59
# PRESS SPACE Text
x4 = 781
y4 = 951
w4 = 356
h4 = 69
# reset_time = 12.6  # Time before clicking on the game again
clown_pos = [scale_width(740), scale_height(540)]
play_button_pos = [scale_width(560), scale_height(600)]
mode = "clownInit"
# for i in range(5, -1, -1):
#     print(i)
#     if i == 0:
#         print("Enter the Clown to Begin")
#     else:
#         time.sleep(1)
print("Enter the Clown to Begin")
while True:
    if mode == "clownInit":

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # cv.imshow('Computer Vision', screenshot)

        img_hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)

        colorRange = 30
        rgb_color = np.uint8([[[248, 145, 104]]])
        hsv_color = cv.cvtColor(rgb_color, cv.COLOR_RGB2HSV)[0][0]
        hsv_color1 = np.asarray([hsv_color[0] - 10, hsv_color[1] - colorRange, hsv_color[2] - colorRange])
        hsv_color2 = np.asarray([hsv_color[0] + 10, hsv_color[1] + colorRange, hsv_color[2] + colorRange])

        mask = cv.inRange(img_hsv, hsv_color1, hsv_color2)

        img_left = mask[scale_height(y1):scale_height(y1) + scale_height(h1), scale_width(x1):scale_width(x1) + scale_width(w1)]
        img_right = mask[scale_height(y2):scale_height(y2) + scale_height(h2), scale_width(x2):scale_width(x2) + scale_width(w2)]

        cv.imshow('img_left', img_left)
        cv.imshow('img_right', img_right)

        img = screenshot[scale_height(y4):scale_height(y4) + scale_height(h4), scale_width(x4):scale_width(x4) + scale_width(w4)]

        img_text = pytesseract.image_to_string(img)

        # print(img_text, wincap.w, wincap.h)

        cv.imshow('img', img)

        if "PRESS SPACE" in img_text:
            mode = "clown"
            print("Ready")

    if mode == "clown":
        keyboard.release("a")
        keyboard.release("s")

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # cv.imshow('Computer Vision', screenshot)

        img_hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)

        colorRange = 30
        rgb_color = np.uint8([[[248, 145, 104]]])
        hsv_color = cv.cvtColor(rgb_color, cv.COLOR_RGB2HSV)[0][0]
        hsv_color1 = np.asarray([hsv_color[0] - 10, hsv_color[1] - colorRange, hsv_color[2] - colorRange])
        hsv_color2 = np.asarray([hsv_color[0] + 10, hsv_color[1] + colorRange, hsv_color[2] + colorRange])

        mask = cv.inRange(img_hsv, hsv_color1, hsv_color2)

        img_left = mask[scale_height(y1):scale_height(y1) + scale_height(h1), scale_width(x1):scale_width(x1) + scale_width(w1)]
        img_right = mask[scale_height(y2):scale_height(y2) + scale_height(h2), scale_width(x2):scale_width(x2) + scale_width(w2)]

        cv.imshow('img_left', img_left)
        cv.imshow('img_right', img_right)

        if len(Image.fromarray(np.uint8(img_left)).convert('RGB').getcolors(2)) == 1 and len(
                Image.fromarray(np.uint8(img_right)).convert('RGB').getcolors(2)) == 1:
            keyboard.press(Key.space)
            print("Froot Punch for Everyone")
            time.sleep(1)
            keyboard.release(Key.space)
            mode = "reset"

    if mode == "reset":
        # print("Resetting")
        keyboard.press("a")
        keyboard.press("s")

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # cv.imshow('Computer Vision', screenshot)

        # img_hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        #
        # colorRange = 5
        # rgb_color = np.uint8([[[144, 145, 146]]])
        # hsv_color = cv.cvtColor(rgb_color, cv.COLOR_RGB2HSV)[0][0]
        # hsv_color1 = np.asarray([min(hsv_color[0] - 10, 180), min(hsv_color[1] - colorRange, 255), min(hsv_color[2] - colorRange, 255)])
        # hsv_color2 = np.asarray([min(hsv_color[0] + 10, 180), min(hsv_color[1] + colorRange, 255), min(hsv_color[2] + colorRange, 255)])
        #
        # mask = cv.inRange(img_hsv, hsv_color1, hsv_color2)

        img = screenshot[scale_height(y3):scale_height(y3) + scale_height(h3), scale_width(x3):scale_width(x3) + scale_width(w3)]

        img_text = pytesseract.image_to_string(img)

        # print(img_text)

        cv.imshow('img', img)

        if "FINISHED!" in img_text:
            print("Resetting")
            # time.sleep(reset_time)
            mouse.position = clown_pos
            mouse.click(Button.left)
            time.sleep(0.15)
            mouse.position = play_button_pos
            mouse.click(Button.left)
            mode = "clown"
            time.sleep(2)
            print("Ready")

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
