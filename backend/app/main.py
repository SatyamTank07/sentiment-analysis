# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import SentimentModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
model = SentimentModel()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = model.predict(input.text)
    return result
