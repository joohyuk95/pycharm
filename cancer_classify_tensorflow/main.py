from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
tf.enable_eager_execution()

data = datasets.load_breast_cancer()        # data read, which have data(x) and target(y)

X = data.data                               # x_data
X = np.array(X, dtype="float32")

y = data.target
y = np.array(y, dtype="float32")
y = y.reshape(-1, 1)                        # for matrix inner-product make target as column verctor

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    # split data as for training, test

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()   # object to normalize data
scaler.fit(X_train)    # calculate mean, standard deviation -> this should be done before normalizing
X_train = scaler.transform(X_train)

initializer = tf.contrib.layers.xavier_initializer()

w = tf.Variable(initializer([30, 1]))       # initializing variables
b = tf.Variable(initializer([1]))

optimizer = tf.train.AdamOptimizer(0.001)

for step in range(100):
    with tf.GradientTape() as tape:
        hypothesis = tf.sigmoid(tf.matmul(X_train, w) + b)

        cost = -tf.reduce_mean(y_train * tf.log(hypothesis) + (1 - y_train) * tf.log(1-hypothesis))
        grads = tape.gradient(cost, [w, b])

    optimizer.apply_gradients(grads_and_vars=zip(grads, [w, b]))

    if step % 10 == 0:
        print("="*50)
        print("step:{}, cost: {}, w:{}, b:{}".format(step, cost.numpy(), w.numpy(), b.numpy()))
        print("="*50)

X_test = scaler.transform(X_test)         # normalizing test data as mean and std of training data to evaluate our model
predict = tf.sigmoid(tf.matmul(X_test, w) + b)          # 학습한 모델로부터 나온 0~1 사이의 예측결과
predict01 = tf.cast(predict > 0.5, dtype=tf.float32)    # 분류 문제이므로 예측 결과로부터 0, 1 값으로 반환

ac01 = tf.equal(predict01, y_test)                      # binary 예측결과로부터 테스트 데이터와 비교하여 참, 거짓 데이터로 변환
ac02 = tf.cast(ac01, dtype="float32")                   # 비교 결과로부터 정확도 계산위해 다시 binary로 변환
ac03 = tf.reduce_mean(ac02)                             # 변환한 수치결과로부터 평균계산해서 정확도 출력

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict01, y_test), dtype=tf.float32))
print("="*20)
print("accuracy")
print(accuracy.numpy())