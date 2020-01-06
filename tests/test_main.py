import pytest
from azure.storage.blob import BlobServiceClient

from blobio import BlobIO

connect_str = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite:10000/devstoreaccount1;"

dir = "dir"
filename = "file"
data = b"data"


@pytest.fixture
def blob_service_client():
    bsc = BlobServiceClient.from_connection_string(connect_str)
    bsc.create_container(dir)
    yield bsc
    bsc.delete_container(dir)


def test_test(blob_service_client):
    blob_client = blob_service_client.get_blob_client(container=dir, blob=filename)
    blob_client.upload_blob(data)

    stream = BlobIO(blob=blob_service_client, container=dir, filename=filename,)

    assert stream.read() == data
