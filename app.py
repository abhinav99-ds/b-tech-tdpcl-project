# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from optimizer import optimize

app = FastAPI()

# ✅ Check BEFORE loading model
MODEL_PATH = "fuel_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise Exception("Model not found! Run model.py first.")

model = joblib.load(MODEL_PATH)

# ✅ Proper request schema
class FlightInput(BaseModel):
    altitude: int
    speed: int
    temperature: int
    weight: int

@app.get("/")
def home():
    return {"message": "Fuel Optimization API running"}

@app.post("/predict")
def predict(data: FlightInput):
    try:
        features = [[
            data.altitude,
            data.speed,
            data.temperature,
            data.weight
        ]]

        fuel = model.predict(features)[0]
        recommendation = optimize(data.dict())

        return {
            "predicted_fuel": float(fuel),
            "optimized_params": recommendation
        }

    except Exception as e:
        return {"error": str(e)}