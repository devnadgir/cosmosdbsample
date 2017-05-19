---
platforms: python
author: dkn
---

# Azure Cosmos DB - Quick Sample

## Azure Cosmos DB Architecture

* Top 3 key attributes of Azure Cosmos DB that we should take note architecturally.
 1. Globally distributed without any management overhead.
 2. Multi-model and Multi API
	- Model brings the a schema agnostic data view
		- e.g., key-value, columnar-family, document and graph
	- APIs, use different ways to interact with the natural resource (data)
		- currently : SQL, MongoDB API, Tables API and Gremlin graph API
 3. Guaranteed single-digit latency with a committed SLA :)

## Using this code

* Make sure you have the relevant python distribution that works on your system. 
* Python needs the document DB SDK.
	- If you already know this, doing a 'pip install pydocumentdb' will set your environment up.
	- Otherwise, more details at https://pypi.python.org/pypi/pydocumentdb
* Open the cosmos-db-sql.py and update at the configuration variables.
* Run the code using 'python cosmos-db-sql.py'

## About the code

* This code is for illustrative purposes and to get a quick working sample only.
* It creates and initiatlizes a database if a database is already present.
* Creates a collection ( or initialize one if already present ).
* Create or update buckets of data. You control how much data you want to stress.
* Provided 'as-is' :).

## References

- [Cosmos DB Introduction](https://docs.microsoft.com/azure/cosmos-db/introduction)
- [Want to dig code further ?](https://github.com/Azure/azure-documentdb-python/tree/master/samples)