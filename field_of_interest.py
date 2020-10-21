import cv2
import numpy as np
import pyautogui as pg
import imutils


def rectangle_selection():
	# take a screenshot

	image = pg.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	cv2.imwrite("to_memory.png", image)
	image = cv2.imread("to_memory.png")

	# define rectangle area
	from_center = False
	r = cv2.selectROI(image, from_center)
	roi = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

	cv2.imshow("ROI", roi)
	cv2.imwrite("to_recognition.png", roi)


rectangle_selection()