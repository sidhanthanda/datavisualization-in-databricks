# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

# COMMAND ----------

titanic[titanic["sex"] == "female"].survived.value_counts()

# COMMAND ----------

titanic[titanic["sex"] == "male"].survived.value_counts()


# COMMAND ----------

women = titanic["sex"] == "female"
titanic[women].survived.value_counts().plot(kind="pie")

# COMMAND ----------

women = titanic["sex"] == "female"
titanic[~women].survived.value_counts().plot(kind="pie")

# COMMAND ----------

house[house["price"] > 5000000].zipcode.value_counts().plot(kind = "bar")

# COMMAND ----------

house.zipcode.value_counts().head(10).plot(kind = "bar")

# COMMAND ----------


