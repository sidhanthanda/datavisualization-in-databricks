# Databricks notebook source
#.value_counts() - shows the exact count of the selected column
#.sort_values() - sorts selected column in ascending order
#.sort_index() - sorts selected column in index by ascending order. 
#.plot() - makes graph

# COMMAND ----------

import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

# COMMAND ----------

titanic.pclass.value_counts()

# COMMAND ----------

titanic.pclass.value_counts().plot(kind="bar")

# COMMAND ----------

titanic.pclass.value_counts().sort_values().plot(kind="bar")

# COMMAND ----------

titanic.pclass.value_counts().sort_values()

# COMMAND ----------

titanic.pclass.value_counts().sort_values().plot(kind="bar")

# COMMAND ----------

house.shape

# COMMAND ----------

house.bedrooms.value_counts(ascending=True).plot(kind="bar")
#bar graph show you how many houses have the x axis amount of bedrooms.

# COMMAND ----------

house.bedrooms.value_counts().sort_values().plot(kind="bar")
#show how the .sort_values() makes it into ascending order without have ascending=True in the parameters.

# COMMAND ----------



# COMMAND ----------


