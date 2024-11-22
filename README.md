# DTP3

Welcome to the DTP3 DDW Portion Webpage!

This website supplements our machine learning tasks in `DDW_DTP.ipynb`, which you can find inside this folder.

## Framework(s) Used
- Flask
- Bootstrap
- SQL

## Setup Instructions

### 1. Install Virtual Environment

To install the virtual environment, run:
```sh
python -m pip install --user pipenv
```

> **Note:** If you encounter a warning about the script location, you may need to add the installation directory to your PATH. To do that, run the following command:
> ```sh
> export PATH='/voc/work/.local/bin':$PATH
> ```

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