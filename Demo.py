import tensorflow as tf

weight = tf.Variable([3.0], dtype='float64')
bias = tf.Variable([6.7], dtype='float64')
input_x = tf.placeholder(tf.float64)
expected_y = tf.placeholder(tf.float64)

linear_regression = weight*input_x + bias
squared_error = tf.square(linear_regression - expected_y)
loss_function = tf.reduce_mean(squared_error)

with tf.Session() as sess:
    initialization = sess.run(tf.global_variables_initializer())
    output_y = sess.run(linear_regression, {input_x: [1, 2, 3]})
    print('Output is :', output_y)

    loss = sess.run(loss_function, {input_x: [1, 2, 3], expected_y:[9.7, 12.7, 15.6]})
    print('Loss is :', loss*100, '%')

'''
TensorFlow provides optimizers that slowly change each variable in order to minimize 
the loss function. The simplest optimizer is gradient descent. It modifies each variable 
according to the magnitude of the derivative of loss with respect to that variable. 
In general, computing symbolic derivatives manually is tedious and error-prone. 
Consequently, TensorFlow can automatically produce derivatives given only a description 
of the model using the function tf.gradients
'''