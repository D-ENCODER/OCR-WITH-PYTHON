import cv2
import noice
import font
import skew
import border
import pytesseract
import detected
from PIL import Image


image_file = "data/capture.png"
img = cv2.imread(image_file)
inverted_image = cv2.bitwise_not(img)
cv2.imwrite("temp/inverted.jpg", inverted_image)


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray_image = grayscale(img)
thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
cv2.imwrite("temp/black_white.jpg", im_bw)
no_noise = noice.noise_removal(im_bw)
cv2.imwrite("temp/no_noise.jpg", no_noise)
eroded_image = font.thin_font(no_noise)
cv2.imwrite("temp/thin_font.jpg", eroded_image)
dilated_image = font.thick_font(no_noise)
cv2.imwrite("temp/thick_font.jpg", dilated_image)
new = cv2.imread(image_file)
fixed = skew.deskew(new)
no_borders = border.remove_borders(no_noise)
color = [255, 255, 255]
top, bottom, left, right = [150]*4
image_with_border = cv2.copyMakeBorder(
    no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

img = Image.open("temp/inverted.jpg")
detected.detectedText(image_file)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
ocr_result = pytesseract.image_to_string(img, lang='fra')
print(ocr_result)
file = open('data.txt', 'w')
file.write(ocr_result)
file.close()
