import os
from dotenv import load_dotenv
from astrapy.db import AstraDB

load_dotenv()

db = AstraDB(
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
    namespace=os.environ["ASTRA_DB_KEYSPACE_NAME"],
)

print(db.collection(os.environ["ASTRA_DB_COLLECTION_NAME"]).find_one())