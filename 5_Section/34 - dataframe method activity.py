# Databricks notebook source
import pandas as pd
books = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/bestsellers.csv")
books

# COMMAND ----------

books.max()
#we can see the highest price is 105.

# COMMAND ----------

books.mean()
#we can see the average user rating

# COMMAND ----------

first5 = books.head()
first5.mean()

# COMMAND ----------

books.mode()
#we can see the user review score that appeared the most was 4.8

# COMMAND ----------

review = books.Reviews
#saving the reviews column as a variable
review.sum()
#summing the variable

# COMMAND ----------

writer = books.Author
writer.count()

# COMMAND ----------

max = writer.max()
#this guy was the writer that wrote the most books

# COMMAND ----------


