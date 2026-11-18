import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path 
project_path=Path(__file__).resolve().parent.parent
report_path=project_path/"reports"/"day1_dataset_audit.csv"
df=pd.read_csv(report_path)
print(df.head)
print("Dataset Shape:",df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

#class wise mage distribution
plt.figure(figsize=(12,6))
sns.barplot(
    data=df,
    x="Class",
    y="Valid Images",
    hue="Split"
 )
plt.title("Class-wise Image Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#average image width analys
plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="Class",
    y="Avg Width",
    hue="Split"
 )
plt.title("Average Image Width by Class")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#invalid image percent
df["Invalid per"]=(
    df["Invalid Images"]/df["Total Images"]
)*100
print(
    df[["Class","Split","Invalid Images","Invalid per"]]
)

#save day 2 EDA report
eda_report_path=project_path/"reports"/"day2_eda_report.csv"
df.to_csv(eda_report_path,index=False)
print("Day 2 EDA Report Saved Successfully")