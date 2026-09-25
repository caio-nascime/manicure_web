import pytest
from app.__init__ import create_app

@pytest.fixture
def create_app_test():

    app = create_app("teste")
    return app


@pytest.fixture
def create_client(create_app_test):

    client = create_app_test.test_client()

    return client