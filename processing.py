import cv2
import glob

images = glob.glob('*.jpg')

for image in images:
    img = cv2.imread(image)
    re = cv2.resize(img, (100, 100))
    cv2.imwrite('resized_'+image,re)
    cv2.imshow('image', re)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()