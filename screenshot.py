import pyautogui
from datetime import datetime
import pyscreenshot as psc
import cv2


def take_screenshot():
    dt = datetime.now()
    time = dt.strftime("%H:%M%S")
    shot = cv2.imwrite("screenshot", psc.grab())
    #image = shot.save(f"screenshots/screenshot_{time}.png")

    return shot
