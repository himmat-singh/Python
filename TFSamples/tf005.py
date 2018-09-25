import tensorflow as tf

#model parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

#inputs and outputs
x = tf.placeholder(tf.float32)

linear_model = W * x + b


y = tf.placeholder(tf.float32)


#loss
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)


optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train, {x:[-1,-2,-3,-4], y:[0,-100.0,-200.0,-300.0]})
    
    print(sess.run([W,b]))