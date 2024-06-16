import json
import requests
import pandas as pd

from datetime import datetime

class ApiExtractor:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def connect_api(self) -> json:
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()

    def json_to_dataframe(self, json_data: json) -> pd.DataFrame:
        data = pd.DataFrame(json_data["result"]["records"])
        data = self.__data_preparation(data)
        return data

    def __data_preparation(self, data: pd.DataFrame) -> pd.DataFrame:

        convert_date_format = lambda x: datetime.strptime(
            x, r"%Y-%m-%dT%H:%M:%S"
        ).strftime(r"%Y-%m-%d")

        data.columns = data.columns.str.lower()
        data["time"] = data["time"].apply(convert_date_format)
        return data

    def export_data(self, data: pd.DataFrame) -> None:
        data.to_csv(r"data/file.csv", index=False, sep=";")
