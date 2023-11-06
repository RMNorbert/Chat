import random
import json
import torch
from chatbot.model.model import NeuralNet
from chatbot.util.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('./chatbot/data/intents.json', 'r') as f:
    intents = json.load(f)

with open('./chatbot/data/catIntents.json', 'r') as f:
    cat_Intents = json.load(f)

FILE = "./chatbot/data/data.pth"
CAT_FILE = "./chatbot/data/cat.pth"
data = torch.load(FILE)
cat = torch.load(CAT_FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

cat_input_size = cat["input_size"]
cat_hidden_size = cat["hidden_size"]
cat_output_size = cat["output_size"]
cat_all_words = cat["all_words"]
cat_tags = cat["tags"]
cat_model_state = cat["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

cat_model = NeuralNet(cat_input_size, cat_hidden_size, cat_output_size).to(device)
cat_model.load_state_dict(model_state)
cat_model.eval()

bot_name = "DentoBot"


def get_response(msg, response_from_cat):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words if not response_from_cat else cat_all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    if not response_from_cat:
        output = model(X)
    else:
        output = cat_model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()] if not response_from_cat else cat_tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        if not response_from_cat:
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    return random.choice(intent["responses"])
        elif response_from_cat:
            for intent in cat_Intents["intents"]:
                if tag == intent["tag"]:
                    return random.choice(intent["responses"])

    return 'I do not understand...'

