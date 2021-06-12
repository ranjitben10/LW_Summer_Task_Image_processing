import cv2
import numpy as np

image = np.zeros((612,612,3))

image = cv2.circle(image,(290,310),110,(255,0,0),10)
# image = cv2.circle(image,(194,320),91,(255,0,0),10)
image = cv2.circle(image,(390,130),61,(255,0,0),11)

image = cv2.line(image,(440,270),(450,430),(255,0,0),10)
image = cv2.line(image,(250,170),(90,250),(255,0,0),10)
# image[612][200] = (0,255,0)
for i in range(540,600):
    for j in range(610):
        image[i][j] = (0,255,0)


for i in range(1,612):
    for j in range(1,612):
        if i%j == 0:
            image[i][j] = (36,88,179)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Created Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()