"""Utilities.

This script contains a collection of helper functions.
"""

from __future__ import annotations

import os
from datetime import datetime
from typing import TYPE_CHECKING

from flask import Request
from sqlalchemy.exc import IntegrityError

from vmms_webapp.models.product import Product
from vmms_webapp.models.stock import Stock
from vmms_webapp.models.stock_record import StockRecord
from vmms_webapp.models.vending_machine import VendingMachine

if TYPE_CHECKING:
    from vmms_webapp.database.database_service import DatabaseService

DATABASE_PATH = f"sqlite:///{str(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vending_machine.db'))}"


def populate_products(database_service: DatabaseService) -> None:
    """Populate database with predefined products.

    Args:
        database_service (DatabaseService): The object used to interact with database
    """
    try:
        with database_service.get_session().begin() as session:
            products = [
                Product(id=1, name="taro", price=20.0),
                Product(id=2, name="pringle", price=30.0),
                Product(id=3, name="lay's", price=50.0),
            ]
            session.add_all(products)
    except IntegrityError:
        pass
    except Exception as e:
        print("populate_products:", e)


def get_vending_machines(database_service: DatabaseService) -> list[VendingMachine]:
    """Get all vending machines in vending_machines table.

    Args:
        database_service (DatabaseService): The object used to interact with database

    Returns:
         list: A list of all vending machines in vending_machines table
    """
    session = database_service.get_session()()
    return session.query(VendingMachine).all()


def get_products(database_service: DatabaseService) -> list[Product]:
    """Get all products in products table.

    Args:
        database_service (DatabaseService): The object used to interact with database

    Returns:
        list: A list of all products in products table
    """
    session = database_service.get_session()()
    return session.query(Product).all()


def get_stock_records(database_service: DatabaseService) -> list[StockRecord]:
    """Get all stock records in stock_records table.

    Args:
        database_service (DatabaseService): The object used to interact with database

    Returns:
        list: A list of all stock records in stock_records table
    """
    session = database_service.get_session()()
    return session.query(StockRecord).all()


def get_vending_machine_by_id(
    database_service: DatabaseService, vm_id: int
) -> VendingMachine:
    """Get a vending machine with the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine

    Returns:
        VendingMachine: A vending machine with the specified id of vm_id
    """
    session = database_service.get_session()()
    return session.query(VendingMachine).filter(VendingMachine.id == vm_id).first()


def get_product_by_id(database_service: DatabaseService, prod_id: int) -> Product:
    """Get a product with the specified id of prod_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        prod_id (int): An id of the interested product

    Returns:
        Product: A product with the specified id of prod_id
    """
    session = database_service.get_session()()
    return session.query(Product).filter(Product.id == prod_id).first()


def get_stock_records_by_vm_id(
    database_service: DatabaseService, vm_id: int
) -> list[StockRecord]:
    """Get stock records with the specified vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine

    Returns:
        list: A stock record list with the specified vm_id
    """
    session = database_service.get_session()()
    return session.query(StockRecord).filter(StockRecord.vm_id == vm_id).all()


def get_stock_records_by_prod_id(
    database_service: DatabaseService, prod_id: int
) -> list[StockRecord]:
    """Get stock records with the specified prod_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        prod_id (int): An id of the interested product

    Returns:
        list: A stock record list with the specified prod_id
    """
    session = database_service.get_session()()
    return session.query(StockRecord).filter(StockRecord.prod_id == prod_id).all()


def get_stock_by_vm_id_and_prod_id(
    database_service: DatabaseService, vm_id: int, prod_id: int
) -> Stock:
    """Get a product stock with the specified ids of vm_id and prod_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine
        prod_id (int): An id of the interested product

    Returns:
        Stock: A vending machine with the specified ids of vm_id and prod_id.
    """
    session = database_service.get_session()()
    return (
        session.query(Stock)
        .filter(Stock.vm_id == vm_id, Stock.prod_id == prod_id)
        .first()
    )


def get_product_choices_by_vm_id(
    database_service: DatabaseService, vm_id: int
) -> list[Product]:
    """Get products that can be added to a vending machine of the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine

    Returns:
        list: A list of products that can be added to the vending machine vm_id
    """
    all_products = get_products(database_service)
    current_products = get_stocks_by_vm_id(database_service, vm_id).keys()
    current_products_ids = list(map(lambda product: product.id, current_products))
    return list(
        filter(
            lambda product: product.id not in current_products_ids,
            all_products,
        )
    )


def get_stocks_by_vm_id(
    database_service: DatabaseService, vm_id: int
) -> dict[Product, int]:
    """Get product stocks of a vending machine with the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine

    Returns:
        dict: A dictionary mapping a product to its stock representing product stocks of the vending machine vm_id
    """
    session = database_service.get_session()()
    results = (
        session.query(
            Stock.vm_id, Stock.prod_id, Product.name, Product.price, Stock.stock
        )
        .join(VendingMachine, VendingMachine.id == Stock.vm_id, isouter=True)
        .join(Product, Product.id == Stock.prod_id, isouter=True)
        .filter(Stock.vm_id == vm_id)
        .all()
    )
    stocks = {}
    for result in results:
        _, prod_id, name, price, stock = result
        stocks[Product(prod_id, name, price)] = stock
    return stocks


