import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# load dataset
df = pd.read_csv(r'D:/Coding/Projects/TurkanaConflicts/data/peace.csv', quotechar='"')
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' to datetime

# Create a simple timeline plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Date'], [1] * len(df), 'ro', markersize=6)  # Plot events as red dots

ax.set_title("Peace Agreements", fontsize=20)
ax.set_xlabel("Date", fontsize=15)
ax.set_yticks([])  # No y-axis needed

# Format the x-axis for better readability
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())

plt.xticks(rotation=45)
plt.grid(True)
plt.show()