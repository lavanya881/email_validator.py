
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 75, 90, 60, 85]
}
df = pd.DataFrame(data)

print("Dataset:")
print(df)
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks (Matplotlib)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
plt.figure(figsize=(6,4))
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Marks (Seaborn)")
plt.show()
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Saved Image")
plt.savefig("output.png")

print("Graph saved as output.png")