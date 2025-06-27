import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 1. Carregar o dataset (usando apenas as 10.000 palavras mais frequentes)
num_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# 2. Pré-processamento: padronizar o tamanho das sequências
maxlen = 200
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# 3. Criar o modelo
model = Sequential([
    Embedding(input_dim=num_words, output_dim=32, input_length=maxlen),
    GlobalAveragePooling1D(),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # saída binária
])

# 4. Compilar o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 5. Treinar o modelo
history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=512,
                    validation_split=0.2,
                    verbose=1)

# 6. Avaliar o modelo
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Acurácia nos dados de teste: {accuracy:.4f}")