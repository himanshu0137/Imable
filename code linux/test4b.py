import cv2
import numpy as np

img = cv2.imread("tfi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Sobel(gray,cv2.CV_8U, 0, 1, ksize=5)
cv2.imwrite("edgesh.jpg", edges)
size = (1567, 3987)
bi = edges.copy()
#bi = np.zeros(size, dtype=np.uint8)
for i in xrange(size[0]):
    for j in xrange(size[1]):
        if edges[i][j] > 0:
            bi[i][j] = 255
        else:
            bi[i][j] = 0

cv2.imwrite("bih.jpg", bi)
th = 400
pos = []
for i in xrange(size[0]):
    longest = 0
    for j in xrange(size[1]-1):
        if bi[i][j+1] == 255:
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
with open("hline.txt", "w") as h:
    h.write(" ".join(map(str, lpos)))

_op = cv2.imread("op.jpg")
op = _op.copy()
for i in lpos:
    for j in xrange(size[1]):
        op[i, j] = [0, 0, 255]
        op[i+1, j] = [0, 0, 255]
        op[i-1, j] = [0, 0, 255]

cv2.imwrite("op.jpg", op)

