"""Test: Save Stock Records API."""

import pytest
from flask.testing import FlaskClient

END_POINT = "/api/stock_records/save"


@pytest.mark.parametrize(
    "product_stocks",
    [
        {
            "vending_machine": {"id": 1, "name": "vm_001", "location": "loc_001"},
            "prod_id": 1,
            "stock": 100,
        },
        {
            "vending_machine": {"id": 2, "name": "vm_002", "location": "loc_002"},
            "prod_id": 2,
            "stock": 200,
        },
        {
            "vending_machine": {"id": 3, "name": "vm_003", "location": "loc_003"},
            "prod_id": 3,
            "stock": 300,
        },
    ],
)
def test_set_up(client: FlaskClient, product_stocks: dict):
    client.post("/api/vending_machines/add", data=product_stocks["vending_machine"])
    response = client.post(
        f"/api/product_stocks/add/{product_stocks['vending_machine']['id']}",
        data=product_stocks,
    )
    assert response.status_code == 200


def test_save_stock_records_status(client: FlaskClient):
    response = client.post(END_POINT)
    assert response.status_code == 200


def test_save_stock_records_response_success(client: FlaskClient):
    response = client.post(END_POINT)
    response_json = response.get_json()
    response_data = response_json["data"]
    assert response_data["post"]
    assert response_json["status"] == "success"
    assert response_json["message"] == "current stocks are successfully recorded"


@pytest.mark.parametrize("vending_machine", [{"id": 1}, {"id": 2}, {"id": 3}])
def test_tear_down(client: FlaskClient, vending_machine: dict):
    response = client.post(f"/api/vending_machines/delete/{vending_machine['id']}")
    assert response.status_code == 200
