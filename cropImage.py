import cv2

image1 = cv2.imread("Chris-Evans.jpg",cv2.IMREAD_UNCHANGED)
image2 = cv2.imread("scene-Iron-Man.jpg",cv2.IMREAD_UNCHANGED)



scale_percent = 50  # percent of original size
width = int(image2.shape[1] * scale_percent / 100)
height = int(image2.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized_image2 = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

# cv2.imwrite("Iron-Man.jpg",resized_image2)

image1 = cv2.rectangle(image1,(320,50),(520,300),(255,0,0),10)

cris_x1 = 320
cris_y1 = 50
cris_x2 = 520
cris_y2 = 300

crop_image1 = image1[cris_y1:cris_y2,cris_x1:cris_x2]
# cv2.imwrite("croppedCris.jpg",crop_image1)



resized_image2 = cv2.rectangle(resized_image2,(340,40),(480,220),(255,0,0),10)

iron_x1 = 340
iron_y1 = 40
iron_x2 = 480
iron_y2 = 220

crop_image2 = resized_image2[40:220,340:480]
# cv2.imwrite("croppedIron.jpg",crop_image2)



# image1[cris_y1:cris_y2,cris_x1:cris_x2]=crop_image2


cv2.imshow("Image1",image1)
cv2.imshow("cropped cris image : image1",crop_image1)
cv2.imshow("Image2",resized_image2)
cv2.imshow("cropped ironman: resized_image2",crop_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()