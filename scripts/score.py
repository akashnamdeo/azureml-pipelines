import numpy as np
import pandas as pd
import xgboost as xgb
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Load the trained model
model = xgb.Booster()
model.load_model("model/model.xgb")  # Ensure correct path

app = FastAPI()

# Define request format
class InputData(BaseModel):
    data: List[List[float]]  # Ensure a 2D list (Matrix)

@app.post("/predict")
def predict(input_data: InputData):
    try:
        # Convert input to 2D DataFrame
        input_array = np.array(input_data.data)
        
        # Ensure input is 2D (needed for XGBoost)
        if input_array.ndim == 1:
            input_array = input_array.reshape(1, -1)

        # Convert to DMatrix
        dmatrix = xgb.DMatrix(input_array)

        # Predict
        predictions = model.predict(dmatrix)

        return {"admission_probability": predictions.tolist()}
    
    except Exception as e:
        return {"error": str(e)}
