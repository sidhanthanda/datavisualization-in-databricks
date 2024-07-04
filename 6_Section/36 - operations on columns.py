# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
titanic.head()

# COMMAND ----------

titanic.name
#easier to type than titanic['name']

# COMMAND ----------

type(titanic.name)

# COMMAND ----------

titanic['name']
#works the same as tianic.name, but this will work in all circumstances

# COMMAND ----------

titanic["name"]
#double quotes work the same way

# COMMAND ----------

titanic

# COMMAND ----------

titanic.home.dest
#dot notataion doesnt't work, causes an  error

# COMMAND ----------

titanic["home.dest"]
#works with square brackets

# COMMAND ----------

column_var = "sibsp"
titanic.column_var
#will give an error

# COMMAND ----------

titanic[column_var]
#will run properly

# COMMAND ----------

titanic.head()
#shows everything normally

# COMMAND ----------

titanic.head
#refers to .head method but is typed wrong

# COMMAND ----------


