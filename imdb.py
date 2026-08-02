import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

num_words = 10000

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

max_len = 500

x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)

model = models.Sequential([
    layers.Embedding(input_dim=num_words, output_dim=64, input_length=max_len),
    layers.LSTM(64),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)

test_loss, test_acc = model.evaluate(x_test, y_test)

print(f"Test accuracy: {test_acc}")

new_review = [1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 4581, 66, 394, 2, 530, 973]

new_review = sequence.pad_sequences([new_review], maxlen=max_len)

prediction = model.predict(new_review)

print(f"Predicted sentiment: {'Positive' if prediction >= 0.5 else 'Negative'}")
