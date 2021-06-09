import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

my_model = load_model("./cnn_mnist.hdf5")
img = cv2.imread("./test[6].jpg", cv2.IMREAD_GRAYSCALE)
img = 255 - img.copy()
test_data = img.reshape(1, 28, 28, 1) / 255

plt.imshow(img)
plt.show()

result = my_model.predict_classes(test_data)
print(result[0])