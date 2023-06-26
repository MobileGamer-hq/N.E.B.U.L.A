import json
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the JSON data
with open('data/intent_data.json', 'r') as file:
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

# Extract the text and labels from the DataFrame
train_texts = train_df['statement'].tolist()
train_labels = train_df['intent'].tolist()
test_texts = test_df['statement'].tolist()
test_labels = test_df['intent'].tolist()

# Transform the combined data using TfidfVectorizer
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(train_texts)
test_vectors = vectorizer.transform(test_texts)

classifier = LogisticRegression()
classifier.fit(train_vectors, train_labels)

predicted_labels = classifier.predict(test_vectors)

# Print classification report
print(classification_report(test_labels, predicted_labels))

predicted_labels = classifier.predict(test_vectors)
report = classification_report(test_labels, predicted_labels)
print("Classification Report:\n", report)

with open('models/intent_classifier_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)
# Save the vectorizer to disk
with open('models/intent_classifier_vectorizer_model.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)
