import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)

node2 = tf.constant(4.0, tf.float32)

node3 = node1 * node2 * 5

with tf.Session() as sess:
    File_Writer = tf.summary.FileWriter('D:\\PYDump\\TFSamples\\graph',sess.graph)
    print(sess.run(node3))

