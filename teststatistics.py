import pandas as pd
df = pd.read_csv("LiverPatient.csv", header=0, names=["age", "gender", "tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "tot_proteins", "albumin", "ag_ratio", "is_patient"])
hodnoty = ["tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "albumin"]
df_chori = df[df["is_patient"] == 1]

from scipy.stats import mannwhitneyu

for col in hodnoty:
    muzi = df_chori[df_chori["gender"] == "Male"][col]
    zeny = df_chori[df_chori["gender"] == "Female"][col]
    stat, p = mannwhitneyu(muzi, zeny)
    print(f"{col}: p-hodnota = {p: .4f}")

