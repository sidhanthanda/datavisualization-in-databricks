# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

netflix

# COMMAND ----------

netflix.director

# COMMAND ----------

netflix[["title", "cast"]]

# COMMAND ----------

netflix[["title", "cast"]].tail(10)

# COMMAND ----------

netflix[["title", "cast", "description"]]

# COMMAND ----------

cols = ["price", "zipcode", "sqft_lot"]
houses[cols]

# COMMAND ----------


