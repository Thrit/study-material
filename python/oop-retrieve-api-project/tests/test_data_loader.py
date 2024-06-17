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
    assert str(loader.engine) == str(mock_engine)
