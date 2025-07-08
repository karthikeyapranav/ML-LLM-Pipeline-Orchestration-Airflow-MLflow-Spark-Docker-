# # aip/model_handler.py


# from mlflow.pyfunc import load_model
# import joblib

# class ModelHandler:
#     def __init__(self):
#         try:
#             self.model = load_model("models:/wine_quality_model@production")
#             print("✅ Model loaded from registry (production).")
#         except Exception as e:
#             self.model = None
#             print("⚠️ No MLflow runs found. Model is not loaded.")
#             print(e)

#     def predict(self, input_data):
#         if self.model:
#             return self.model.predict(input_data)
#         else:
#             return ["Model not loaded"]
        
#     def load_model(self):
#         return joblib.load(self.model_path)  

# def predict_quality(model, features: dict):
#     import pandas as pd
#     df = pd.DataFrame([features])
#     prediction = model.predict(df)
#     return {"prediction": prediction.tolist()}
    

# import joblib
# import os
# import pandas as pd

# class ModelHandler:
#     def __init__(self):
#         self.model_path = os.path.join("models", "best_model.pkl")
#         self.model = self.load_model()

#     def load_model(self):
#         return joblib.load(self.model_path)

#     def predict(self, features: dict):
#         df = pd.DataFrame([features])
#         prediction = self.model.predict(df)
#         return {"prediction": prediction.tolist()}


# api/model_handler.py

import joblib
import os

class ModelHandler:
    def __init__(self):
        self.model_path = os.path.join("models", "best_model.pkl")
        self.model = self.load_model()

    def load_model(self):
        return joblib.load(self.model_path)

    def predict(self, df):
        return self.model.predict(df)

def predict_quality(model, features: dict):
    import pandas as pd
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
