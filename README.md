# 📌 Turkana Conflict & Peace Agreements Analysis
## 🕊️ A data-driven exploration of conflicts, peacebuilding, and media coverage in the Turkana region of Kenya, East Africa.
🌍 Project Overview

The Turkana region — spanning borders between Kenya, Uganda, South Sudan, and Ethiopia — has long been affected by recurring conflicts over livestock, grazing land, and water. Despite this, it remains underrepresented in mainstream global datasets.

This project curates, cleans, and analyzes detailed event-level data on conflicts and peace agreements reported in the region from 2011 to 2025, offering a unique lens into:

- The nature of peace efforts

- The actors involved

- The effectiveness of peace interventions

 And the media coverage that amplifies (or omits) these narratives.

## 🛠️ Tools & Technologies
- Python: Pandas, NumPy, Matplotlib, Seaborn, Folium

- Git & GitHub for version control and collaboration

## 📊 Data

This project draws on two key datasets compiled from open media sources and government reports:

### 1. `conflicts.csv`
A chronological record of conflict events in the Turkana region and surrounding areas (2013–2025).

- **Fields:**  
  `Date`, `Location`, `Lat`, `Long`, `Involved Parties`, `Event Type`, `Description`, `Consequences`, `Source`

- **Sample Events:**  
  - Cross-border cattle raids  
  - Armed ambushes  
  - Clashes involving local communities and state actors

- **Sources include:**  
  *The Star, Daily Nation, Reuters, The Standard, Capital FM, Tuko.co.ke, Kenya Red Cross, The New Humanitarian*

---

### 2. `peace.csv`
A detailed log of peace efforts, disarmament campaigns, and local reconciliation initiatives (2011–2025).

- **Fields:**  
  `Date`, `Location`, `Involved Parties`, `Event Type`, `Description`, `Consequences`, `Source`

- **Sample Initiatives:**  
  - Lokiriama Peace Accords  
  - Voluntary Disarmament
  - Joint Peace Patrols


## 📊 Visual Analysis
- Peace event frequency over time

- Most common event types: Peace Agreements, Disarmament Initiatives, Community Meetings

- Plots violent events on a map using longitude and latitude.

- Media outlets: Who reports on these events most consistently?

## Example Visuals:
- 📈 Bar chart: Peace events per year
- 🧭 Map : Event locations
- 📡 Pie chart: Sources of reports (e.g., local gov’t vs national media)

## 📰 Media Coverage Analysis
- By comparing sources across both datasets:

- Some outlets (e.g., Kenya News Agency, Turkana County Government) consistently report on peacebuilding.

- Others highlight conflict events but neglect resolutions.

- This gap in coverage can influence public and policy perception.

## 🚀 What's Next?
📊 Interactive Dashboard with filters by location, time, and event type.

🌐 Predictive model to predict violence escalation.

🤝 Merge with external datasets (drought, elections, aid interventions) to understand root causes.

## 🙋 Why This Project Matters
- Highlights underrepresented conflicts and peace efforts.

- Encourages data-informed peacebuilding strategies.

- Demonstrates technical skills in data cleaning, visualization, exploratory analysis, and critical thinking.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone git@github.com:Dedenyoka/turkana-conflict-analysis.git
