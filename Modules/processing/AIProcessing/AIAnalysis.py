import tensorflow as tf
import numpy as np
import joblib
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = tf.keras.models.load_model('AI Training - Model/phishing_email_model.h5')
tokenizer = joblib.load('AI Training - Model/tokenizer.pkl')

def ai_bodytext_analysis(input_text):
    # Tokenize input text
    input_sequence = tokenizer.texts_to_sequences([input_text])
    
    # Pad sequences to a fixed length (100 tokens)
    input_sequence_padded = pad_sequences(input_sequence, maxlen=100, padding='post')

    # Make predictions
    prediction = model.predict(input_sequence_padded)

    # Convert prediction probabilities to class labels
    predicted_class = "Phishing" if prediction[0][0] < 0.5 else "Legitimate"

    return predicted_class
