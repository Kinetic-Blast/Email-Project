import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the email data
emails = pd.read_csv('AI Training - Model\EmailData\Phishing_Email.csv')
emails = emails.dropna()

# Preprocess the text data
X = emails["Email Text"]
y = emails["Email Type"]

tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_tfidf = tfidf_vectorizer.fit_transform(X)

X_tfidf_dense = X_tfidf.toarray()

train_X, val_X, train_y, val_y = train_test_split(X_tfidf_dense, y, test_size=0.2, random_state=1)

label_encoder = LabelEncoder()
train_y = label_encoder.fit_transform(train_y)
val_y = label_encoder.transform(val_y)

input_shape = X_tfidf_dense.shape[1]
model = keras.Sequential([
    layers.Dense(units=512, activation='relu', input_shape=(input_shape,)),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(units=512, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(units=512, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(units=1, activation='sigmoid')  # Binary classification with sigmoid activation
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_X, train_y, epochs=10, batch_size=32, validation_data=(val_X, val_y))

# Evaluate the model
y_pred = (model.predict(val_X) > 0.5).astype(int)  # Convert probabilities to binary predictions
accuracy = accuracy_score(val_y, y_pred)
report = classification_report(val_y, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(report)


model.save('phishing_email_model.h5')