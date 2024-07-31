# Databricks notebook source
#underscores can be used instead of commas for large numbers

thing = 115635454135415312
thing2 = 115_635_454_135_415_312
print(thing)
print(thing2)
#the output will be the same for both

# COMMAND ----------

#scientific notation
t1 = 3e4
print(t1)
t2 = 3E4 #having caps e changes nothing
print(t2)
t3 = 3e-4
print(t3)
print(0.0000000000000000000000000000000256) #very large/small strings are autowritten in scientific notation

# COMMAND ----------

#octal numbers
print(0o123)

# COMMAND ----------

#hexadecimal numbers
print(0x123)

# COMMAND ----------


