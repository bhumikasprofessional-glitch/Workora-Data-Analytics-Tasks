#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# 1. Load Data
print("Loading raw dataset for structural validation...")
file_path = r"C:\Users\NITIN CHHABRA\Documents\Week1_NLP_Internship\Data\Reviews.csv"
df = pd.read_csv(file_path, nrows=5000)

# Record baseline shape before cleaning
initial_rows, initial_cols = df.shape
print(f"Initial Dataset Shape: {initial_rows} Rows, {initial_cols} Columns")

print("\n--- Starting Data Cleaning & Structural Validation Pipeline ---")

# =========================================================
# STEP 2: DUPLICATE REMOVAL
# =========================================================
# Checking duplicates across core identifying features
duplicate_count = df.duplicated(subset=['UserId', 'ProductId', 'Time', 'Text']).sum()
print(f"[Validation] Duplicate records identified: {duplicate_count}")

# Drop duplicates in-place
df.drop_duplicates(subset=['UserId', 'ProductId', 'Time', 'Text'], inplace=True)
df.reset_index(drop=True, inplace=True)

# =========================================================
# STEP 3: MISSING VALUE HANDLING (IMPUTATION)
# =========================================================
print("\n[Validation] Checking for missing/null fields:")
null_summary = df.isnull().sum()
for col, missing in null_summary.items():
    if missing > 0:
        print(f" -> Column '{col}' has {missing} null values.")

# Handle missing strings in structural text columns safely
df['Summary'] = df['Summary'].fillna('No Summary Provided')
df['Text'] = df['Text'].fillna('Empty Review Log')

# =========================================================
# STEP 4: DATA TYPE CONVERSION & VALIDATION
# =========================================================
print("\n[Validation] Normalizing data types and constraints...")

# Formatting Unix Timestamps into structural Datetime format
df['Datetime_Format'] = pd.to_datetime(df['Time'], unit='s')

# Validating rating boundaries (Scores must be between 1 and 5)
df['Score'] = df['Score'].clip(lower=1, upper=5)

# Final Post-Cleaning Shape evaluation
final_rows, final_cols = df.shape
print("\n--- Structural Validation Successfully Completed ---")
print(f"Final Cleaned Shape: {final_rows} Rows, {final_cols} Columns")
print(f"Total entries securely pruned/cleaned: {initial_rows - final_rows}")

# Save the pristine dataset as output
output_name = "Validated_Cleaned_Reviews.csv"
df.to_csv(output_name, index=False)
print(f"Cleaned repository artifact exported as: '{output_name}'")


# In[ ]:




