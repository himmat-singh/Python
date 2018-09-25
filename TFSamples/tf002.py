import tensorflow as tf

n1 = tf.placeholder(float)
n2 = tf.placeholder(float)

n3 = n1 * n2

with tf.Session() as sess:
    file_writer = tf.summary.FileWriter("D:\\pydump\\tfsamples\\graph",sess.graph)
    print(sess.run(n3, {n1:[1,2], n2:[2,5]}))