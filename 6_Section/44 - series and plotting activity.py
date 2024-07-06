# Databricks notebook source
import pandas as pd
book = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/bestsellers.csv")
book

# COMMAND ----------

book["Name"]
type(book["Name"])
#checking to see if it returns a series

# COMMAND ----------

book["User Rating"]
type(book["User Rating"])
#checking to see if it returns a series

# COMMAND ----------

book.Genre.unique()
#shows unique types

# COMMAND ----------

book.Author.nunique()
#shows amount of unique values

# COMMAND ----------

book.Price.value_counts(ascending=False)

# COMMAND ----------

book['Name'].value_counts().nlargest(3)


# COMMAND ----------

# DBTITLE 1,()
cols = ['Author', 'Reviews']
book[cols]

# COMMAND ----------

book.Genre.value_counts().plot(kind = "pie")

# COMMAND ----------


