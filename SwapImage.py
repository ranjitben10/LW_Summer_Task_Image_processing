import cv2
import numpy as np

IronMan = cv2.imread("Iron-Man.jpg",cv2.IMREAD_UNCHANGED)
ChrisEvans = cv2.imread("Chris-Evans.jpg",cv2.IMREAD_UNCHANGED)
crop_iron_man = cv2.imread("croppedIron.jpg",cv2.IMREAD_UNCHANGED)
crop_chris_evans = cv2.imread("croppedCris.jpg",cv2.IMREAD_UNCHANGED)



cris_x1 = 320
cris_y1 = 50
cris_x2 = 520
cris_y2 = 300
# print(crop_iron_man.shape)
# # print(ChrisEvans.shape)
ChrisEvans[cris_y1:cris_y2,cris_x1:cris_x2] = crop_iron_man

iron_x1 = 320
iron_y1 = 50
iron_x2 = 520
iron_y2 = 300

IronMan[iron_y1:iron_y2,iron_x1:iron_x2] = crop_chris_evans




cv2.imshow("Before Swap: IRONMAN",IronMan)
cv2.imshow("Cropped IRONMAN",crop_iron_man)
cv2.imshow("Before Swap: ChrisEvans",ChrisEvans)
cv2.imshow("Cropped CHRISEVANS",crop_chris_evans)


cv2.imshow("After Swap: IRONMAN",IronMan)
cv2.imshow("After Swap: CHRISEVANS",ChrisEvans)
cv2.waitKey(0)
cv2.destroyAllWindows()