# Databricks notebook source
import matplotlib.pyplot as plt
import pandas as pd

d = [x * 10 for x in range(10)]
d

# COMMAND ----------

labels = [f'{x}!' for x in range(10)]

labels

# COMMAND ----------

plt.plot(d);

# COMMAND ----------

plt.plot(labels, d)

plt.show()

# COMMAND ----------

df = pd.DataFrame(d, labels).assign(series2 = lambda x: x[0]/2)

df.head()

# COMMAND ----------

plt.plot(df)

# COMMAND ----------

""
