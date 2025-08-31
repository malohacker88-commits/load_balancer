import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient


from web.application import init_app


@pytest.fixture
def fastapi_app() -> FastAPI:
    """
    Фикстура для создания FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    return init_app()


@pytest.fixture
def client(fastapi_app):
    """
    Create a test client for our FastAPI application.
    """
    return TestClient(fastapi_app)
