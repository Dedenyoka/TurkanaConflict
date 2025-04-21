import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


df = pd.read_csv(r'D:/Coding/Projects/TurkanaConflicts/data/peace.csv', quotechar='"')

# Define a function to categorize the consequences
def categorize_consequences(consequence):
    if 'violence' in consequence or 'casualties' in consequence:
        return 'Security/Violence Reduction'
    elif 'relations' in consequence or 'peace committee' in consequence:
        return 'Cooperation/Relationships'
    elif 'grazing' in consequence or 'trade' in consequence:
        return 'Economic/Social Development'
    elif 'disarmament' in consequence:
        return 'Disarmament Efforts'
    elif 'cultural' in consequence or 'integration' in consequence:
        return 'Cultural/Social Integration'
    else:
        return 'Other'

# Apply the function to categorize the Consequences column
df['Consequences_Category'] = df['Consequences'].apply(categorize_consequences)

# Count the frequency of each category
category_counts = df['Consequences_Category'].value_counts()

# Plot the result
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Type of Treaties', fontsize=16)
plt.xlabel('Consequences Categories', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
