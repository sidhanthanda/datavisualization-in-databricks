# Databricks notebook source
import pandas as pd
country= pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
country

btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

#country.set_index("Country name", inplace=True)
#country

# COMMAND ----------

btc.drop(labels=["SNo","Name", "Symbol"], axis='columns')


# COMMAND ----------

btc.drop(labels=["SNo","Name", "Symbol"], axis='columns')


# COMMAND ----------

btc[["Date", "High", "Low"]]

# COMMAND ----------

btc.drop(columns=["SNo","Name", "Symbol"], inplace=True)
btc

# COMMAND ----------


