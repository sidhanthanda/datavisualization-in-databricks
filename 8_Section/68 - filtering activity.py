# Databricks notebook source
import pandas as pd

book = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/bestsellers.csv")
book

# COMMAND ----------

book[book["Author"] == "Pete Souza"]

# COMMAND ----------

book[book["Price"] < 10]


# COMMAND ----------

book[(book["Price"] >= 50) & (book["Price"] <= 60)]

# COMMAND ----------

book[(book["Author"] == "Kristin Hannah") | (book["Author"] == "Andy Weir") | (book["Author"] == "Delia Owens")]

# COMMAND ----------

book[(book["Genre"] == "Non Fiction") &  (book["User Rating"] == 4.9)]

# COMMAND ----------

fb = book[book["Genre"] == "Fiction"]
lowrating = fb["User Rating"].min()


fiction_low = fb[fb["User Rating"] == lowrating]
fiction_low

# COMMAND ----------

max_rating = book["User Rating"].max()  
book[(book["Year"] == 2012) & (book["User Rating"] == max_rating)]

# COMMAND ----------


