import pandas as pd
import matplotlib.pyplot as plt

# Assuming both CSV files have been loaded into two DataFrames
# df_conflict and df_peace_treaties

# 1. Load conflict data
df_conflict = pd.read_csv("D:/Coding/Projects/TurkanaConflicts/data/conflicts.csv")

# 2. Load peace treaties data
df_peace_treaties= pd.read_csv(r'D:/Coding/Projects/TurkanaConflicts/data/peace.csv', quotechar='"')

# 3. Combine the two datasets into one (to compare sources)
df_conflict['Event Type'] = 'Conflict'  # Label conflict events
df_peace_treaties['Event Type'] = 'Peace Treaty'  # Label peace treaty events

# Combine both dataframes into a single dataframe
df_combined = pd.concat([df_conflict[['Date', 'Location', 'Event Type', 'Source']],
                         df_peace_treaties[['Date', 'Location', 'Event Type', 'Source']]])

# 4. Count the occurrences of each source
source_counts = df_combined['Source'].value_counts()

# 5. Visualize the sources that are most frequently reporting
plt.figure(figsize=(12, 6))

# Plot the top 10 most frequent sources
source_counts.head(10).plot(kind='barh', color='skyblue')

# Customize chart
plt.title('Top 10 Media Outlets Reporting on Conflicts and Peace Treaties', fontsize=16)
plt.xlabel('Number of Reports', fontsize=12)
plt.ylabel('Media Outlets', fontsize=12)
plt.tight_layout()

# Show the chart
plt.show()

# For deeper insights, look at the breakdown of sources by event type
source_event_type_counts = pd.crosstab(df_combined['Source'], df_combined['Event Type'])
print(source_event_type_counts)
