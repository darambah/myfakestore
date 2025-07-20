import pytest
import requests

BASE_URL = "https://fakestoreapi.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def session():
    with requests.Session() as s:
        yield s
