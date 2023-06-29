import json
import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


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

    return new_data


# Create a DataFrame from the JSON data
df = pd.DataFrame(get_data())
print(df)
df.to_csv('data/intent_data.csv')

classifier_path = 'models/intent_classifier_model.pkl'
vectorizer_path = 'models/intent_classifier_vectorizer_model.pkl'

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Extract the text and labels from the DataFrame
train_texts = train_df['statement'].tolist()
train_labels = train_df['intent'].tolist()
test_texts = test_df['statement'].tolist()
test_labels = test_df['intent'].tolist()

if os.path.exists(classifier_path):
    # Load the vectorizer from disk
    with open('models/intent_classifier_vectorizer_model.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    # Load the classifier from disk
    with open('models/intent_classifier_model.pkl', 'rb') as file:
        classifier = pickle.load(file)

    print("Retraining Model")

    train_vectors = vectorizer.fit_transform(train_texts)
    test_vectors = vectorizer.transform(test_texts)

    classifier.fit(train_vectors, train_labels)

    predicted_labels = classifier.predict(test_vectors)
    report = classification_report(test_labels, predicted_labels)
    print("Classification Report:\n", report)

else:
    # Transform the combined data using TfidfVectorizer
    vectorizer = TfidfVectorizer()
    train_vectors = vectorizer.fit_transform(train_texts)
    test_vectors = vectorizer.transform(test_texts)

    classifier = LogisticRegression()
    classifier.fit(train_vectors, train_labels)

    predicted_labels = classifier.predict(test_vectors)
    report = classification_report(test_labels, predicted_labels)
    print("Classification Report:\n", report)

    # Save the classifier to disk
    with open(classifier_path, 'wb') as file:
        pickle.dump(classifier, file)

    # Save the vectorizer to disk
    with open(vectorizer_path, 'wb') as file:
        pickle.dump(vectorizer, file)
