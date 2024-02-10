import tensorflow as tf
import joblib

def load_model_and_predict(input_text):
    # Load the model
    model = tf.keras.models.load_model('AI Training - Model/phishing_email_model.h5')

    # Load the TF-IDF vectorizer
    tfidf_vectorizer = joblib.load('AI Training - Model/tfidf_vectorizer.pkl')

    # Transform the input text
    input_text_tfidf = tfidf_vectorizer.transform([input_text])

    # Reorder sparse matrix indices
    input_text_tfidf = input_text_tfidf.tocsr()  # Convert to CSR format
    input_text_tfidf.sort_indices()

    # Make predictions
    prediction = model.predict(input_text_tfidf)

    # Convert prediction probabilities to class labels
    predicted_class = "Phishing" if prediction[0][0] > 0.5 else "Legitimate"

    return predicted_class

input_text = "Dear Customer, your account has been compromised. Please click the link to reset your password."
prediction = load_model_and_predict(input_text)
print("Predicted class:", prediction)


