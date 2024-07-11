# Databricks notebook source
import pandas as pd
import numpy as np
import math

# COMMAND ----------

# MAGIC %md
# MAGIC ## Path

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

# COMMAND ----------

df_house = 

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC ## mean

# COMMAND ----------

df["price"]

# COMMAND ----------

df["price"].mean()

# COMMAND ----------

df["date"].mean()

# COMMAND ----------

df["price"].mean(numeric_only=True)

# COMMAND ----------

df["price"].mean(numeric_only=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Max

# COMMAND ----------

df["price"].max()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Idxmin

# COMMAND ----------

df["price"].idxmin()

# COMMAND ----------

df["price"].min()

# COMMAND ----------

df.head(1150)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Idxmax

# COMMAND ----------

df["price"].idxmax()

# COMMAND ----------

df.head(7253)

# COMMAND ----------

# MAGIC %md
# MAGIC ## loc & iloc

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

thing = df.iloc[4]


# COMMAND ----------

df

# COMMAND ----------



# COMMAND ----------

df["price"].diff

# COMMAND ----------

df.price

# COMMAND ----------

import numpy as np
import pandas as pd

g = np.random.default_rng(0)
month = ["Sept", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]
random_integers = g.integers(70, 101, 10)
s = pd.Series(random_integers)
s.index = month
t1 = s[:5].mean()
t2 =  s[5:].mean()
s

#print(f'Yearly Average: {s.mean()}')
#print(f'Average for first 5 months: {s[:5].mean()}')
#print(f'Average for last 5 months: {s[5:].mean()}')
#print(f'Improvement: {t2 - t1}')
#print(f'Highest score in the year: {s.nlargest(5)}')


# COMMAND ----------

import numpy as np
import pandas as pd

g = np.random.default_rng(0)
month = ["Sept", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "August"]
random_integers = g.integers(50, 101, 12)
s = pd.Series(random_integers)
s.index = month
s

thing1 = s.mean()
thing2 = s.min()
thing3 = s.max()

print(thing1)
print(thing2)
print(thing3)

# COMMAND ----------

import numpy as np
import pandas as pd

# Initialize the random number generator
g = np.random.default_rng(0)

# Define the month variables
months = ["Sept", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "June"]

# Generate 10 random integers in the range 40 to 60
random_integers = g.integers(40, 60, 10)

# Create a Pandas Series with the random integers and set the index to the month names
s = pd.Series(random_integers, index=months)

# Calculate the mean of the scores
actual_mean = s.mean()

# Calculate the difference between 80 and the actual mean
difference = 80 - actual_mean

# Add the difference to each of the scores to scale them
scaled_scores = s + difference

# Print the original and scaled scores
print("Original scores:")
print(s)
print("\nScaled scores:")
print(scaled_scores)
print("\nMean of scaled scores:")
print(scaled_scores.mean())


# COMMAND ----------


