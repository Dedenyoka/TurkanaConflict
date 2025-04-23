import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from geopy.geocoders import Nominatim
from flask import Flask, render_template_string

app = Flask(__name__)

# === 1. Load Data ===
df_conflict = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\conflicts.csv")
df_peace = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\peace.csv")

# === 2. Parse dates and clean ===
for df in [df_conflict, df_peace]:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

# === 3. Assign escalation labels ===
escalation_keywords = r'killed|injured|hundred|hundreds|[5-9][0-9]{1,}\s*livestock|700\s*livestock'
df_conflict['escalated'] = df_conflict['Consequences'].str.contains(escalation_keywords, case=False, regex=True).astype(int)
df_peace['escalated'] = 0

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

event_type_dummies = pd.get_dummies(df_all['Event Type'], prefix='event')

X = pd.concat([
    df_all[['Lat', 'Long', 'year', 'month', 'day', 'weekday', 'desc_length', 'conseq_length', 'num_parties']],
    event_type_dummies
], axis=1)
y = df_all['escalated']

# === 6. Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# === 7. Train Model ===
clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
clf.fit(X_train, y_train)

# === 8. Evaluation ===
y_pred = clf.predict(X_test)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# === 9. Feature Importance ===
importances = clf.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

# Top events
event_features = [col for col in feature_names if col.startswith('event_')]
event_scores = sorted([
    (name, importances[feature_names.get_loc(name)] * 100)  # Convert to percentage
    for name in event_features
], key=lambda x: x[1], reverse=True)[:5]

# Top regions
geo_importance = pd.DataFrame({
    'Lat': df_all['Lat'],
    'Long': df_all['Long'],
    'importance': clf.feature_importances_[:2].mean()
})
top_regions = geo_importance.sort_values(by='importance', ascending=False).head(3)

geolocator = Nominatim(user_agent="turkana_escalation_model")
region_info = []
for idx, row in top_regions.iterrows():
    try:
        location = geolocator.reverse((row['Lat'], row['Long']), timeout=10)
        address = location.address.split(',')[0]
    except:
        address = "Unknown Location"
    region_info.append((address, row['Lat'], row['Long']))

# === 10. Web Display ===
@app.route('/')
def index():
    return render_template_string('''
        <h1>Escalation Prediction Summary</h1>
        <h2>Model Performance</h2>
        <pre>{{ report }}</pre>
        <h2>Confusion Matrix</h2>
        <pre>{{ matrix }}</pre>
        <h2>Top Events Driving Escalation</h2>
        <ul>
        {% for event, score in events %}
            <li>{{ event.replace('event_', '').replace('_', ' ') }} (Importance: {{ '{:.2f}'.format(score) }}%)</li>
        {% endfor %}
        </ul>
        <h2>Top Locations Linked to Escalation</h2>
        <ul>
        {% for address, lat, long in regions %}
            <li>{{ address }} - (Lat: {{ lat }}, Long: {{ long }})</li>
        {% endfor %}
        </ul>
    ''', report=report, matrix=conf_matrix, events=event_scores, regions=region_info)

if __name__ == '__main__':
    app.run(debug=True)
