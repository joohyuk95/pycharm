import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data = [
        [2, 0, 81],
        [4, 4, 93],
        [6, 2, 91],
        [8, 3, 97]
]

x1 = [i[0] for i in data]
x2 = [i[1] for i in data]
y = [i[2] for i in data]
"""
plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
ax.dist = 10
ax.scatter(x1, x2, y)
plt.show()
"""

# 넘파이 배열로 바꾸면 원소별 연산이 가능
x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)

a1 = 0
a2 = 0
b = 0

lr = 0.05
epochs = 2021

for i in range(epochs):
    y_pred = a1 * x1_data + a2 * x2_data + b
    error = y_data - y_pred
    a1_diff = -(1/len(x1_data)) * sum(x1_data * (error))
    a2_diff = -(1/len(x2_data)) * sum(x2_data * (error))
    b_diff = -(1/len(x1_data)) * sum(error)

    a1 = a1 - lr * a1_diff
    a2 = a2 - lr * a2_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("epoch=%.f, 기울기1= %.04f, 기울기2= %.04f, 절편= %.04f" %(i, a1, a2, b))