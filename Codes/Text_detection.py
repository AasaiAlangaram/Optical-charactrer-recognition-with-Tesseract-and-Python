import cv2
import pytesseract

#executable file location
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\aasai\\AppData\\Local\\Tesseract-OCR\\tesseract.exe' # Directory of tesseract.exe
#read image
img = cv2.imread("sample_1.png")
#convert our input image to rgb format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Original',img)

#############################################
#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])    # The indices of boxes 1,2,3,4 represents x,y,w,h of a character
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (5, 250, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(250,50,255),2)


##############################################
##### Detecting Words  ######
##############################################
# boxes = pytesseract.image_to_data(img)
# print(boxes)
# for a,b in enumerate(boxes.splitlines()):
#         print(b)
#         if a!=0:
#             b = b.split()
#             if len(b)==12:
#                 x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])      # The indices of boxes 6,7,8,9 represents x,y,w,h of a word
#                 cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
#                 cv2.rectangle(img, (x,y), (x+w, y+h), (50, 100, 255), 2)



cv2.imshow("Result", img)
cv2.waitKey(0)