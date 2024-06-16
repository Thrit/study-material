import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

class dataLoader:
    def __init__(self) -> None:
        postgres_user = os.environ["POSTGRES_USER"]
        postgres_password = os.environ["POSTGRES_PASSWORD"]
        postgres_db = os.environ["POSTGRES_DB"]
        postgres_host = os.environ["POSTGRES_HOST"]
        postgres_port = os.environ["POSTGRES_PORT"]

        self.engine = self.__create_connection(
            postgres_user, postgres_password, postgres_db, postgres_host, postgres_port
        )

    def load_data(self, data: pd.DataFrame) -> None:
        data.to_sql('test', self.engine, if_exists='replace', index=False)
    
    def print_data(self):
        print(pd.read_sql_query("SELECT * FROM test", self.engine))

    def __create_connection(
        self,
        postgres_user,
        postgres_password,
        postgres_db,
        postgres_host,
        postgres_port,
    ) -> create_engine:
        return create_engine(
            f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
        )
