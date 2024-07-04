# Databricks notebook source
import pandas as pd
bestsellers = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/bestsellers.csv")


# COMMAND ----------

bestsellers.min()

# COMMAND ----------

bestsellers.mean()

# COMMAND ----------

bestsellers.head().mean()

# COMMAND ----------

bestsellers.describe(include="O")

# COMMAND ----------

bestsellers.describe(include="int64")

# COMMAND ----------

import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|", index_col=0)

titanic.head()

# COMMAND ----------

type(titanic.name)

# COMMAND ----------

titanic["name"]
name = titanic["name"]
name.shape

# COMMAND ----------

titanic.age

# COMMAND ----------

titanic.pclass

# COMMAND ----------



# COMMAND ----------

titanic["home.dest"]

# COMMAND ----------

unknown_thingy = "home.dest"
titanic[unknown_thingy]

# COMMAND ----------

titanic

# COMMAND ----------

type(titanic.mean())

# COMMAND ----------

titanic.sum

# COMMAND ----------

houses.sum()

# COMMAND ----------

houses.price

# COMMAND ----------

houses.price.sum()

# COMMAND ----------

houses.sum(numeric_only=True)

# COMMAND ----------

houses.price.min()

# COMMAND ----------

houses.price.max()

# COMMAND ----------

titanic["name"]
name = titanic["name"]
name.shape

# COMMAND ----------

titanic.shape

# COMMAND ----------

name.values

# COMMAND ----------

name.index

# COMMAND ----------

name

# COMMAND ----------

number_mins = houses.min(numeric_only=True)
number_mins.index

# COMMAND ----------

number_mins.index

# COMMAND ----------


