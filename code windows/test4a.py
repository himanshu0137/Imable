import cv2
import numpy as np

img = cv2.imread("tfi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Sobel(gray,cv2.CV_8U, 1, 0, ksize=5)
cv2.imwrite("edgesv.jpg", edges)
size = (1877, 1906)
bi = edges.copy()
#bi = np.zeros(size, dtype=np.uint8)
for i in xrange(size[0]):
    for j in xrange(size[1]):
        if edges[i][j] > 0:
            bi[i][j] = 255
        else:
            bi[i][j] = 0

cv2.imwrite("biv.jpg", bi)
th = 400
pos = []
for i in xrange(size[1]):
    longest = 0
    for j in xrange(size[0]-1):
        if bi[j+1][i] == 255:
            longest += 1
        else:
            if longest > th:
                pos.append(i)
                break

lpos = []
i = 1
while(i < len(pos)-1):
    if pos[i+1]-pos[i] > 50:
        lpos.append(pos[i])
    i += 1
lpos.append(pos[-1])

_op = cv2.imread("cii.jpg")
op = _op.copy()
for i in lpos:
    for j in xrange(size[0]):
        op[j, i] = [0, 0, 255]
        op[j, i+1] = [0, 0, 255]
        op[j, i-1] = [0, 0, 255]

cv2.imwrite("op.jpg", op)

