#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
print("Extracting location metadata for Geospatial Pipeline...")
file_path = r"C:\Users\NITIN CHHABRA\Documents\Week1_NLP_Internship\Data\Reviews.csv"
df = pd.read_csv(file_path, nrows=5000)

# =========================================================
# STEP 2: GEOGRAPHIC REGION MAPPING & DEMAND MATRIX
# =========================================================
# Simulating corporate global operational markets for expansion tracking
regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
np.random.seed(42)  # For reproducible results
df['Market_Region'] = np.random.choice(regions, size=len(df), p=[0.50, 0.25, 0.15, 0.10])

# Compute regional metrics: Transaction Volume vs Average Rating
geo_metrics = df.groupby('Market_Region').agg(
    Total_Sales_Demand=('ProductId', 'count'),
    Avg_Customer_Satisfaction=('Score', 'mean')
).reset_index()

print("\nComputed Regional Business Density Matrix:")
print(geo_metrics)

# =========================================================
# STEP 3: REGIONAL GEOSPATIAL VISUALIZATIONS
# =========================================================
# Plot 1: Regional Sales Demand Profile
plt.figure(figsize=(8, 5))
sns.barplot(x='Market_Region', y='Total_Sales_Demand', data=geo_metrics, palette='viridis')
plt.title('Global Market Demand Footprint (Sales Volume)', fontsize=14, fontweight='bold')
plt.xlabel('Geographic Expansion Zone')
plt.ylabel('Total Orders Logged')
plt.savefig('geospatial_demand_volume.png', bbox_inches='tight')
plt.show()

# Plot 2: Demand vs Performance Matrix (Identifying Market Gaps)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Total_Sales_Demand', y='Avg_Customer_Satisfaction', 
                hue='Market_Region', s=300, data=geo_metrics, palette='deep')
plt.title('Expansion Grid: High Demand vs Low Presence Target Finder', fontsize=12, fontweight='bold')
plt.xlabel('Regional Demand Volume')
plt.ylabel('Average Market Rating')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('geospatial_market_gap.png', bbox_inches='tight')
plt.show()

# 4. Export Spatial Performance Metrics
output_name = "Geospatial_Data_Analysis_Report.csv"
geo_metrics.to_csv(output_name, index=False)
print(f"\nSuccess! Geospatial grid exported as '{output_name}'")


# In[ ]:




