from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the labeled dataset of emails
emails = [("spam", "spam email content"), ("not spam", "not spam email content"), ...]

# Extract the email content and labels
X, y = zip(*emails)

# Convert the email content to a numerical feature vector
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Train the naive Bayes classifier
clf = MultinomialNB()
clf.fit(X, y)

# Classify a new, unseen email
new_email = "This is an email I want to classify as spam or not spam"
new_email_vec = vectorizer.transform([new_email])
prediction = clf.predict(new_email_vec)
print(prediction)
