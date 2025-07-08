# # # api/main.py

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd
# from api.model_handler import ModelHandler

# # Dummy ModelHandler stub for illustration, replace with your actual one
# class ModelHandler:
#     def __init__(self):
#         # Load your real model here
#         # For demo, just do nothing
#         pass
    
#     def predict(self, df: pd.DataFrame):
#         # Replace this with your actual model inference
#         # For demo, return a dummy prediction list
#         print("ModelHandler received DataFrame:")
#         print(df)
#         return ["good"]  # dummy prediction

# app = FastAPI()
# model_handler = ModelHandler()

# # Map API input names to your model's expected column names
# column_mapping = {
#     "fixed_acidity": "fixed acidity",
#     "volatile_acidity": "volatile acidity",
#     "citric_acid": "citric acid",
#     "residual_sugar": "residual sugar",
#     "chlorides": "chlorides",
#     "free_sulfur_dioxide": "free sulfur dioxide",
#     "total_sulfur_dioxide": "total sulfur dioxide",
#     "density": "density",
#     "pH": "pH",
#     "sulphates": "sulphates",
#     "alcohol": "alcohol"
# }

# class WineData(BaseModel):
#     fixed_acidity: float
#     volatile_acidity: float
#     citric_acid: float
#     residual_sugar: float
#     chlorides: float
#     free_sulfur_dioxide: float
#     total_sulfur_dioxide: float
#     density: float
#     pH: float
#     sulphates: float
#     alcohol: float

# @app.get("/")
# def read_root():
#     return {"message": "Wine Quality Prediction API is running"}

# @app.post("/predict")
# def predict(data: WineData):
#     try:
#         # Convert input to dict, then remap keys to model columns
#         input_dict = data.dict()
#         formatted_input = {column_mapping[k]: v for k, v in input_dict.items()}
        
#         # Create DataFrame in the exact format model expects
#         df = pd.DataFrame([formatted_input])
        
#         print("Input DataFrame for prediction:")
#         print(df)
        
#         # Run prediction
#         prediction = model_handler.predict(df)
        
#         print("Prediction result:", prediction)
        
#         # Return first prediction as JSON response
#         return {"prediction": prediction[0]}
    
#     except Exception as e:
#         print("Prediction error:", e)
#         raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# @app.get("/reload-model")
# def reload_model():
#     global model_handler
#     model_handler = ModelHandler()
#     return {"message": "🔄 Model reloaded from registry."}


# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# from api.model_handler import ModelHandler
# from api import app


# app = FastAPI()
# model_handler = ModelHandler()

# class WineFeatures(BaseModel):
#     fixed_acidity: float
#     volatile_acidity: float
#     citric_acid: float
#     residual_sugar: float
#     chlorides: float
#     free_sulfur_dioxide: float
#     total_sulfur_dioxide: float
#     density: float
#     pH: float
#     sulphates: float
#     alcohol: float

# @app.post("/predict")
# def predict(data: WineFeatures):
#     df = pd.DataFrame([data.dict()])
#     prediction = model_handler.predict(df)
#     return {"prediction": prediction[0]}

# @app.get("/")
# def home():
#     return {"message": "Wine Quality API running"}

# @app.get("/reload-model")
# def reload_model():
#     global model_handler
#     model_handler = ModelHandler()
#     return {"message": "🔄 Model reloaded from registry."}



# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import traceback

from .model_wrapper import model

app = FastAPI()

class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/")
def home():
    return {"message": "Wine Quality API running"}

@app.post("/predict/")
def predict(data: WineInput):
    try:
        input_data = np.array([[  # nested list to represent 2D shape (1 sample, 11 features)
            data.fixed_acidity,
            data.volatile_acidity,
            data.citric_acid,
            data.residual_sugar,
            data.chlorides,
            data.free_sulfur_dioxide,
            data.total_sulfur_dioxide,
            data.density,
            data.pH,
            data.sulphates,
            data.alcohol
        ]])
        prediction = model.predict(input_data)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
