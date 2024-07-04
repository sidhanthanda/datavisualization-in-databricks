# Databricks notebook source
import pandas as pd

book = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/bestsellers.csv")
book

# COMMAND ----------

book.shape
#550 rows x 7 columns

# COMMAND ----------

book.head()
#displaying the first 5 rows

# COMMAND ----------

book.head(19)
#displaying the first 19 rows

# COMMAND ----------

book.tail()
#displaying the last 5 rows

# COMMAND ----------

book.tail(2)
#displaying the last 2 rows

# COMMAND ----------

book.info()
#can see there are no null values
#column user rating was asigned a float64 datatype
#can see 3 columns with int64 datatype

# COMMAND ----------

mountev = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/mount_everest_deaths.csv")
mountev

# COMMAND ----------

mountev.shape
#we now know there are 310 rows and 8 columns

# COMMAND ----------

mountev.info()
# No., Name, and Date columns have no null values
# The Age column has the most null values

# COMMAND ----------

movie = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/movie_titles.tsv", sep = "\t")
movie
#had to google what character represented tabs in a tsv

# COMMAND ----------

header_names = ['id', 'title', 'year', 'imdb_rating', 'imdb_id', 'genres']
movie = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/movie_titles.tsv", sep = "\t", names = header_names, header = 0 )
movie

# COMMAND ----------

movie.tail(7)

# COMMAND ----------


