import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("LiverPatient.csv", header=0, names=["age", "gender", "tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "tot_proteins", "albumin", "ag_ratio", "is_patient"])
hodnoty = ["tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "albumin"]
df_chori = df[df["is_patient"] == 1]
fig, axes = plt.subplots(2, 3, figsize = (12, 7))

for ax, col in zip(axes.flatten(), hodnoty):
    sb.boxplot(data = df_chori, x = "gender", y = col, ax = ax)
    ax.set_title(col)
    if col != "albumin":
        ax.set_yscale("log")

plt.tight_layout()
plt.savefig("hodnotychorygender.png")
plt.show()

