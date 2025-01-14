import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

MODEL_FILE = 'trained_model.pkl'
VECTORIZER_FILE = 'vectorizer.pkl'

def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

def preprocess_data(data):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Speech'])
    y = data['Intent']
    return X, y, vectorizer

def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model

def save_model(model, vectorizer):
    joblib.dump(model, MODEL_FILE)
    joblib.dump(vectorizer, VECTORIZER_FILE)

def load_model_and_vectorizer():
    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)
    return model, vectorizer

def predict_category(phrase):
    model, vectorizer = load_model_and_vectorizer()
    input_vector = vectorizer.transform([phrase])
    prediction = model.predict(input_vector)
    return prediction[0]

if __name__ == "__main__":
    dataset_path = 'Dataset.csv'
    
    data = load_data(dataset_path)
    X, y, vectorizer = preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    save_model(model, vectorizer)

    test_phrase = "What is the weather today?"
    print(f"Predicted Category: {predict_category(test_phrase)}")