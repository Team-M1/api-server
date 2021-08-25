import torch

from transformers import ElectraModel
from tokenizer import KoCharElectraTokenizer

from model import GRUNet

max_input_length = 172

pretrained_model = ElectraModel.from_pretrained("monologg/kocharelectra-small-discriminator")
tokenizer = KoCharElectraTokenizer.from_pretrained("monologg/kocharelectra-small-discriminator")

hidden_dim = 256
output_dim = 1
n_layers = 2
bidirectional = True
dropout = 0.2

model = GRUNet(pretrained_model, hidden_dim, output_dim, n_layers, bidirectional, dropout)
model.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu')))
model.eval()

def predict(text):
    tokens = tokenizer.tokenize(text)
    tokens = tokens[:max_input_length-2]
    indexed = tokenizer.convert_tokens_to_ids(tokens)
    tensor = torch.LongTensor(indexed)
    tensor = tensor.unsqueeze(0)
    prediction = torch.sigmoid(model(tensor))
    return prediction.item()