def create_vending_machine_from_request(request: Request) -> VendingMachine:
    """Create a vending machine from request.

    Args:
        request (Request): A request that from the client

    Returns:
        VendingMachine: A vending machine with the specified values of attributes
    """
    return VendingMachine(request.form["name"], request.form["location"])


def add_vending_machine(
    database_service: DatabaseService, vending_machine: VendingMachine
) -> dict:
    """Add a vending machine to vending_machine table.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vending_machine (VendingMachine): A vending machine that needs to be added to the table

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    session.add(vending_machine)
    session.commit()
    return {
        "status": "success",
        "data": {"post": {"id": vending_machine.id} | vending_machine.to_dict()},
        "message": f"vending machine {vending_machine.id} is successfully added",
    }


def update_vending_machine(
    database_service: DatabaseService, new_vending_machine: VendingMachine, vm_id: int
) -> dict:
    """Update attributes of a vending machine with the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        new_vending_machine (VendingMachine): A vending machine with the desired values of attributes
        vm_id (int): An id of the interested vending machine

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    vending_machine = (
        session.query(VendingMachine).filter(VendingMachine.id == vm_id).first()
    )
    vending_machine.name = new_vending_machine.name
    vending_machine.location = new_vending_machine.location
    session.commit()
    return {
        "status": "success",
        "data": {"post": {"id": vending_machine.id} | vending_machine.to_dict()},
        "message": f"vending machine {vending_machine.id} is successfully updated",
    }


def delete_vending_machine(database_service: DatabaseService, vm_id: int) -> dict:
    """Delete a vending machine with the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    vending_machine = (
        session.query(VendingMachine).filter(VendingMachine.id == vm_id).first()
    )
    session.delete(vending_machine)
    session.query(Stock).filter(Stock.vm_id == vending_machine.id).delete()
    session.commit()
    return {
        "status": "success",
        "data": None,
        "message": f"vending machine {vending_machine.id} is successfully deleted",
    }


def create_product_stock_from_request(
    request: Request, vm_id: int, prod_id: int = None
) -> Stock:
    """Create a product stock of a vending machine with the specified id of vm_id from request.

    Args:
        request (Request): A request that from the client
        vm_id (int): An id of the interested vending machine
        prod_id (int): An id of the interested product
            (default is None)
    Returns:
        Stock: A product stock of the vending machine vm_id
    """
    if not prod_id:
        prod_id = request.form["prod_id"]
    return Stock(vm_id, prod_id, request.form["stock"])


def add_product_stock(database_service: DatabaseService, product_stock: Stock) -> dict:
    """Add a product stock to stocks table.

    Args:
        database_service (DatabaseService): The object used to interact with database
        product_stock (Stock): A product stock that needs to be added to the table

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    session.add(product_stock)
    session.commit()
    return {
        "status": "success",
        "data": {"post": product_stock.to_dict()},
        "message": f"new product stock is successfully added to vending machine {product_stock.vm_id}",
    }


def update_product_stock(
    database_service: DatabaseService, new_product_stock: Stock
) -> dict:
    """Update attributes of a vending machine with the specified id of vm_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        new_product_stock (Stock): A product stock with the desired values of attributes

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    product_stock = (
        session.query(Stock)
        .filter(
            Stock.vm_id == new_product_stock.vm_id,
            Stock.prod_id == new_product_stock.prod_id,
        )
        .first()
    )
    product_stock.stock = new_product_stock.stock
    session.commit()
    return {
        "status": "success",
        "data": {"post": product_stock.to_dict()},
        "message": f"product {product_stock.prod_id} stock is successfully updated "
        f"in vending machine {product_stock.vm_id}",
    }


def delete_product_stock(
    database_service: DatabaseService, vm_id: int, prod_id: int
) -> dict:
    """Delete a product stock with the specified vm_id and prod_id.

    Args:
        database_service (DatabaseService): The object used to interact with database
        vm_id (int): An id of the interested vending machine
        prod_id (int): An id of the interested product

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    product_stock = (
        session.query(Stock)
        .filter(Stock.vm_id == vm_id, Stock.prod_id == prod_id)
        .first()
    )
    session.delete(product_stock)
    session.commit()
    return {
        "status": "success",
        "data": None,
        "message": f"product {product_stock.prod_id} is successfully deleted "
        f"from vending machine {product_stock.vm_id}",
    }


def save_stock_records(database_service: DatabaseService) -> dict:
    """Record current stocks.

    Args:
        database_service (DatabaseService): The object used to interact with database

    Returns:
        dict: A dictionary representing the response
    """
    session = database_service.get_session()()
    stocks = session.query(Stock).all()
    time_stamp = datetime.utcnow()
    stock_records = [
        StockRecord(stock.vm_id, stock.prod_id, stock.stock, time_stamp)
        for stock in stocks
    ]
    session.add_all(stock_records)
    session.commit()
    return {
        "status": "success",
        "data": {
            "post": list(
                map(
                    lambda stock_record: stock_record.to_dict(),
                    stock_records,
                )
            )
        },
        "message": "current stocks are successfully recorded",
    }
