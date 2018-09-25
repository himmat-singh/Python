import tensorflow as tf

W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
x = tf.placeholder(tf.float32)

linear_model = W * x + b

init = tf.global_variables_initializer()

with tf.Session() as sess:
    file_writer = tf.summary.FileWriter("D://pydump//tfsamples//graph",sess.graph)
    print(sess.run(init))
    for n in range(10):
        print(sess.run(linear_model,{x:[n+1,n+2,n+3,n+4]}))