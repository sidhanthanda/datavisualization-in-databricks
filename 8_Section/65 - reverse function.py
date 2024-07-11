# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

# COMMAND ----------

df = titanic.head()
women = df.sex == 'female'
~women
df[~women]

# COMMAND ----------



# COMMAND ----------

newly_built = house["yr_built"] >=2014
newly_renovated = house["yr_renovated"] >= 2014
recent_homes = newly_built | newly_renovated
house[~recent_homes]

# COMMAND ----------



# COMMAND ----------

titanic[titanic.survived == 0]

# COMMAND ----------

titanic[~(titanic.survived == 0)]

# COMMAND ----------


