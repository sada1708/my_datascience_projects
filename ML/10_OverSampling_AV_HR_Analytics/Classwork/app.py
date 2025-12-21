
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class Input(BaseModel):
  city : object
  city_development_index : float
  gender : object
  relevent_experience : object
  enrolled_university : object
  education_level : object
  major_discipline : object
  experience : object
  company_size : object
  company_type : object
  last_new_job : object
  training_hours : float

class Output(BaseModel):
  target : int

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/predict")
def predict(data : Input) -> Output:
  model = joblib.load('jobchg_pipeline_model.pkl')

  X_input = pd.DataFrame([[data.city, data.city_development_index, data.gender, data.relevent_experience, 
                          data.enrolled_university, data.education_level, data.major_discipline, data.experience, 
                          data.company_size, data.company_type, data.last_new_job, data.training_hours]])

  X_input.columns = [ 'city', 'city_development_index', 'gender',
       'relevent_experience', 'enrolled_university', 'education_level',
       'major_discipline', 'experience', 'company_size', 'company_type',
       'last_new_job', 'training_hours']

  #X_input = pd.DataFrame([Input.dict()])
  prediction = model.predict(X_input)
  print(prediction)
  return Output(target=prediction[0])
