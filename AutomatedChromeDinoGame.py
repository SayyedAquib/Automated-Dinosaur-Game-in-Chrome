import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(200, 315):
        for j in range(270, 357):
            if data[i, j] < 100:
                hit("down")
                return

    # Draw the rectangle for cactus
    for i in range(200, 315):
        for j in range(377, 461):
            if data[i, j] < 100:
                hit("up")
                return
    return




if __name__ == "__main__":
    print("Hey... Dino game about to start in 3 seconds")
    time.sleep(5)


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
