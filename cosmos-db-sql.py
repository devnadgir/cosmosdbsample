import pydocumentdb, uuid, time;
import pydocumentdb.document_client as cosmosdb_client
import pydocumentdb.documents as documents
import pydocumentdb.errors as errors

config = { 
    'cosmosdb_endpoint': 'https://dkncosmos1.documents.azure.com',
    'primary_key': 'foAELnp9Vt4uBBIqHW4ojqfBIVR3ZN8EpbUBvIh6y8ox0gaNojUoSyrPkK9DiCEIavpKqQiiYRIJt6Py2v7IXCg==',
    'db': 'cosmicworld',
	'collection':'samples'
};

# Create a database, if not already present. If present, return a read handle for the DB resource.
def initiate_database(my_cosmos_client):
	cosmos_db_handle = None
	try:
		cosmos_db_handle =  my_cosmos_client.CreateDatabase({"id": config['db']})
		print('Created a new database with id \'{0}\'.'.format(config['db']))
	except errors.DocumentDBError as e:
		if e.status_code == 409:
			print('Initializing the database with id \'{0}\' ...'.format(config['db']))
			cosmos_db_handle = my_cosmos_client.ReadDatabase('dbs/'+config['db'])
		else:
			raise errors.HTTPFailure(e.status_code)            
	return cosmos_db_handle

def upload_data(my_cosmos_client, my_cosmos_db, num_of_docs):
	# Create a collection in the database ( if not already present ) and upload data.
	collection_options	= {'offerEnableRUPerMinuteThroughput': True,'offerVersion': "V2",'offerThroughput': 400} # This needs explanation :)
	try:
		my_collection = my_cosmos_client.CreateCollection(my_cosmos_db['_self'], { 'id': config['collection'] },collection_options)
	except errors.DocumentDBError as e: 
		if e.status_code == 409: #The collection resource exists, access it by its resource ID. 
			my_collection = my_cosmos_client.ReadCollection('dbs/'+config['db']+'/colls/'+config['collection'])
	start_time = time.clock() ;
	for i in range(num_of_docs):
		temp_record = { 'id': 'datakey'+str(i), 'data_random1': str(uuid.uuid4()), 'data_random2':str(uuid.uuid4())}
		try:
			temp_doc = my_cosmos_client.CreateDocument(my_collection['_self'],temp_record)
		except errors.DocumentDBError as e: #Remember everything is a 'resource'.
			if e.status_code == 409 : temp_doc = my_cosmos_client.ReplaceDocument('dbs/'+config['db']+'/colls/'+config['collection']+'/docs/'+temp_record['id'],temp_record)
		#if(temp_doc): print temp_doc
	print('Uploaded \'{0}\' documents. Delta time = \'{1}\' ...'.format(str(num_of_docs),str(time.clock() - start_time)))
		

if __name__ == "__main__":
	my_cosmos_client = cosmosdb_client.DocumentClient(config['cosmosdb_endpoint'], {'masterKey': config['primary_key']})
	my_cosmos_db = initiate_database(my_cosmos_client)
	if(my_cosmos_db):
		upload_data(my_cosmos_client, my_cosmos_db, 10)