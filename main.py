import os

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

from blobio import BlobIO

load_dotenv()

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

stream = BlobIO(
    blob=blob_service_client,
    container=os.getenv("container"),
    filename=os.getenv("filename"),
)

print(stream.read())
