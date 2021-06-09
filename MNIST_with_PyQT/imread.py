import cv2
import matplotlib.pyplot as plt

img0 = cv2.imread("./test[6].jpg")
img1 = cv2.imread("./test[6].jpg", cv2.IMREAD_GRAYSCALE)
img2 = 255 - img1.copy()
img3 = img2.copy()

rows = 2
cols = 2

imgs = []
imgs.append(img0)
imgs.append(img1)
imgs.append(img2)
imgs.append(img3)

axes = []
fig = plt.figure()

for i in range(rows*cols):
    axes.append(fig.add_subplot(rows, cols, i+1))

    if i == 3:
        plt.imshow(imgs[i], cmap="Greys")
    else:
        plt.imshow(imgs[i], cmap="gray")

axes[0].set_title("original")
axes[1].set_title("gray")
axes[2].set_title("reverse & gray")
axes[3].set_title("reverse & Greys")

fig.tight_layout()
plt.show()