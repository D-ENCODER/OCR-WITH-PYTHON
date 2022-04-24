import pytesseract
import cv2
from gtts import gTTS
import os
img = cv2.imread('data/data.png')

img = cv2.resize(img, (600, 360))
hImg, wImg, _ = img.shape
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
boxes = pytesseract.image_to_boxes(img)
xy = pytesseract.image_to_string(img)
for b in boxes.splitlines():
    b = b.split(' ')

x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
cv2.putText(img, b[0], (x, hImg - y + 13),
            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

cv2.imshow('Detected text', img)

audio = gTTS(text=xy, lang='en', slow=False)
audio.save("saved_audio.wav")
os.system("saved_audio.wav")
