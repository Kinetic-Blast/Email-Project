# Phishing Email Classification

This repository contains code for a machine learning model that classifies emails as either "phishing" or "non-phishing" (legitimate). It uses a neural network to process email text data and make binary classification predictions.

## Data Source

The dataset used for this project is obtained from Kaggle and is available in the "Phishing_Email.csv" file. It contains email text and their corresponding types (phishing or non-phishing).

## Preprocessing

- Text data is preprocessed using the TF-IDF vectorization technique.
- Label encoding is applied to convert the target labels into a suitable format for binary classification.

## Model

The neural network model is designed with multiple hidden layers and dropout layers for regularization. The final layer uses a sigmoid activation function for binary classification.

## Training

The model is trained for 10 epochs using the Adam optimizer and binary cross-entropy loss. Training and validation data are used to monitor the model's progress.

## Evaluation

After 10 epochs, the model achieved an accuracy of 0.9654 on the validation set.

