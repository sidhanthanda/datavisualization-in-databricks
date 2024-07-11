# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix
house

# COMMAND ----------

recent = house[(house["yr_built"] >= 2014) | (house["yr_renovated"] >= 2014)]
recent.sort_values("yr_renovated")

# COMMAND ----------

netflix[(netflix["director"] == "David Fincher") | (netflix["director"] == "Martin Scorsese")]

# COMMAND ----------

netflix[netflix["director"].isin(["David Fincher", "Martin Scorsese"])]

# COMMAND ----------


