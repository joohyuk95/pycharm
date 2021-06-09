import cv2


img = cv2.imread("C:\\Users\\user\\Desktop\\image.jpg")
img = img[20:, 90:550]  # from 480 X 640

img1 = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_AREA)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

out = img2.copy()
height, width = img2.shape
high = img2.max()
low = img2.min()

for i in range(width):
    for j in range(height):
        out[i][j] = ((img2[i][j] - low) * 255 / (high - low))


cv2.imwrite(f"C:\\Users\\user\\Desktop\\img_new.jpg", out)