import numpy as np
import cv2
from os import system

with open("vline.txt", "r") as v:
    vline = map(int, v.read().split())
with open("hline.txt", "r") as h:
    hline = map(int, h.read().split())
op = cv2.imread("tfi.jpg")


opa = []
for i in xrange(len(vline)-1):
    row = []
    for j in xrange(len(hline)-1):
        cv2.imwrite("cell.jpg", op[hline[j]:hline[j+1], vline[i]:vline[i+1]])
        system("tesseract cell.jpg -psm 10 out digits")
        with open("out.txt", "r") as o:
            l = o.read().strip()
            if l != '':
                row.append(l)
            else:
                row.append(" ")
    opa.append(row)
        #cv2.imwrite("cell{}-{}.jpg".format(i, j), op[hline[j]:hline[j+1], vline[i]:vline[i+1]])
for i in opa:
    print i
