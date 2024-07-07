# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

# COMMAND ----------

w = titanic["sex"] == 'female'
died = titanic["survived"] == 0
titanic[w & died]

# COMMAND ----------

house

# COMMAND ----------

house[(house["waterfront"] == 1) & (house["price"] < 500000)]

# COMMAND ----------

house[(house["grade"] >= 11) & (house["view"]==4)]

# COMMAND ----------


