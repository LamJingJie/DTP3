# DTP3

Welcome to the DTP3 DDW Portion Webpage!

This website supplements our machine learning tasks in `DDW_DTP.ipynb`, which you can find inside this folder.

## Framework(s) Used
1. Flask
2. Bootstrap
3. SQL

## Setup Instructions

### 1. Install Virtual Environment

To install the virtual environment, run:
```sh
python -m pip install --user pipenv
```

### 2. Activate Virtual Environment

To activate the virtual environment, run:
```sh
pipenv shell
```

### 3. Install Dependencies

To install the required dependencies, run:
```sh
pipenv install
```

### 4. Set Up the Database

To set up the database, run:
```sh
flask db init
flask db migrate
flask db upgrade
```

You should see the following files/folders:
- `app.db`
- `migrations` folder

### 5. Run the Web Application

To run the web application, execute:
```sh
flask run --debug
```