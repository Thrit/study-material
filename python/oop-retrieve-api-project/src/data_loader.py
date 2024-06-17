import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class dataLoader:
    """
    Load data into a PostgreSQL database and retrieve data from it.
    """

    def __init__(self) -> None:
        """
        Initialize the dataLoader with a PostgreSQL.
        """
        postgres_user = os.environ["POSTGRES_USER"]
        postgres_password = os.environ["POSTGRES_PASSWORD"]
        postgres_db = os.environ["POSTGRES_DB"]
        postgres_host = os.environ["POSTGRES_HOST"]
        postgres_port = os.environ["POSTGRES_PORT"]

        self.engine = self.__create_connection(
            postgres_user, postgres_password, postgres_db, postgres_host, postgres_port
        )

    def load_data(self, data: pd.DataFrame) -> None:
        """
        Load data into the PostgreSQL table named 'test'.

        Parameters:
        data (pd.DataFrame): DataFrame containing the data to be loaded into the database.
        """
        data.to_sql("test", self.engine, if_exists="replace", index=False)

    def print_data(self):
        """
        Print the data from the PostgreSQL table named 'test'.
        """
        print(pd.read_sql_query("SELECT * FROM test", self.engine))

    def __create_connection(
        self,
        postgres_user,
        postgres_password,
        postgres_db,
        postgres_host,
        postgres_port,

    ) -> create_engine:
        """
        Create a SQLAlchemy engine connection to the PostgreSQL database.

        Parameters:
        postgres_user (str): PostgreSQL username.
        postgres_password (str): PostgreSQL password.
        postgres_db (str): PostgreSQL database name.
        postgres_host (str): PostgreSQL host.
        postgres_port (str): PostgreSQL port.

        Returns:
        create_engine: SQLAlchemy engine connected to the specified PostgreSQL database.
        """
        return create_engine(
            f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
        )
