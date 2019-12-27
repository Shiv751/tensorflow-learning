import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np


class myCallback(tf.keras.callbacks.Callback):
    """ In it, we'll implement the on_epoch_end function, which gets called by the callback whenever the epoch ends.
    It also sends a logs object which contains lots of great information about the current state of training """

    def on_epoch_end(self, epoch, logs={}):
        if logs.get('loss') < 0.27:
            print("\nReached {}% accuracy so cancelling training!".format(round(logs.get('accuracy') * 100, 2)))
            self.model.stop_training = True


fashion_mnist_dataset = tf.keras.datasets.fashion_mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = fashion_mnist_dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

img = test_images[0]
plt.imshow(img)
plt.show()
print("Shape: X", img.shape[0])
print("Shape: Y", img.shape[1])
print("Size of image: {} bytes".format(img.shape[0] * img.shape[1]))
print(class_names[test_labels[0]])

train_images = train_images / 255.0
test_images = test_images / 255.0

cb = myCallback()


def mnist_model(p_on, t_images, t_labels):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x=t_images, y=t_labels, epochs=10, callbacks=[cb])
    # print("Evaluating the model -----------------------------------")
    # model.evaluate(test_images, test_labels)
    return model.predict(p_on)


prediction_on = test_images
pred = mnist_model(prediction_on, train_images, train_labels)
print("Pred - ", np.argmax(pred[0]))
