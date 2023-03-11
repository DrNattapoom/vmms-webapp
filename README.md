[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DrNattapoom_vmms-webapp&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DrNattapoom_vmms-webapp)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DrNattapoom_vmms-webapp&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DrNattapoom_vmms-webapp)

# Vending Machine Management System

MUIC ICCS372 Software Engineering

# Repository Files

```
├── .github
│   └── workflow
│       └── python-tests.yml
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

# ER Diagram

<div align="center">
  <img src="https://user-images.githubusercontent.com/60769071/224496021-b83198ef-ac4a-465d-aca7-77ee1d54f9d0.png" alt="swe-vmms-project" style="border-radius: 5px;">
</div>
