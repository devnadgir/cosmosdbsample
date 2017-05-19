---
platforms: python
author: devnadgir
---

# Azure Cosmos DB


## Using this code

* Make sure you have the relevant python distribution that works on your system. 
* Python needs the document DB SDK.
	- if you already know this, doing a 'pip install pydocumentdb' will set your environment up.
	- Otherwise, more details at https://pypi.python.org/pypi/pydocumentdb
* Open the cosmos-db-sql.py and update at the configuration variables.
* Run the code using 'python cosmos-db-sql.py'

## About the code

* This code is for illustrative purposes and to get a quick working sample only.
* It creates and initiatlizes a database if a database is already present.
* Creates a collection ( or initialize one if already present ).
* Create or update buckets of data. You control how much data you want to stress.
* Provided 'as-is' :). 