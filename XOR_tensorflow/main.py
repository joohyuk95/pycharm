import numpy as np
import tensorflow as tf
tf.enable_eager_execution()

X = np.array([
            [0., 0.],
            [0., 1.],
            [1., 0.],
            [1., 1.]
], dtype="float32")

y = np.array([
            [0.],
            [1.],
            [1.],
            [0.]
], dtype="float32")

w0 = tf.Variable([[1, 2], [3, 4]], dtype="float32")
b0 = tf.Variable([0, 0], dtype="float32")

w1 = tf.Variable([[5], [6]], dtype="float32")
b1 = tf.Variable([0], dtype="float32")

optimizer = tf.train.AdamOptimizer(0.1)

for step in range(5000):
    with tf.GradientTape() as tape:
        hypothesis0 = tf.sigmoid(tf.matmul(X, w0) + b0)
        hypothesis1 = tf.sigmoid(tf.matmul(hypothesis0, w1) + b1)

        cost = -tf.reduce_mean(y * tf.log(hypothesis1) + (1 - y) * tf.log(1 - hypothesis1))
        grads = tape.gradient(cost, [w0, w1, b0, b1])

        optimizer.apply_gradients(grads_and_vars=zip(grads, [w0, w1, b0, b1]))

        if step % 500 == 0:
            print("cost:{}, w0:{}, w1:{}".format(cost, w0, w1))

hypothesis0 = tf.sigmoid(tf.matmul(X, w0) + b0)
predict = tf.sigmoid(tf.matmul(hypothesis0, w1) + b1)
predict01 = tf.cast(predict > 0.5, dtype="float32")

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict01, y), dtype="float32"))

print("="*20)
print("accuracy")
print(accuracy.numpy())
