import json
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm import MLE, NgramCounter
from nltk.util import bigrams, ngrams


def get_data():
    # Load the JSON data
    with open('data/intent_data.json', 'r') as file:
        data = json.load(file)

    intents = []
    statements = []
    responses = []

    for item in data:
        intent = item['intent']
        statement = item['statement']

        if item.get('responses') is not None:
            for response in item.get('responses'):
                intents.append(intent)
                statements.append(statement)
                responses.append(response)
        else:
            response = item['response']

            intents.append(intent)
            statements.append(statement)
            responses.append(response)

    new_data = []
    for i in range(len(intents)):
        obj = {
            "intent": intents[i],
            "statement": statements[i],
            "response": responses[i]
        }
        new_data.append(obj)
    else:
        print('done reorganizing dataset')
    return new_data, intents, statements, responses


data, intents, statements, responses = get_data()

training_data = []
for i in range(len(data)):
    statement = data[i]['statement']
    response = data[i]['response']
    training_data.append((statement, response))


# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess the input text


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()
              and token not in stop_words]
    return tokens

# Generate a response based on the trained language model
def generate_response(model, context, num_words=10):
    context_tokens = preprocess_text(context)
    context_tokens = list(ngrams(pad_both_ends(context_tokens, n=2), 2))
    response_tokens = []

    if not context_tokens:
        return "I'm sorry, but I don't have enough information to generate a response."

    for _ in range(num_words):
        word = model.generate(1, context_tokens)[-1][0]
        response_tokens.append(word)
        context_tokens = context_tokens[1:] + [(context_tokens[-1][-1], word)]

    response = ' '.join(response_tokens)
    return response

# Train the language model
def train_language_model(training_data):
    tokenized_data = [
        [preprocess_text(context), preprocess_text(response)]
        for context, response in training_data
    ]

    ngrams_data = [ngrams(tokens, 2) for tokens in tokenized_data]
    flatten_data = [token for sublist in ngrams_data for token in sublist]

    model = MLE(2)
    model.fit([flatten_data], vocabulary_text=training_data)
    return model


model = train_language_model(training_data)

while True:
    user_input = input("User: ")
    response = generate_response(model, user_input, num_words=10)
    print("Bot:", response)
