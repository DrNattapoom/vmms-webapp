"""Test: Get Stock Timeline by Product API."""

import pytest
from flask.testing import FlaskClient

END_POINT = "/api/stock_records/timeline/products"


def test_get_timeline_product_status(client: FlaskClient):
    response = client.get(f"{END_POINT}/1")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "product",
    [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
)
def test_get_timeline_vending_machine_response_success(
    client: FlaskClient, product: dict
):
    response = client.get(f"{END_POINT}/{product['id']}")
    response_json = response.get_json()
    response_data = response_json["data"]
    assert response_data["get"]
    assert response_json["status"] == "success"
    assert (
        response_json["message"]
        == f"all stock records of product {product['id']} are successfully retrieved"
    )
