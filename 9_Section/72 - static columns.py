# Databricks notebook source
import pandas as pd
country= pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
country


country.set_index("Country name", inplace=True)
country

btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
titanic

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv") 
house

# COMMAND ----------

titanic["species"] = "human"
titanic

# COMMAND ----------

house.insert(0, "county", "King County")
house

# COMMAND ----------

house["sale_price"] = house["price"]
house

# COMMAND ----------

house.insert(3, "num_bedrooms", house["bedrooms"])
house

# COMMAND ----------


