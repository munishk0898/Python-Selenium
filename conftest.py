from data import Webpage_elements
import pytest


@pytest.fixture(scope='session')
def config_data():
    data = Webpage_elements
    return data
