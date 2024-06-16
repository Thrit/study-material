import json
import requests

#load_dotenv()

# https://data.smartdublin.ie/dataset/dublin-city-centre-footfall-counters/resource/8a570347-9541-4adc-a1eb-21323c733d58

class DataLoader:
    def __init__(self, api_url):
        self.api_url = api_url

    def connect_api(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        return json.dumps(response.json())

    def print_data(self):
        data = self.connect_api()
        print(data)


if __name__=='__main__':
    api_url = 'https://data.smartdublin.ie/api/3/action/datastore_search?resource_id=8a570347-9541-4adc-a1eb-21323c733d58&limit=5&q=title:jones'  
    data_loader = DataLoader(api_url)
    data_loader.print_data()
