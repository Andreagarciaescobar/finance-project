"""Test cases for main module"""

def test_get_stocks(test_client, mock_expected_stock_list):

    response = test_client.get("/stocks")

    assert response.status_code == 200
    assert response.json() == mock_expected_stock_list