import pytesseract
import cv2
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

def read_image(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    scale = 220
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    #final = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)[1]

    enhanced = cv2.detailEnhance(resized, sigma_s=10, sigma_r=0.15)
    # cv2.imshow("old image", resized)
    # cv2.imshow("new image", enhanced)
    #cv2.waitKey(0)
    #new_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(enhanced, config='--psm 6')
    text = text.splitlines()
    for i in range(len(text)):
        text[i] = re.sub(r'[^a-zA-Z]', '', text[i])

    return text

