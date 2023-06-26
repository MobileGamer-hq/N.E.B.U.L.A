import json
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the JSON data
with open('intent_data.json', 'r') as file:
    data = json.load(file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# # Split the data into training and testing sets
# train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# # Extract the text and labels from the DataFrame
# train_texts = train_df['text'].tolist()
# train_labels = train_df['intent'].tolist()
# test_texts = test_df['text'].tolist()
# test_labels = test_df['intent'].tolist()

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Extract the text, entities, and labels from the DataFrame
train_texts = train_df['text'].tolist()
train_entities = train_df['entities'].tolist()
train_labels = train_df['intent'].tolist()
test_texts = test_df['text'].tolist()
test_entities = test_df['entities'].tolist()
test_labels = test_df['intent'].tolist()

# Combine text and entities for training
train_data = [' '.join([text] + [entity['value'] for entity in entities])
              for text, entities in zip(train_texts, train_entities)]

# Combine text and entities for testing
test_data = [' '.join([text] + [entity['value'] for entity in entities])
             for text, entities in zip(test_texts, test_entities)]

# Transform the combined data using TfidfVectorizer
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(train_data)
test_vectors = vectorizer.transform(test_data)

classifier = LogisticRegression()
classifier.fit(train_vectors, train_labels)

predicted_labels = classifier.predict(test_vectors)

# Print classification report
print(classification_report(test_labels, predicted_labels))

predicted_labels = classifier.predict(test_vectors)
report = classification_report(test_labels, predicted_labels)
print("Classification Report:\n", report)

with open('classifier_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

    
