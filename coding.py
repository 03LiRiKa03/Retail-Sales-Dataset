import pandas as pd

df = pd.read_csv(".venv/SuperMarket Analysis.csv")

df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

df["DayOfWeek"] = pd.to_datetime(df["Date"]).dt.day_name()

df.to_csv("SuperMarket_Sales_Clean.csv", index=False)