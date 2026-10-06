import pandas as pd
df = pd.read_csv("LiverPatient.csv", header=0, names=["age", "gender", "tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "tot_proteins", "albumin", "ag_ratio", "is_patient"])
hodnoty = ["tot_bilirubin", "direct_bilirubin", "alkphos", "sgpt", "sgot", "albumin"]
df_chori = df[df["is_patient"] == 1]

x = df[hodnoty]
y = df["is_patient"]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
import numpy as nm
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=42)
logreg.fit(x_train_scaled, y_train)
y_pred = logreg.predict(x_test_scaled)
y_proba = logreg.predict_proba(x_test_scaled)[:,0]
y_proba_novy = (y_proba >= 0.642).astype(int)
y_proba_novy = nm.where(y_proba_novy == 1, 1, 2)

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_proba_novy)
print(cnf_matrix)
print(metrics.classification_report(y_test, y_proba_novy))

from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

fpr, tpr, tresholds = roc_curve(y_test, y_proba, pos_label = 1)
roc_auc = roc_auc_score(y_test == 1, y_proba)

optimal_idx = nm.argmax(tpr - fpr)
optimal_treshold = tresholds[optimal_idx]
print("Optimal prah:", optimal_treshold)
print("Pri prahu TPR:", tpr[optimal_idx], "FPR:", fpr[optimal_idx])
plt.plot(fpr, tpr, label = f"AUC = {roc_auc:.2f}")
plt.plot([0,1], [0,1], linestyle="--", color="gray", label ="nahodny model")
plt.xlabel("False positive rate")
plt.ylabel("True positive rate(Recall)")
plt.title("ROC-krivka")
plt.legend()
plt.savefig("roc_krivka.png")
plt.show()