import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")


ret, frame = cam.read()
cv2.imshow("test", frame)
    
img_name = "img.png"
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))

cam.release()

cv2.destroyAllWindows()