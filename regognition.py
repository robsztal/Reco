from field_of_interest import *
import pytesseract
import cv2
from operations import *

# path bypass
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
image = cv2.imread("to_recognition.png")

noise = remove_noise(image)
gray = get_grayscale(noise)
thresh = thresholding(gray)
opening = opening(thresh)

cv2.imshow("changed", image)
cv2.waitKey()
processed = pytesseract.image_to_string(thresh)
print(processed)
