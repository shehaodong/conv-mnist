import cv2
photo = cv2.imread('C://timg.jpg')
cv2.imshow('input_image', photo)
cv2.waitKey(0)
h, w = photo.shape[:2]
center = (h//2, w//2)
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(photo, M, (w, h))
cv2.imshow('rotated_image', rotated)
cv2.waitKey(0)
sfan = cv2.flip(photo, 1)
cv2.imshow('fliped_image', sfan)
cv2.waitKey(0) 