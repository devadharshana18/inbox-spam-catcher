import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib

# Sample data
data = {
    'text': [
        'Congratulations! You have won a lottery.',
        'Your order has been shipped.',
        'Claim your free prize now!',
        'Meeting scheduled for tomorrow.',
        'Exclusive deal just for you!',
        'Can we reschedule our meeting?',
    ],
    'label': [1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Build a pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'spam_model.pkl')

print("Model trained and saved.")
