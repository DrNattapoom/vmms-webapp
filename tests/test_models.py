"""Test: Models."""
from datetime import datetime

import pytest

from vmms_webapp.models.product import Product
from vmms_webapp.models.stock import Stock
from vmms_webapp.models.stock_record import StockRecord
from vmms_webapp.models.vending_machine import VendingMachine


@pytest.mark.parametrize(
    "vending_machines",
    [
        {"id": 1, "name": "vm_001", "location": "loc_001"},
        {"id": 2, "name": "vm_002", "location": "loc_002"},
        {"id": 3, "name": "vm_003", "location": "loc_003"},
    ],
)
def test_vending_machine_repr(vending_machines: dict):
    vending_machine = VendingMachine(
        vending_machines["name"], vending_machines["location"]
    )
    vending_machine.id = vending_machines["id"]
    assert (
        str(vending_machine)
        == f"<VendingMachine {vending_machines['id']}: {vending_machines['name']}>"
    )


@pytest.mark.parametrize(
    "vending_machines",
    [
        {"id": 1, "name": "vm_001", "location": "loc_001"},
        {"id": 2, "name": "vm_002", "location": "loc_002"},
        {"id": 3, "name": "vm_003", "location": "loc_003"},
    ],
)
def test_vending_machine_eq(vending_machines: dict):
    vending_machine_a = VendingMachine(
        vending_machines["name"], vending_machines["location"]
    )
    vending_machine_a.id = vending_machines["id"]
    vending_machine_b = VendingMachine(
        vending_machines["name"], vending_machines["location"]
    )
    vending_machine_b.id = vending_machines["id"]
    assert vending_machine_a == vending_machine_b
    vending_machine_a.id = vending_machines["id"] + 1
    assert vending_machine_a != vending_machine_b


@pytest.mark.parametrize(
    "vending_machines",
    [
        {"id": 1, "name": "vm_001", "location": "loc_001"},
        {"id": 2, "name": "vm_002", "location": "loc_002"},
        {"id": 3, "name": "vm_003", "location": "loc_003"},
    ],
)
def test_vending_machine_to_dict(vending_machines: dict):
    vending_machine = VendingMachine(
        vending_machines["name"], vending_machines["location"]
    )
    vending_machine.id = vending_machines["id"]
    assert vending_machine.to_dict() == vending_machines


@pytest.mark.parametrize(
    "products",
    [
        {"id": 1, "name": "prod_001", "price": 10},
        {"id": 2, "name": "prod_002", "price": 20},
        {"id": 3, "name": "prod_003", "price": 30},
    ],
)
def test_product_repr(products: dict):
    product = Product(products["id"], products["name"], products["price"])
    assert str(product) == f"<Product {products['id']}: {products['name']}>"


@pytest.mark.parametrize(
    "products",
    [
        {"id": 1, "name": "prod_001", "price": 10},
        {"id": 2, "name": "prod_002", "price": 20},
        {"id": 3, "name": "prod_003", "price": 30},
    ],
)
def test_product_eq(products: dict):
    product_a = Product(products["id"], products["name"], products["price"])
    product_b = Product(products["id"], products["name"], products["price"])
    assert product_a == product_b
    product_a.id = products["id"] + 1
    assert product_a != product_b


@pytest.mark.parametrize(
    "products",
    [
        {"id": 1, "name": "prod_001", "price": 10},
        {"id": 2, "name": "prod_002", "price": 20},
        {"id": 3, "name": "prod_003", "price": 30},
    ],
)
def test_product_to_dict(products: dict):
    product = Product(products["id"], products["name"], products["price"])
    assert product.to_dict() == {"name": products["name"], "price": products["price"]}


@pytest.mark.parametrize(
    "products",
    [
        {"id": 1, "name": "prod_001", "price": 10},
        {"id": 2, "name": "prod_002", "price": 20},
        {"id": 3, "name": "prod_003", "price": 30},
    ],
)
def test_product_hash(products: dict):
    assert hash(Product(products["id"], products["name"], products["price"])) == hash(
        products["id"]
    )


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_repr(product_stock: dict):
    stock = Stock(
        product_stock["vm_id"], product_stock["prod_id"], product_stock["stock"]
    )
    assert (
        str(stock)
        == f"<Stock {(product_stock['vm_id'], product_stock['prod_id'])}: {product_stock['stock']}>"
    )


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_eq(product_stock: dict):
    stock_a = Stock(
        product_stock["vm_id"], product_stock["prod_id"], product_stock["stock"]
    )
    stock_b = Stock(
        product_stock["vm_id"], product_stock["prod_id"], product_stock["stock"]
    )
    assert stock_a == stock_b
    stock_a.vm_id = product_stock["vm_id"] + 1
    assert stock_a != stock_b


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_to_dict(product_stock: dict):
    stock = Stock(
        product_stock["vm_id"], product_stock["prod_id"], product_stock["stock"]
    )
    assert stock.to_dict() == product_stock


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_record_repr(product_stock: dict):
    time_stamp = datetime.utcnow()
    stock_record = StockRecord(
        product_stock["vm_id"],
        product_stock["prod_id"],
        product_stock["stock"],
        time_stamp,
    )
    assert (
        str(stock_record)
        == f"<StockRecord {(time_stamp, product_stock['vm_id'], product_stock['prod_id'])}: {product_stock['stock']}>"
    )


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_record_eq(product_stock: dict):
    time_stamp = datetime.utcnow()
    stock_record_a = StockRecord(
        product_stock["vm_id"],
        product_stock["prod_id"],
        product_stock["stock"],
        time_stamp,
    )
    stock_record_b = StockRecord(
        product_stock["vm_id"],
        product_stock["prod_id"],
        product_stock["stock"],
        time_stamp,
    )
    assert stock_record_a == stock_record_b
    stock_record_a.time_stamp = datetime(2020, 1, 1)
    assert stock_record_a != stock_record_b


@pytest.mark.parametrize(
    "product_stock",
    [
        {"vm_id": 2, "prod_id": 2, "stock": 200},
        {"vm_id": 3, "prod_id": 3, "stock": 300},
    ],
)
def test_stock_record_to_dict(product_stock: dict):
    time_stamp = datetime.utcnow()
    stock_record = StockRecord(
        product_stock["vm_id"],
        product_stock["prod_id"],
        product_stock["stock"],
        time_stamp,
    )
    assert stock_record.to_dict() == {"time_stamp": time_stamp} | product_stock
