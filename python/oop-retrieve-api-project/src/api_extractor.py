import json
import requests
import pandas as pd

from datetime import datetime


class ApiExtractor:
    """
    A class to extract, transform, and export data from an API.
    """

    def __init__(self, api_url: str) -> None:
        """
        Initialize the ApiExtractor with the given API URL.

        Parameters:
        api_url (str): The URL of the API to extract data from.
        """
        self.api_url = api_url

    def extract_api(self) -> pd.DataFrame:
        """
        Extract data from the API and convert it to a pandas DataFrame.

        Returns:
        pd.DataFrame: DataFrame containing the extracted data.
        """
        response = requests.get(self.api_url)
        response.raise_for_status()
        return self.__json_to_dataframe(response.json())

    def __json_to_dataframe(self, json_data: json) -> pd.DataFrame:
        """
        Convert JSON data to a pandas DataFrame.

        Parameters:
        json_data (dict): JSON data to be converted.

        Returns:
        pd.DataFrame: DataFrame containing the JSON data.
        """
        data = pd.DataFrame(json_data["result"]["records"])
        return self.__data_preparation(data)

    def __data_preparation(self, data: pd.DataFrame) -> pd.DataFrame:
        def convert_date_format(value: str) -> str:
            date_format = r"%Y-%m-%dT%H:%M:%S"
            return datetime.strptime(value, date_format).strftime(r"%Y-%m-%d")

        data.columns = data.columns.str.lower()
        data["time"] = data["time"].apply(convert_date_format)
        return data

    def export_data(self, data: pd.DataFrame) -> None:
        """
        Export the data to a CSV file.

        Parameters:
        data (pd.DataFrame): DataFrame containing the data to be exported.
        """
        data.to_csv(r"data/file.csv", index=False, sep=";")
