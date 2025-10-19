import pandas as pd

df = pd.read_csv("your_file.csv")

df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

df["DayOfWeek"] = pd.to_datetime(df["Date"]).dt.day_name()

df.to_csv("SuperMarket_Sales.csv", index=False)
