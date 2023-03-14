[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DrNattapoom_vmms-webapp&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DrNattapoom_vmms-webapp)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DrNattapoom_vmms-webapp&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DrNattapoom_vmms-webapp)

# Vending Machine Management System

MUIC ICCS372 Software Engineering

# Repository Files

```
├── .github
│   └── workflow
│       └── python-tests.yml
├── docs
│   ├── dbdiagram
│   │   ├── er-diagram.dbml
│   │   └── er-diagram.png
│   └── openapi.yml
├── src
│   └── vmms-webapp
│       ├── database
│       │   ├── database_service.py
│       │   ├── utils.py
│       │   └── vending_machine.db
│       ├── models
│       │   ├── base.py
│       │   ├── product.py
│       │   ├── stock.py
│       │   └── vending_machine.py
│       ├── templates
│       │   ├── add.html
│       │   ├── base.html
│       │   ├── index.html
│       │   └── update.html
│       ├── app.py
│       └── config.py
├── tests
│   ├── apis
│   │   ├── test_api_add_product_stock.py
│   │   ├── test_api_add_vending_machine.py
│   │   ├── test_api_delete_product_stock.py
│   │   ├── test_api_delete_vending_machine.py
│   │   ├── test_api_update_product_stock.py
│   │   └── test_api_update_vending_machine.py
│   │── conftest.py
│   └── test_utils.py
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── checklist.md
├── poetry.lock
├── pyproject.toml
├── sonar-project.properties
└── tox.ini
```

# Project Setup

```
Python 3.9.13

Package Requirements
   -  flask
   -  sqlite3
   -  sqlalchemy
```

Please run the following command to install required dependencies.
```
poetry install
```
<b> Note: </b> Please make sure <code>poetry</code> is installed on your machine.

# Run

Please run app.py to start a webapp running on http://127.0.0.1:5000

```
python app.py
```

<b> Note: </b> The current working directory <b> must be </b> where the files are located.

# Run Tests

```
poetry run pytest
```

# APIs

APIs for managing vending machines and product stocks

### Vending Machines

Add a new vending machine
```
POST 	/api/vending_machines/add
```

Update a vending machine
```
POST 	/api/vending_machines/update/{vm_id}
```

Deletes a vending machine
```
POST 	/api/vending_machines/delete/{vm_id}
```

### Product Stocks

Add product stocks to a vending machine
```
POST 	/api/product_stocks/add/{vm_id}
```

Update product stock in a vending machine
```
POST 	/api/product_stocks/update/{vm_id}/{prod_id}
```

Delete a product stock from a vending machine
```
POST 	/api/product_stocks/delete/{vm_id}/{prod_id}
```

### Stock Records

Retrieve all stock records
```
GET 	/api/stock_records
```

Save current stock records
```
POST 	/api/stock_records/save
```

Retrieves timeline of stock records for a vending machine
```
GET 	/api/stock_records/timeline/vending_machines/{vm_id}
```

Retrieves the stock records timeline for a given product
```
GET     /api/stock_records/timeline/products/{prod_id}
```

For more information, please checkout the `docs/openapi.yml`.

# ER Diagram

<div align="center">
  <img src="https://user-images.githubusercontent.com/60769071/224496021-b83198ef-ac4a-465d-aca7-77ee1d54f9d0.png" alt="swe-vmms-project" style="border-radius: 5px;">
</div>
