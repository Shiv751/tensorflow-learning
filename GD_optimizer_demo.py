import tensorflow as tf

weight = tf.Variable([3.0], dtype='float64')
bias = tf.Variable([6.7], dtype='float64')
input_x = tf.placeholder(tf.float64)
expected_y = tf.placeholder(tf.float64)

linear_regression = weight*input_x + bias
loss_function = tf.reduce_mean(tf.square(linear_regression - expected_y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss_function)
        
# training data
x_train = [1, 2, 3]
y_train = [9.7, 10.7, 15.7]

with tf.Session() as sess:
    initialization = sess.run(tf.global_variables_initializer())
    #iterating it 1000 times and each time gradient descent looks for local minima
    for i in range(1000):
        sess.run(train, {input_x: x_train, expected_y: y_train})

    # evaluate training accuracy
    curr_W, curr_b, curr_loss = sess.run([weight, bias, loss_function], {input_x: x_train, expected_y: y_train})
    print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))
