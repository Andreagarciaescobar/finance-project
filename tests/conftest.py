"""Pytest configuraion file"""

import pytest

from finance_project.main import app
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
def mock_expected_stock_list():
    return [
            {"name": "Apple Company", "price": 102, "code": "AAPL.US"},
            {"name": "Microsoft Company", "price": 78, "code": "MICRO.US"},
            {"name": "Google Company", "price": 92, "code": "GGLE.US"}
    ]

