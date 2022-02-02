# Databricks notebook source
import requests

def getNotebookContent(url, path, bearerToken):
  headers = {"Accept": "application/json", "Authorization": "Bearer " + bearerToken }
  data_path = '{ "path": "' + path + '", "format": "SOURCE", "direct_download": true }'
  response = requests.get(url, headers=headers, data=data_path)
  content = response.text
  return content

def searchNotebookContent(url, path, bearerToken, searchTerm):
  content = getNotebookContent(url, path, bearerToken)
  result = content.find(searchTerm)
  return result

# COMMAND ----------

exportUri = '/api/2.0/workspace/export'
listUri = '/api/2.0/workspace/list'

# COMMAND ----------

import requests
import json
from ast import literal_eval

def searchNotebooks(relativePath, searchTerm, bearerToken):
 headers = {"Authorization": "Bearer " + bearerToken }
 data_path = '{{"path": "{0}"}}'.format(relativePath)
 url = f'{instanceName}{listUri}'
 response = requests.get(url, headers=headers, data=data_path)
 # Raise exception if a directory or URL does not exist.
 response.raise_for_status()
 jsonResponse = response.json()
 for i, result in jsonResponse.items():
   for value in result:
    data = literal_eval(json.dumps(value))
    if data['object_type'] == 'DIRECTORY':
     # Iterate through all folders.
     searchNotebooks(data['path'], searchTerm, bearerToken)
    elif data['object_type'] == 'NOTEBOOK':
      if 'DB-WS-Notebooks-Search' not in data['path'] and searchNotebookContent(f'{instanceName}{exportUri}', data['path'], bearerToken, searchTerm) > -1:
        print(data['path'])
      else:
        pass
    else:
     # Skip imported libraries.
     pass