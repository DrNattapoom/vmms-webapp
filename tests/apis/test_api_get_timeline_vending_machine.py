"""Test: Get Stock Timeline by Vending Machine API."""

import pytest
from flask.testing import FlaskClient

END_POINT = "/api/stock_records/timeline/vending_machines"


def test_get_timeline_vending_machine_status(client: FlaskClient):
    response = client.get(f"{END_POINT}/1")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "vending_machine",
    [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
)
def test_get_timeline_vending_machine_response_success(
    client: FlaskClient, vending_machine: dict
):
    response = client.get(f"{END_POINT}/{vending_machine['id']}")
    response_json = response.get_json()
    response_data = response_json["data"]
    assert response_data["get"]
    assert response_json["status"] == "success"
    assert (
        response_json["message"]
        == f"all stock records of vending machine {vending_machine['id']} are successfully retrieved"
    )
