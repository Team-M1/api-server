import pathlib
import torch
from transformers import ElectraForSequenceClassification, ElectraTokenizer

# kocharelectra tokenizer
# from tokenizer.tokenization_kocharelectra import KoCharElectraTokenizer

CURRENT_PATH = pathlib.Path().resolve()
MODEL_PATH = CURRENT_PATH / "model/model"

model = ElectraForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-small-v3-discriminator")
model.eval()


def predict(text: str):
    with torch.no_grad():
        tokens = tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
        output = model(**tokens)
        logits = output.logits
        pred = logits.argmax().item()
        score = logits.softmax(1).max().item()
        return {"label": pred, "score": score}
