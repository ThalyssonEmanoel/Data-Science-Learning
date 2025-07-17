from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
#fastapi dev api.py
app = FastAPI()

model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

class Penguin(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

@app.post("/predict")
def predict_penguin(p: Penguin):
    data = pd.DataFrame([{
        "bill_length_mm": p.bill_length_mm,
        "bill_depth_mm": p.bill_depth_mm,
        "flipper_length_mm": p.flipper_length_mm,
        "body_mass_g": p.body_mass_g,
    }])
    prediction = model.predict(data)[0]
    especie = encoder.inverse_transform([prediction])[0]
    return {"species": especie}