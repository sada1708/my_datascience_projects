from fastapi import FastAPI
from pydantic import BaseModel 
import pandas as pd
import joblib
from pathlib import Path  


app = FastAPI(title = 'Job Look Prediction API')

# --- 1. Load the Model ONCE at startup (Outside the function) ---
# This keeps the model in memory, making predictions nearly instant.

CURRENT_DIR = Path(__file__).parent
MODEL_PATH = CURRENT_DIR / 'jobchg_pipeline_model.pkl'  # Fixed quotes

model = None
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f'Error loading model: {e}')

class PredictionInput(BaseModel):
    city: str
    city_development_index: float
    gender: str
    relevent_experience: str
    enrolled_university: str
    education_level: str
    major_discipline: str
    experience: str
    company_size: str
    company_type: str  # Fixed typo 'trype'
    last_new_job: str
    training_hours: float

class PredictionOutput(BaseModel):
    target: int  # Fixed typo 'terget'

@app.get('/')
def health_check():
    return {'status': 'online', 'message': 'Model is loaded and ready.'}

@app.post('/predict', response_model=PredictionOutput)
def predict(data: PredictionInput):
    if model is None:
        return {"error": "Model not loaded"}
    
    # Convert Pydantic object to DataFrame
    input_dict = data.model_dump() 
    X_input = pd.DataFrame([input_dict])
    prediction = model.predict(X_input)
    print(prediction)
    return PredictionOutput(target = int(prediction[0]))




