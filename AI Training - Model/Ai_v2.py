import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec
import joblib

def train_model_and_save():
    # Load the email data
    emails = pd.read_csv('AI Training - Model/EmailData/Phishing_Email.csv')
    emails = emails.dropna()

    # Preprocess the text data
    X = emails["Email Text"]
    y = emails["Email Type"]

    # Tokenize text data
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X)
    X_seq = tokenizer.texts_to_sequences(X)
    X_padded = pad_sequences(X_seq, maxlen=100, padding='post')

    # Split data into training and validation sets
    train_X, val_X, train_y, val_y = train_test_split(X_padded, y, test_size=0.2, random_state=1)

    # Encode labels
    label_encoder = LabelEncoder()
    train_y = label_encoder.fit_transform(train_y)
    val_y = label_encoder.transform(val_y)

    # Load pre-trained Word2Vec embeddings
    word_vectors = Word2Vec(sentences=X, vector_size=100, window=5, min_count=1, workers=4)


    # Build embedding matrix
    embedding_matrix = np.zeros((len(tokenizer.word_index) + 1, 100))
    for word, i in tokenizer.word_index.items():
        if word in word_vectors.wv:
            embedding_matrix[i] = word_vectors.wv[word]

    # Build the CNN model
    model = keras.Sequential([
        layers.Embedding(len(tokenizer.word_index) + 1, 100, weights=[embedding_matrix], input_length=100, trainable=True),
        layers.Conv1D(256, 5, activation='relu'),
        layers.GlobalMaxPooling1D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    # Early stopping callback
    early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

    # Train the model
    model.fit(train_X, train_y, epochs=20, batch_size=32, validation_data=(val_X, val_y), callbacks=[early_stopping])

    # Evaluate the model
    y_pred = (model.predict(val_X) > 0.5).astype(int)
    accuracy = accuracy_score(val_y, y_pred)
    report = classification_report(val_y, y_pred)

    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(report)

    # Save the model
    model.save('AI Training - Model/phishing_email_model.h5')

    # Save the Tokenizer
    joblib.dump(tokenizer, 'AI Training - Model/tokenizer.pkl')

train_model_and_save()
