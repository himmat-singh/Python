import tensorflow as tf

#model parameters
W = tf.Variable([-1.0], tf.float32)
b = tf.Variable([1.0], tf.float32)

#inputs and outputs
x = tf.placeholder(tf.float32)

linear_model = W * x + b

y = tf.placeholder(tf.float32)


#loss
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)


init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

