import os
import sys

sys.path.append("../")
import pandas as pd
import pytest

from dotenv import load_dotenv
from sqlalchemy import create_engine
from unittest.mock import patch
from src.data_loader import dataLoader

load_dotenv()

# Sample DataFrame for testing
sample_data = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "gender": ["F", "M", "M"],
    }
)


# Environment variables setup
@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    monkeypatch.setenv("TEST_POSTGRES_USER", os.environ["TEST_POSTGRES_USER"])
    monkeypatch.setenv("TEST_POSTGRES_PASSWORD", os.environ["TEST_POSTGRES_PASSWORD"])
    monkeypatch.setenv("TEST_POSTGRES_DB", os.environ["TEST_POSTGRES_DB"])
    monkeypatch.setenv("TEST_POSTGRES_HOST", os.environ["TEST_POSTGRES_HOST"])
    monkeypatch.setenv("TEST_POSTGRES_PORT", os.environ["TEST_POSTGRES_PORT"])


@pytest.fixture
def mock_engine(mocker):
    test_postgres_user = os.environ["TEST_POSTGRES_USER"]
    test_postgres_password = os.environ["TEST_POSTGRES_PASSWORD"]
    test_postgres_db = os.environ["TEST_POSTGRES_DB"]
    test_postgres_host = os.environ["TEST_POSTGRES_HOST"]
    test_postgres_port = os.environ["TEST_POSTGRES_PORT"]
    engine = create_engine(
        f"postgresql://{test_postgres_user}:{test_postgres_password}@{test_postgres_host}:{test_postgres_port}/{test_postgres_db}"
    )
    mocker.patch("src.data_loader.dataLoader", return_value=engine)
    return engine


def test_create_connection(mock_engine):
    loader = dataLoader()
    assert loader.engine == mock_engine


def test_load_data(mock_engine):
    loader = dataLoader()
    loader.load_data(sample_data)
    result = pd.read_sql_query("SELECT * FROM test", loader.engine)
    assert len(result) == 3
    assert result.iloc[0]["name"] == "Alice"
    assert result.iloc[1]["name"] == "Bob"
    assert result.iloc[2]["name"] == "Charlie"


def test_print_data(mocker, capsys):
    loader = dataLoader()
    loader.load_data(sample_data)
    loader.print_data()
    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "Charlie" in captured.out
