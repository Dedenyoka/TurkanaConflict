import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# === 1. Load Data ===
df_conflict = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\conflicts.csv")
df_peace = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\peace.csv")

# === 2. Parse dates and clean ===
for df in [df_conflict, df_peace]:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

# === 3. Assign escalation labels ===
# Escalated if serious consequences in conflict data
escalation_keywords = r'killed|injured|hundred|hundreds|[5-9][0-9]{1,}\s*livestock|700\s*livestock'
df_conflict['escalated'] = df_conflict['Consequences'].str.contains(escalation_keywords, case=False, regex=True).astype(int)
df_peace['escalated'] = 0  # All peaceful events are non-escalated

# === 4. Combine both datasets ===
df_all = pd.concat([df_conflict, df_peace], ignore_index=True)

# === 5. Feature Engineering ===
df_all['year'] = df_all['Date'].dt.year
df_all['month'] = df_all['Date'].dt.month
df_all['day'] = df_all['Date'].dt.day
df_all['weekday'] = df_all['Date'].dt.weekday
df_all['desc_length'] = df_all['Description'].fillna("").apply(len)
df_all['conseq_length'] = df_all['Consequences'].fillna("").apply(len)
df_all['num_parties'] = df_all['Involved Parties'].fillna("").str.count('/') + df_all['Involved Parties'].fillna("").str.count(' and ') + 1

# One-hot encode event types
event_type_dummies = pd.get_dummies(df_all['Event Type'], prefix='event')

# Combine features
X = pd.concat([
    df_all[['Lat', 'Long', 'year', 'month', 'day', 'weekday', 'desc_length', 'conseq_length', 'num_parties']],
    event_type_dummies
], axis=1)
y = df_all['escalated']

# === 6. Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# === 7. Train Random Forest ===
clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
clf.fit(X_train, y_train)

# === 8. Evaluate ===
y_pred = clf.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
