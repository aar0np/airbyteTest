import os, sys
from dotenv import load_dotenv
from astrapy.db import AstraDB
from langchain_openai import OpenAIEmbeddings

load_dotenv()

model = OpenAIEmbeddings()

db = AstraDB(
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
    namespace=os.environ["ASTRA_DB_KEYSPACE_NAME"],
)
collection = db.collection(os.environ["ASTRA_DB_COLLECTION_NAME"])

if (len(sys.argv) > 1):
    query = sys.argv[1]
else:
    query = "Kepler"

print(f'Query="{query}"')
vector = model.embed_query(query)
result = collection.vector_find_one(vector,fields=['title','img','alt'])

print(result)