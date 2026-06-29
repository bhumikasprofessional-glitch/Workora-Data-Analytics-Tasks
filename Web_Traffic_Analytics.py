#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
print("Extracting digital footprints for Web Traffic Analytics Pipeline...")
file_path = r"C:\Users\NITIN CHHABRA\Documents\Week1_NLP_Internship\Data\Reviews.csv"
df = pd.read_csv(file_path, nrows=5000)

# Fill baseline parameters safely
df['HelpfulnessNumerator'] = df['HelpfulnessNumerator'].fillna(0)
df['HelpfulnessDenominator'] = df['HelpfulnessDenominator'].fillna(0)

# =========================================================
# STEP 2: TRAFFIC METRICS EXTRACTION & USER JOURNEY MAPPING
# =========================================================
# Mapping raw structural records into dynamic web engagement properties
web_traffic = pd.DataFrame()
web_traffic['User_ID'] = df['UserId']
web_traffic['Product_ID'] = df['ProductId']

# Operational Definitions for clickstream behavioral mapping
web_traffic['Page_Views'] = df['HelpfulnessNumerator'] + 1 
web_traffic['Session_Duration_Min'] = (df['HelpfulnessDenominator'] * 1.5) + 2.0

# Strategic Drop-off identification constraint: high interactions but zero helpfulness signaling bounce anomaly
def identify_dropoff(row):
    if row['Page_Views'] > 3 and row['Session_Duration_Min'] > 5.0:
         return 'Completed Journey'
    return 'Drop-off / Bounce'

web_traffic['Journey_Status'] = web_traffic.apply(identify_dropoff, axis=1)

# Summary Evaluation Logs
print(f"Total Unique Sessions Scanned: {len(web_traffic)}")
print(web_traffic['Journey_Status'].value_counts())

# =========================================================
# STEP 3: VISUALIZATIONS
# =========================================================
# Plot 1: User Journey Funnel Distribution
plt.figure(figsize=(7, 5))
sns.countplot(x='Journey_Status', data=web_traffic, palette='magma')
plt.title('Web User Journey Execution & Conversion Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Session Engagement Outcome')
plt.ylabel('Session Footprint Count')
plt.savefig('web_journey_distribution.png', bbox_inches='tight')
plt.show()

# Plot 2: Scatter Metric Correlation (Page Views vs Session Duration)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Page_Views', y='Session_Duration_Min', hue='Journey_Status', data=web_traffic, palette='cool')
plt.title('Session Intensity Matrix: Page Views vs Duration (Min)', fontsize=12, fontweight='bold')
plt.xlabel('Aggregated Page Views')
plt.ylabel('Total Session Duration (Minutes)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('traffic_intensity_correlation.png', bbox_inches='tight')
plt.show()

# 4. Export Clean Analytics Web Logs
output_name = "Web_Traffic_Analytics_Report.csv"
web_traffic.to_csv(output_name, index=False)
print(f"\nSuccess! Clean clickstream artifact exported as '{output_name}'")


# In[ ]:




