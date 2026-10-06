import pandas as pd

df = pd.read_csv("LiverPatient.csv", header=0, names=["age", "gender", "tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "tot_proteins", "albumin", "ag_ratio", "is_patient"])
print(df.isnull().sum())
print(df["is_patient"].value_counts())
print(df["gender"].value_counts())

hodnoty = ["tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "albumin"]
print(df.groupby("is_patient")[hodnoty].median())