# model.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

MODEL_PATH = "/model/bert-imdb-classification"


class SentimentModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
        self.model.eval()  # Inference mode

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)
            prob_value, pred_class = torch.max(probs, dim=1)

        label = "Positive" if pred_class.item() == 1 else "Negative"
        probability = prob_value.item()

        return {
            "label": label,
            "probability": round(probability * 100, 2)  # in percentage
        }
