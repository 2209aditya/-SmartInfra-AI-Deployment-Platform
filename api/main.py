from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import time

app = FastAPI(title="SmartInfra ML API", version="1.0.0")

# Load trained model
with open("../model/model.pkl", "rb") as f:
    model = pickle.load(f)

class InputData(BaseModel):
    features: list

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": time.time(), "version": "1.0.0"}

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])[0]
    confidence = max(model.predict_proba([data.features])[0])
    return {
        "prediction": int(prediction),
        "confidence": float(confidence),
        "model_version": "v1.0.0",
        "processing_time_ms": 10
    }
