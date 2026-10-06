# Liver-Patients
We performed exploratory analysis on 583 liver-patient lab records (correcting a column-naming mismatch first), compared diseased vs. healthy patients and male vs. female patients using boxplots and a Mann-Whitney U test, then built a logistic regression classifier to predict disease status and tuned its decision threshold using an ROC curve to balance recall between the two classes.

# goal
built a model to predict disease status

# data
Indian liver patients from Kaggle.com (https://www.kaggle.com/datasets/zubairdhuddi/indian-liver-patient-dataset)

# methods
 - exploratory data analysis (age, gender, mixed columns)
 - using boxplots and mannwhitneyu model
 - using Logistics Regression classifier to predict disease status and tuned its deciding threshold by ROC curve
# results
 - accuracy - 75%
            - 60% with class_weight = balanced
            - 66% with optimal threshold
- main finding - the logistic regression model (AUC = 0.76) could meaningfully distinguish diseased from healthy patients using liver lab values, but the default 0.5 threshold badly missed healthy patients — shifting the threshold to 0.64 gave a much better balance (60% recall for disease, 81% recall for healthy), showing that model tuning matters as much as model choice for imbalanced medical data. 

# tools
python, pandas, numpy, sklearn, scipy, matplotlib, seaborn


