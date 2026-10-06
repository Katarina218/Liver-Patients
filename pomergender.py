import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("LiverPatient.csv", header=0, names=["age", "gender", "tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "tot_proteins", "albumin", "ag_ratio", "is_patient"])
hodnoty = ["tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "albumin"]
df_chori = df[df["is_patient"] == 1]

print(df_chori["gender"].value_counts())