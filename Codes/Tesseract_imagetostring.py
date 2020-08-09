import cv2
import pytesseract

#executable file location
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\aasai\\AppData\\Local\\Tesseract-OCR\\tesseract.exe' # Directory of tesseract.exe
#read image
img = cv2.imread("sample_1.png")
#convert our input image to rgb format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('Original',img)

print(pytesseract.image_to_string(img))

cv2.imshow('result', img)
cv2.waitKey(0)