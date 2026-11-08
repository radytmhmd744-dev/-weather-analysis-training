import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("mecca_weather_data (1).csv")

# Task 1: Display First 10 Rows
print("\n===== First 10 Rows =====")
print(df.head(10))

# Task 2: Dataset Information
print("\n===== Dataset Information =====")
print("Number of Rows and Columns:", df.shape)
print("Column Names:", df.columns.tolist())

# Task 3: Average Temperature
average_temp = df["temp"].mean()

print("\n===== Average Temperature =====")
print(f"Average Temperature: {average_temp:.2f} °C")

# Task 4: Highest and Lowest Temperature
highest_temp = df["temp"].max()
lowest_temp = df["temp"].min()

highest_date = df.loc[df["temp"].idxmax(), "time"]
lowest_date = df.loc[df["temp"].idxmin(), "time"]

print("\n===== Temperature Analysis =====")
print(f"Highest Temperature: {highest_temp} °C")
print("Date:", highest_date)
print(f"Lowest Temperature: {lowest_temp} °C")
print("Date:", lowest_date)

# Task 5: Missing Values
missing_values = df.isna().sum()

print("\n===== Missing Values =====")
print(missing_values)

print("\n===== Impact of Missing Values =====")
for column, count in missing_values.items():
    if count > 0:
        percentage = (count / len(df)) * 100
        print(
            f"{column}: {count} missing values "
            f"({percentage:.1f}%). These missing records may limit "
            f"analysis of this weather variable."
        )
    else:
        print(f"{column}: No missing values.")

# Task 6: Temperature Chart for the First 30 Days
first_30_days = df.head(30)

plt.figure(figsize=(12, 5))
plt.plot(
    first_30_days["time"],
    first_30_days["temp"],
    marker="o"
)

plt.title("Temperature During the First 30 Days")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
