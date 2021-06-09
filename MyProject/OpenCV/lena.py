import cv2

src = cv2.imread('./data/lena.jpg')

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()