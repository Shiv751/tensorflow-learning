#Import TF
import tensorflow as tf 

#defining constants
x1 = tf.constant(5)
x2 = tf.constant(6)

#Performing operation
result = x1 * x2

#it will print the crude tensor
print(result)

#it will create a session and automatically close it after use
with tf.Session() as sess:
	print(sess.run(result))