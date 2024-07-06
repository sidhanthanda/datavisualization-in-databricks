# Databricks notebook source
import pandas as pd
wh = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
wh



# COMMAND ----------

wh["Healthy life expectancy"]

# COMMAND ----------

wh.set_index("Country name", "inplace = True")


# COMMAND ----------

wh

# COMMAND ----------

wh["Healthy life expectancy"]

# COMMAND ----------

wh["Healthy life expectancy"].head(18).plot()

# COMMAND ----------


