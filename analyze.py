"""
AI Product Manager — example analysis.
Reads data/AI_PM_Examples.xlsx and produces two charts in charts/.
Run:  python3 analyze.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # no screen needed; saves to file
import matplotlib.pyplot as plt
import numpy as np

XLSX = "data/AI_PM_Examples.xlsx"
SKILLS = ["AI_Literacy","Data_Strategy","Responsible_AI","Cross_Functional","Experimentation"]

# --- load ---
df = pd.read_excel(XLSX, sheet_name="AI_PM_Examples")
print("Loaded", len(df), "AI-PM examples")
print(df[["Industry","Business_Impact"]].to_string(index=False))

# --- Chart 1: business impact by industry (bar) ---
d = df.sort_values("Business_Impact", ascending=True)
plt.figure(figsize=(8,4.5))
plt.barh(d["Industry"], d["Business_Impact"], color="#4F81BD")
plt.xlabel("Business impact (1-5)")
plt.title("AI-PM examples — business impact by industry")
plt.xlim(0,5)
plt.tight_layout()
plt.savefig("charts/business_impact.png", dpi=150)
plt.close()

# --- Chart 2: skill emphasis heatmap (industry x skill) ---
mat = df.set_index("Industry")[SKILLS]
plt.figure(figsize=(8,4.5))
im = plt.imshow(mat.values, cmap="Blues", vmin=1, vmax=5, aspect="auto")
plt.xticks(range(len(SKILLS)), [s.replace("_","\n") for s in SKILLS])
plt.yticks(range(len(mat.index)), mat.index)
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        plt.text(j, i, int(mat.values[i,j]), ha="center", va="center",
                 color="white" if mat.values[i,j]>=4 else "black", fontsize=10)
plt.colorbar(im, label="Emphasis (1-5)")
plt.title("Skill emphasis across AI-PM examples")
plt.tight_layout()
plt.savefig("charts/skill_heatmap.png", dpi=150)
plt.close()

# --- quick summary table saved to CSV ---
summary = df[SKILLS].mean().round(2).sort_values(ascending=False)
summary.to_csv("charts/skill_averages.csv", header=["avg_emphasis"])
print("\nAverage emphasis per skill:")
print(summary.to_string())
print("\nSaved: charts/business_impact.png, charts/skill_heatmap.png, charts/skill_averages.csv")
