from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn
from model_dataPrep import data_prep

# 1. Initialize FastAPI app
app = FastAPI(title="HR Promotion Prediction API")

# 2. Load the Model Pipeline
# We load it globally so it stays in memory
try:
    model = joblib.load("hr_promotion_best_pipeline.pkl")
except Exception as e:
    print(f"Error loading model: {e}")

# 3. Define the Input Data Schema using Pydantic
# This ensures the API only accepts correctly formatted data
class EmployeeData(BaseModel):
    department: str
    region: str
    education: str
    gender: str
    recruitment_channel: str
    no_of_trainings: int
    age: int
    previous_year_rating: float
    length_of_service: int
    KPIs_met_80: int  # Use 0 or 1
    awards_won: int   # Use 0 or 1
    avg_training_score: int

@app.get("/")
def home():
    return {"message": "HR Promotion Prediction API is running. Use /predict endpoint."}

@app.post("/predict")
def predict(data: EmployeeData):
    try:
        # Convert Pydantic object to Dictionary, then to DataFrame
        # We must map the keys to match exactly what the Pipeline expects
        input_dict = {
            'department': data.department,
            'region': data.region,
            'education': data.education,
            'gender': data.gender,
            'recruitment_channel': data.recruitment_channel,
            'no_of_trainings': data.no_of_trainings,
            'age': data.age,
            'previous_year_rating': data.previous_year_rating,
            'length_of_service': data.length_of_service,
            'KPIs_met >80%': data.KPIs_met_80,  # Match column names from training
            'awards_won?': data.awards_won,      # Match column names from training
            'avg_training_score': data.avg_training_score
        }
        
        df = pd.DataFrame([input_dict])
        input_df = data_prep(df)
        
        # 4. Generate Prediction
        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0][1])
        
        return {
            "is_promoted": prediction,
            "promotion_probability": round(probability, 4),
            "status": "Success"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)