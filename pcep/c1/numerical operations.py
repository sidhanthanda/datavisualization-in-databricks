# Databricks notebook source
#addition
2 +3

# COMMAND ----------

#subrtaction
5-4

# COMMAND ----------

#multiplication
3 * 5

# COMMAND ----------

# normal division
answer = 18 / 2
dtype = type(answer)
print(dtype)
# even though 18 ÷ 2 is 9, python takes it as a float

# COMMAND ----------

# integer division
answer = 15 // 3 
dtype = type(answer)
print(dtype)
# using two slashes, the answer's datatype is an integer, not a float

# COMMAND ----------

#modulus division
6 % 3
#this gives us the remainder of the operation, in this case 0


# COMMAND ----------

7 % 3
# the remainder is 1

# COMMAND ----------

5 / 0
#will not run

# COMMAND ----------

#exponents
2 ** 2 #this will be equal to 4

# COMMAND ----------

2 **3 #this will be equal to 8

# COMMAND ----------

2 +3 #this is equal to 5, but
2 + 3.0 #is equal to 5.0, a float

# COMMAND ----------


