# Databricks notebook source
# MAGIC %run "./Includes/Notebooks-Search-Utilities"

# COMMAND ----------

dbutils.widgets.text(label='Search Term', name='search_term', defaultValue='')
dbutils.widgets.text(label='Instance Name', name='instance_name', defaultValue='')
dbutils.widgets.text(label='Bearer Token', name='bearer_token', defaultValue='')

# COMMAND ----------

instanceName = dbutils.widgets.get("instance_name")
if len(instanceName.strip()) == 0:
  raise Exception("Parameter Instance Name is required!")

bearerToken = dbutils.widgets.get("bearer_token")
if len(bearerToken.strip()) == 0:
  raise Exception('Auth Parameter Bearer Token is required!')

search_term = dbutils.widgets.get("search_term")
if bool(search_term and not search_term.isspace()):
  searchNotebooks('/', search_term, bearerToken)
else:
  print('Nothing to search. Please Enter a term!')