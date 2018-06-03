import cv2
import numpy as np

#cleaning image
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
#gray = cv2.Canny(gray,80,80)
gaussian = cv2.GaussianBlur(gray, (11, 11), 0)
thresh = cv2.adaptiveThreshold(gaussian, 255, 0, 1, 13, 4)
kernel = np.ones((5,5), np.uint8)
#kernel = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.uint8)
thresh = cv2.dilate(thresh, kernel)
cv2.imwrite("rr.jpg", thresh)

#Finding table
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
biggest = None
max_area = 0
for i in contours:
    area = cv2.contourArea(i)
    if area > max_area:
        max_area = area
        biggest = i
x, y, w, h = cv2.boundingRect(biggest)
table_img = thresh[y: y + h, x: x + w]
cv2.imwrite("ti.jpg",table_img)

#cutting table in original image
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
peri = cv2.arcLength(biggest, True)
approx = cv2.approxPolyDP(biggest, 0.02*peri, True)
cv2.drawContours(img, [approx], 0, (0, 255, 0), 2, cv2.CV_AA)
cv2.imwrite("ii.jpg", img)
cv2.imwrite("cii.jpg", img[y: y + h, x: x + w])
cv2.imwrite("tfi.jpg", cv2.imread("rr.jpg")[y: y + h, x: x + w])
