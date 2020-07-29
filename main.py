import cv2
import numpy as np


a= np.array([356,256])
b= np.array([256,256])
c= np.array([256,156])
ba = a - b
bc = c - b
for row in range(100):
    img = np.zeros([512, 512])
    c+=1
    ba = a - b
    bc = c - b
    cv2.line(img, tuple(b), tuple(a), (255),3)
    cv2.line(img,tuple(b), tuple(c), (255),3)
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    degres = np.degrees(angle)
    cv2.ellipse(img, (256, 256), (100, 100), 1, 1, -degres, (255))
    cv2.putText(img, str(int(degres)), (225, 256), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255), 1)
    cv2.imshow('Output Window', img)
    if cv2.waitKey(240)==27:
        break
cv2.destroyAllWindows()
