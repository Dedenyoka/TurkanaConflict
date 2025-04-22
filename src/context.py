import pandas as pd
import matplotlib.pyplot as plt
import re

#load context dataset
df = pd.read_csv(r"D:\Coding\Projects\TurkanaConflicts\data\contextual_data.csv")

# function to classify the type of aid
def classify_aid(aid_text):
    text = str(aid_text).lower()
    if "Food Assistance" in aid_text or "assisted communities" in aid_text:
        return "Food Assistance"
    elif "usaid aid freeze" in aid_text or "hiv treatment" in aid_text or "medication shortage" in aid_text:
        return "HIV Treatment Impact (USAID)"
    elif "drought-affected populations" in aid_text:
        return "Drought Support"
    else:
        return "Other"
    
# apply classification function
df['Aid Type'] = df['Aid Intervention'].apply(classify_aid)
# count occurences of each aid intervention type
aid_counts = df['Aid Intervention'].value_counts()

# create a pie chart
plt.figure(figsize=(8,8))
aid_counts.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)

#customize chart
plt.title('Distribution of Aid Interventions in Turkana and Kenya.', fontsize=14)
plt.ylabel('') # to remove the y label

# to show the plot 
plt.tight_layout()
plt.show()