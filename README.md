🧾 README.md
☀️ Solar Energy Data Analysis & Interactive Dashboard

This project explores solar energy generation across multiple countries using Python and Streamlit.  
It provides automated data cleaning, outlier detection, statistical summaries, and an interactive dashboard for visual exploration.


🌍 Project Overview

The aim of this project is to analyze and visualize global solar energy performance.  
We assess trends, identify outliers, and build insights on energy production, efficiency, and growth patterns.


 🧠 Key Features

- Automated Data Cleaning:  
  Removes duplicates, handles missing values, normalizes columns, and flags invalid readings.

- Outlier Detection & Correction:  
  Uses Z-score and IQR to detect and optionally cap abnormal values.

- Exploratory Data Analysis (EDA):  
  Interactive charts with Plotly + Streamlit for dynamic exploration.

- Cross-Country Comparison:  
  Statistical analysis comparing average solar output, capacity, and efficiency by country.

- Streamlit Dashboard:  
  Real-time data visualization with filters for region, country, and year.


 🧩 Folder Structure
solar-challenge-week0/
│
├── app/
│ ├── dashboard.py  Main Streamlit dashboard logic
│ ├── components/  Visualization components
│
├── data/
│ ├── solar_clean.csv  Cleaned dataset
│ ├── solar_raw.csv  Original dataset
│
├── notebooks/
│ ├── data_cleaning.ipynb  Initial data cleaning process
│ ├── exploratory_analysis.ipynb
│
├── scripts/
│ ├── data_cleaning.py  Automated cleaning script
│ ├── eda_analysis.py  EDA + statistical comparison
│
├── requirements.txt
├── README.md
└── streamlit_app.py  App entry file

 🧹 Data Cleaning Workflow

The cleaning pipeline includes:
- Dropping duplicate and null rows
- Converting datatypes to correct formats
- Handling outliers using IQR and Z-Score methods
- Standardizing column names
- Saving a cleaned version to `data/solar_clean.csv`

Example code snippet:

```python
from scripts.data_cleaning import clean_data

df = clean_data("data/solar_raw.csv")
df.to_csv("data/solar_clean.csv", index=False)

📊 Cross-Country Analysis
Example insights derived:
•	Kenya and Ethiopia showed the highest growth rate in solar adoption between 2018–2024.
•	Togo had the largest variability in production (high outlier influence).
•	The average solar capacity utilization improved by ~15% over 5 years globally.
🖥️ Dashboard Preview
The dashboard allows you to:
•	Filter data by country and year
•	Explore solar output trends
•	Identify underperforming or high-potential regions
•	Visualize outliers interactively with Plotly
Run locally with:
streamlit run streamlit_app.py
📈 Example Visuals
(to include in LinkedIn post screenshot)
•	Solar output trends per country (line chart)
•	Top producers bar chart
•	Outlier boxplot visualization
🧮 Libraries Used
pandas
numpy
plotly
streamlit
scipy
matplotlib
seaborn
🧩 Author
Newaz Nezif
Cybersecurity Analyst | Data Science Enthusiast
(24) Newaz Nezif | LinkedIn    | GitHub
