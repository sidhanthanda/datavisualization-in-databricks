# Databricks notebook source
import pandas as pd

df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
df2 = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
df3 = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

df3



# COMMAND ----------

df2.pclass.value_counts()

# COMMAND ----------

df2.pclass.value_counts().sort_values()

# COMMAND ----------

df2.pclass.value_counts().plot(kind="bar")

# COMMAND ----------

df2.pclass.value_counts().plot(kind="bar")

# COMMAND ----------

df2.pclass.value_counts().sort_values().plot(kind="bar")

# COMMAND ----------

df2.pclass.sort_values()

# COMMAND ----------

df2.pclass.value_counts().sort_index().plot(kind="bar")

# COMMAND ----------

df3['bedrooms'].value_counts()

# COMMAND ----------

df3['bedrooms'].value_counts().plot()

# COMMAND ----------

df3['bedrooms'].value_counts().plot(kind="bar")

# COMMAND ----------

df3['bedrooms'].value_counts().sort_values().plot(kind="bar")

# COMMAND ----------

df3['bedrooms'].value_counts().sort_index()

# COMMAND ----------


