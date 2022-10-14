"""
The REST API server for inference
needs to run on a different port as the data source.

Start the server with:

    uvicorn prediction_server:app --reload --port 8001

"""
import pickle

from fastapi import FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


# intialize web server
app = FastAPI()


@app.get("/dice")  # URL suffix, URL path or endpoint
def roll_dice():
    """Rolls a die"""
    number = np.random.randint(1, 7)
    return {"dice_result": number}


class Item(BaseModel):
    gender: int
    age: int
    year: int
    age_of_car_M: int
    Car_power_M: float
    Car_2ndDriver_M: int
    num_policiesC: int
    metro_code: int
    Policy_PaymentMethodA: int
    Policy_PaymentMethodH: int
    Insuredcapital_content_re: float
    Insuredcapital_continent_re: float
    appartment: int
    Client_Seniority: float
    Retention: int


@app.post("/predict")
def predict(item: Item):
    """uses the ML model to make a prediction for a single data point"""
    model = pickle.load(open("model.pkl", "rb"))
    Xpred = pd.DataFrame([jsonable_encoder(item)])
    model.predict(Xpred)
    ypred = model.predict(Xpred).tolist()[0]
    return {"prediction result": ypred}
