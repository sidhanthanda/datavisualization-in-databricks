# Databricks notebook source
import pandas as pd
country= pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
country


country.set_index("Country name", inplace=True)
country

btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic

#

# COMMAND ----------

titanic["species"] = "human"
titanic

# COMMAND ----------

titanic.drop(columns=["species"], inplace=True)
titanic

# COMMAND ----------

titanic["thing"] = titanic.sibsp + titanic["parch"]
titanic

# COMMAND ----------

titanic.sort_values("num_relatives", ascending=False)

# COMMAND ----------



# COMMAND ----------

titanic[titanic["survived"] == 1].sort_values("num_relatives", ascending=False)

# COMMAND ----------


