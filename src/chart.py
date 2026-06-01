import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/finance_history.csv",
    names=["Income", "Expenses", "Savings", "SavingsRate", "Health"]
)

plt.figure(figsize=(8, 5))
plt.plot(df["Savings"], marker="o")
plt.title("Savings Trend")
plt.xlabel("Record Number")
plt.ylabel("Savings")
plt.grid(True)

plt.savefig("screenshots/savings_trend.png")
print("Chart saved to screenshots/savings_trend.png")
