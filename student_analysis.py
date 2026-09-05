import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Anu", "Rahul", "Meera", "Arjun", "Diya"],
    "Maths": [85, 72, 90, 65, 78],
    "Science": [88, 75, 95, 70, 80],
    "English": [82, 70, 88, 68, 85]
}

df = pd.DataFrame(data)

df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("Student Performance Analysis")
print("\nStudent Data:")
print(df)

print("\nClass Average:")
print(df["Average"].mean())

print("\nTop Performing Student:")
print(df.loc[df["Average"].idxmax(), "Name"])

plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Performance")
plt.show()