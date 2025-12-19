# 🎮 Gaming Hours vs Performance Analysis

## 📦 About Data

A Kaggle [dataset](https://www.kaggle.com/datasets/prince7489/gaming-hours-vs-academic-and-work-performance) exploring the relationship between gaming habits and academic/work performance across 1,000 users.

This dataset contains information on gaming behavior, sleep patterns, stress levels, and performance metrics for students and working professionals.

---

## 💡 Highlights

- **Gaming hours alone don't predict performance** — Light, Moderate, and Heavy gamers all perform similarly (~75 avg)
- **Sleep + Stress combination matters** — Users with poor sleep AND high stress show noticeably lower performance
- **Students vs Professionals** — Both groups show similar patterns, though students with poor sleep slightly outperform professionals with poor sleep
- **No "sweet spot" for gaming** — The scatter plot shows no clear relationship between daily gaming hours and performance

---

## ✏️ Data Wrangling

Conducted data cleaning and feature engineering using Python:

- Checked for missing values and duplicates
- Cleaned text columns (standardized formatting)
- Created new categorical features:
  - `Gaming_Intensity` — Light (0-2h), Moderate (2-4h), Heavy (4-6h), Extreme (6h+)
  - `Sleep_Quality` — Poor (<5h), Adequate (5-7h), Good (7h+)
  - `Age_Group` — 18-22, 23-27, 28-32, 33+
  - `Overall_Performance` — Average of Academic/Work Score and Productivity Level
  - `High_Stress` — Boolean flag for stress level ≥ 7
  - `Performance_Category` — Low, Medium, High, Excellent

📌 Python script: [Python](https://github.com/AlmostSurely1476/Gaming-Hours-and-Performance-Analysis-/blob/main/CleaningData.py)

📌 Clean Data: [Gaming_Data_CLEANED.csv](https://github.com/AlmostSurely1476/Gaming-Hours-and-Performance-Analysis-/blob/main/Gaming_Data_CLEANED.csv)

---

## 📊 Visualization

Produced a 1-pager dashboard using Tableau.

Tableau: [Link](https://public.tableau.com/app/profile/justin.eng3812/viz/GamingHours_Performance_Analysis/Dashboard1?publish=yes)

<img width="2055" height="1212" alt="Gaming_Performance" src="https://github.com/user-attachments/assets/976a30fd-5a44-4810-b6e0-da2da94c004d" />
