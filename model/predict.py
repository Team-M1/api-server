from typing import Dict, Union

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


async def predict(text: str) -> Dict[str, Union[int, float]]:
    """
    입력으로 들어온 텍스트를 예측하여 레이블과 스코어(확률)을 반환하는 함수
    args:
        text: str - 예측할 텍스트

    return:
        Dict[str, Union[int, float]]
    """
    with torch.no_grad():
        tokens = tokenizer(
            text, padding="max_length", truncation=True, return_tensors="pt"
        )
        output = model(**tokens)
        logits = output.logits
        pred = logits.argmax().item()
        score = logits.softmax(1).max().item()
    return {"label": pred, "score": score}
