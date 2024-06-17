from src.api_extractor import ApiExtractor
from src.data_loader import dataLoader

# https://data.smartdublin.ie/dataset/dublin-city-centre-footfall-counters/resource/8a570347-9541-4adc-a1eb-21323c733d58

if __name__ == "__main__":
    api_url = "https://data.smartdublin.ie/api/3/action/datastore_search?\
        resource_id=8a570347-9541-4adc-a1eb-21323c733d58&limit=5"

    api_extractor = ApiExtractor(api_url)
    df_pedestrian_footfall = api_extractor.extract_api()

    data_loader = dataLoader()
    data_loader.load_data(df_pedestrian_footfall)
    data_loader.print_data()
