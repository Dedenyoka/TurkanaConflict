import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load data
df = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\conflicts.csv")

# Parse dates and drop invalid ones
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Define escalation based on criteria
escalation_keywords = r'killed|injured|hundred|hundreds|[5-9][0-9]{1,}\s*livestock|700\s*livestock'
df['escalated'] = df['Consequences'].str.contains(escalation_keywords, case=False, regex=True).astype(int)

# Feature engineering
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['weekday'] = df['Date'].dt.weekday
df['desc_length'] = df['Description'].apply(len)
df['conseq_length'] = df['Consequences'].apply(len)
df['num_parties'] = df['Involved Parties'].str.count('/') + df['Involved Parties'].str.count(' and ') + 1

event_type_dummies = pd.get_dummies(df['Event Type'], prefix='event')

# Combine features
X = pd.concat([
    df[['Lat', 'Long', 'year', 'month', 'day', 'weekday', 'desc_length', 'conseq_length', 'num_parties']],
    event_type_dummies
], axis=1)
y = df['escalated']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
