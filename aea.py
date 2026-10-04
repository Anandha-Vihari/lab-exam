import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

print("Libraries imported successfully")

# Load MNIST dataset
(x_train, _), (x_test, _) = mnist.load_data()

# Normalize pixel values
x_train = x_train.astype("float32") / 255.
x_test = x_test.astype("float32") / 255.

# Flatten the images
x_train = x_train.reshape((len(x_train),
                           np.prod(x_train.shape[1:])))

x_test = x_test.reshape((len(x_test),
                         np.prod(x_test.shape[1:])))

print(f"x_train shape: {x_train.shape}")
print(f"x_test shape: {x_test.shape}")

# Encoding dimension
encoding_dim = 32

# Input layer
input_img = Input(shape=(784,))

# Encoder
encoded = Dense(
    encoding_dim,
    activation='relu'
)(input_img)

# Decoder
decoded = Dense(
    784,
    activation='sigmoid'
)(encoded)

# Autoencoder model
autoencoder = Model(input_img, decoded)

# Encoder model
encoder = Model(input_img, encoded)

# Decoder model
encoded_input = Input(shape=(encoding_dim,))

decoder_layer = autoencoder.layers[-1]

decoder = Model(
    encoded_input,
    decoder_layer(encoded_input)
)

# Display model summary
autoencoder.summary()

# Compile model
autoencoder.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy'
)

# Train autoencoder
history = autoencoder.fit(
    x_train,
    x_train,
    epochs=50,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test)
)

# Plot training and validation loss
plt.figure(figsize=(10, 6))

plt.plot(
    history.history['loss'],
    label='Training Loss'
)

plt.plot(
    history.history['val_loss'],
    label='Validation Loss'
)

plt.title('Autoencoder Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# Encode and decode test images
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

# Display original and reconstructed images
n = 10

plt.figure(figsize=(20, 4))

for i in range(n):

    # Original image
    ax = plt.subplot(2, n, i + 1)

    plt.imshow(
        x_test[i].reshape(28, 28)
    )

    plt.gray()

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    if i == 0:
        ax.set_title("Original")

    # Reconstructed image
    ax = plt.subplot(2, n, i + 1 + n)

    plt.imshow(
        decoded_imgs[i].reshape(28, 28)
    )

    plt.gray()

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    if i == 0:
        ax.set_title("Reconstructed")

plt.show()

print("Autoencoder demonstration complete!")
