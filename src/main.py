import pandas as pd

df = pd.read_csv(
    "data/finance_history.csv",
    names=["Income", "Expenses", "Savings", "SavingsRate", "Health"]
)

print("\nAnalytics Summary")
print("Average Income:", round(df["Income"].mean(), 2))
print("Average Expenses:", round(df["Expenses"].mean(), 2))
print("Average Savings:", round(df["Savings"].mean(), 2))
