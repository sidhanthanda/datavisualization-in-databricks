# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house

# COMMAND ----------

type(titanic[titanic.age == 18])

# COMMAND ----------

titanic[titanic.age == "18"]

# COMMAND ----------

titanic[titanic.pclass != 1]

# COMMAND ----------

titanic[titanic.pclass != 1].pclass.value_counts()

# COMMAND ----------

house[house["price"] > 5000000]

# COMMAND ----------

house[house["bedrooms"] >= 10 ]

# COMMAND ----------

house[house["sqft_living"] < 1000 ]

# COMMAND ----------

house[house["sqft_living"] < 500 ]

# COMMAND ----------


