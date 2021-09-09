import torch
from transformers import ElectraForSequenceClassification

# kocharelectra tokenizer
from model.tokenizer import KoCharElectraTokenizer

MODEL_PATH = "./model/model"

model = ElectraForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = KoCharElectraTokenizer.from_pretrained(
    "monologg/kocharelectra-small-discriminator", model_max_length=512
)
model.eval()


async def predict(text: str):
    with torch.no_grad():
        tokens = tokenizer(
            text, padding="max_length", truncation=True, return_tensors="pt"
        )
        output = model(**tokens)
        logits = output.logits
        pred = logits.argmax().item()
        score = logits.softmax(1).max().item()
        return {"label": pred, "score": score}
