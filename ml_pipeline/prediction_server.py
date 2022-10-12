"""
run it with:

    uvicorn prediction_server:app --reload
"""
from fastapi import FastAPI
import numpy as np
import model_dummy
from pydantic import BaseModel


# intialize web server
app = FastAPI()


@app.get("/dice")   # URL suffix, URL path or endpoint
def roll_dice():
    """Rolls a die"""
    number = np.random.randint(1, 7)
    return {"dice_result": number}



class Item(BaseModel):
    gender: bool
    age: int
    income: float


@app.post("/predict")
def predict(item: Item):
    """uses the ML model"""
    df = [item]
    result = model_dummy.get_prediction(df)
    return {"probability": result}

