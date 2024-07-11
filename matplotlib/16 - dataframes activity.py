# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# COMMAND ----------

hotels = pd.read_excel("/dbfs/FileStore/matplotlib/HotelCustomersDataset.xlsx")
thing1 = hotels["date"] = (
    pd.to_datetime("2018-12-31")
    - pd.to_timedelta(hotels["DaysSinceCreation"], unit="D")
).astype("datetime64[ns]") 
thing1

# COMMAND ----------

hotels.info()

# COMMAND ----------

hotels.head()

# COMMAND ----------

daily_revenue = (
    hotels
    .groupby("date")
    .agg({"LodgingRevenue": "sum", "OtherRevenue": "sum"})
)

monthly_revenue = daily_revenue.resample("M").sum()

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(monthly_revenue)
plt.show

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(monthly_revenue["LodgingRevenue"])
ax.plot(monthly_revenue["OtherRevenue"])
plt.show

# COMMAND ----------


