import tensorflow as tf
import numpy as np

tf.enable_eager_execution()

X = np.array([                      # 2d data input as type of numpy, and element type is float32
            [0., 0.],               # tensorflow operates float
            [0., 1.],
            [1., 0.],
            [1., 1.]
], dtype="float32")

y = np.array([
            [0.],
            [0.],
            [0.],
            [1.]
], dtype="float32")

w = tf.Variable([[1], [2]], dtype="float32")          # make weight and initializing
b = tf.Variable([3], dtype="float32")

# tf.sigmoid(tf.matmul(X, w) + b)     # == np.dot(X, w) 벡터 내적연산

optimizer = tf.train.AdamOptimizer(0.01)    # activation func = adam

for step in range(5000):
    with tf.GradientTape() as tape:         # for IPC make tensorflow object
        hypothesis = tf.sigmoid(tf.matmul(X, w) + b)        # make hypothesis as output of sigmoid function

        cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
        grads = tape.gradient(cost, [w, b]) # gradient of cost function , variables are w0, w1, b

    optimizer.apply_gradients(grads_and_vars=zip(grads, [w, b]))  # Gradient Descent algorithm (method = adam)

    if step % 100 == 0:
        print("="*50)
        print("step: {}, cost: {}, w:{}, b:{}".format(step, cost.numpy(), w.numpy(), b.numpy()))
        print("="*50)