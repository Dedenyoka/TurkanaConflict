import pandas as pd 
import matplotlib.pyplot as plt


#load context dataset
df = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\contextual_data.csv")

# Extract month-year from date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # coerce drops bad dates
df['Month-Year'] = df['Date'].dt.to_period('M').astype(str)

# Filter rows where there was drought (even if all are Alert Phase for now)
drought_df = df[df['Drought Severity'].str.contains("Alert", case=False)]

# Group by location and time
grouped = drought_df.groupby(['Month-Year', 'Location']).size().unstack(fill_value=0)

# Plot drought by year and month
grouped.plot(kind='bar', stacked=True, width=0.9, figsize=(14, 7), colormap='Set3')

plt.title('Drought Presence by Location Over Time')
plt.xlabel('Time (Month-Year)')
plt.ylabel('Reported Drought Events')
plt.xticks(rotation=45)
plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()