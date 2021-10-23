import cv2

img = cv2.imread('interior.png')


cv2.imshow('interior', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()