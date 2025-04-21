import folium
import pandas as pd
import random

# Load dataset
df = pd.read_csv("D:/Coding/Projects/TurkanaConflicts/data/conflicts.csv")

# Filter out rows with missing or invalid coordinates
valid_data = df.dropna(subset=['Lat', 'Long'])
valid_data = valid_data[(valid_data['Lat'] != 0) & (valid_data['Long'] != 0)]

# Create base map centered on the Turkana region
map_center = [3.5, 35.0]  # Adjust based on dataset region (Turkana, Kenya/Ethiopia border, Kenya/Sudan border)
mymap = folium.Map(location=map_center, zoom_start=7)

# Event type color palette
event_colors = {
    "Cattle Raid": "red",
    "Clash over grazing land": "blue",
    "Cross-border attack": "green",
    "Attack on Police": "purple"
    # Add more event types and their colors as needed
}

# Plot each location on the map
for _, row in valid_data.iterrows():
    lat, lon = row['Lat'], row['Long']

    # Add a small random offset for duplicate coordinates
    offset_lat = random.uniform(-0.005, 0.005)  # small random offset for latitude
    offset_lon = random.uniform(-0.005, 0.005)  # small random offset for longitude

    # Event Type (used to set the marker color)
    event_type = row['Event Type']
    
    # Assign a default color if the event type is not in the palette
    marker_color = event_colors.get(event_type, "gray")  # Default to gray if event type not listed

    # Create popup content for each event
    popup_content = f"""
    Location: {row['Location']}<br>
    Date: {row['Date']}<br>
    Event: {event_type}<br>
    Casualties: {row['Consequences']}
    """

    # Add marker to map with random offset and event-based color
    folium.Marker(
        [lat + offset_lat, lon + offset_lon], 
        popup=popup_content,
        icon=folium.Icon(color=marker_color)
    ).add_to(mymap)

# Save map as an HTML file
mymap.save('map_colored.html')
