import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("Gaming_Hours_vs_Performance_1000_Rows.csv")

print(f'Loaded {df.shape[0]} rows and {df.shape[1]} columns.')

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Remove duplicates 
df = df.drop_duplicates() 

# Clean text columns
text_columns = ['Gender', 'Occupation', 'Game_Type', 'Primary_Gaming_Time', 'Performance_Impact']

for col in text_columns:
    df[col] = df[col].str.strip()
    df[col] = df[col].str.title()

# Create new columns for Tableau  
df['Gaming_Intensity'] = pd.cut(
    df['Daily_Gaming_Hours'],
    bins=[0, 2, 4, 6, 24],
    labels=['Light (0-2h)', 'Moderate (2-4h)', 'Heavy (4-6h)', 'Extreme (6h+)']
)

df['Sleep_Quality'] = pd.cut(
    df['Sleep_Hours'],
    bins=[0, 5, 7, 12],
    labels=['Poor (<5h)', 'Adequate (5-7h)', 'Good (7h+)']
)

df['Overall_Performance'] = (df['Academic_or_Work_Score'] + df['Productivity_Level']) / 2

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[17, 22, 27, 32, 40],
    labels=['18-22', '23-27', '28-32', '33+']
)

df['High_Stress'] = df['Stress_Level'] >= 7

df['Performance_Category'] = pd.cut(
    df['Overall_Performance'],
    bins=[0, 60, 75, 90, 100],
    labels=['Low', 'Medium', 'High', 'Excellent']
)

# Save the cleaned data
df.to_csv('Gaming_Data_CLEANED.csv', index=False)

print("\n DONE! Saved as 'Gaming_Data_CLEANED.csv'")