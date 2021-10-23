import cv2

img = cv2.imread('interior.png')


img2 = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow('interior', img2)
cv2.waitKey(0) 
cv2.destroyAllWindows()