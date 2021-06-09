import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.enable_eager_execution()
print(tf.__version__)

X = np.array([1, 2, 3], dtype="float32")
Y = np.array([2, 2.5, 3.5], dtype="float32")

W = tf.Variable([2], dtype="float32")
b = tf.Variable([1], dtype="float32")

print(W)
print(b)

learning_rate = 0.1

for i in range(1000):
    with tf.GradientTape() as tape:
        hypothesis = W * X + b
        print("hypothesis", hypothesis)

        cost = tf.reduce_mean(tf.square(hypothesis - Y))


    W_grad, b_grad = tape.gradient(cost, [W, b])
    print("W_grad:", W_grad, "b_grad", b_grad)

    W.assign_sub(W_grad * learning_rate)
    b.assign_sub(b_grad * learning_rate)
