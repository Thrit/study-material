import os
import json
import requests

from datetime import datetime
from dotenv import load_dotenv

from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from azure.keyvault.secrets import SecretClient

load_dotenv()

execution_datetime = f'{datetime.now():%Y-%m-%d-%H%M%S}'

storage_connection_string = os.environ['AZURE_STORAGE_CONNECTION_STRING']
vault_url = os.environ['AZURE_KEY_VAULT_URL']
tenant_id = os.environ['AZURE_TENANT_ID']
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

client = SecretClient(vault_url=vault_url, credential=credential)
secret_properties = client.get_secret('storage-account-connection-string')

url = r'https://data.smartdublin.ie/mobybikes-api/last_reading/'
api_response = requests.get(url)
json_api_data = json.dumps(api_response.json())

blob_service_client = BlobServiceClient.from_connection_string(secret_properties.value)
containers = blob_service_client.list_containers()

container_client = blob_service_client.get_container_client('landing-zone')

blob_client = container_client.get_blob_client(f'{execution_datetime}_ebike_dublin.json')
blob_client.upload_blob(json_api_data, overwrite=True)
