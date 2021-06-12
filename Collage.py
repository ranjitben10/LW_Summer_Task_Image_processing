import cv2
import numpy as np

image1 = cv2.imread("Chris-Evans.jpg")
image2 = cv2.imread("Iron-Man.jpg")


cris_x1 = 320
cris_y1 = 50
cris_x2 = 520
cris_y2 = 300
crop_image1 = image1[cris_y1:cris_y2,cris_x1:cris_x2]

iron_x1 = 320
iron_y1 = 50
iron_x2 = 520
iron_y2 = 300
crop_image2 = image2[iron_y1:iron_y2,iron_x1:iron_x2]

collage = np.hstack((crop_image1,crop_image2))
cv2.imshow("Collage",collage)
cv2.waitKey(0)
cv2.destroyAllWindows()