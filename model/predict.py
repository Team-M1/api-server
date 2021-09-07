import os
import pathlib
import torch
from transformers import ElectraForSequenceClassification, ElectraTokenizer

# kocharelectra tokenizer
# from tokenizer.tokenization_kocharelectra import KoCharElectraTokenizer

CURRENT_PATH = pathlib.Path().resolve()
MODEL_PATH = os.path.join(CURRENT_PATH, 'model/model')

model = ElectraForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = ElectraTokenizer.from_pretrained('monologg/koelectra-small-v3-discriminator')

def predict(text):
    with torch.no_grad():
        tokens = tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
        output = model(**tokens)
        return torch.argmax(output.logits, dim=1).item()
