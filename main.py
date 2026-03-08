from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Initialize API
app = FastAPI(title="Spam Detection API")

# Load trained model
model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Request format
class EmailRequest(BaseModel):
    message: str


# Root route
@app.get("/")
def home():
    return {"message": "Spam Detection API Running"}


# Prediction route
@app.post("/predict")
def predict_spam(data: EmailRequest):

    # Convert text to vector
    vector = vectorizer.transform([data.message])

    # Predict
    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "Spam"
    else:
        result = "Not Spam"

    return {
        "message": data.message,
        "prediction": result
    }
