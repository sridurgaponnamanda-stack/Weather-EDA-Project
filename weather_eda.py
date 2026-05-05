import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("weather_data.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp.png")
plt.show()

# Humidity Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Humidity'], marker='o')
plt.title("Humidity Trend")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("humidity.png")
plt.show()

# Precipitation Chart
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Precipitation'])
plt.title("Precipitation Chart")
plt.xlabel("Date")
plt.ylabel("Precipitation (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("rainfall.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['Temperature','Humidity','Precipitation']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()