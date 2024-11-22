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

If you are running the above commands in Vocareum, you may encounter the following message at the end of the installation.

WARNING: The script virtualenv is installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The scripts pipenv and pipenv-resolver are installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
It is basically saying that you need to add the newly installed pipenv program into the PATH so that you can use it from anywhere in the terminal. To do that, run the following command in the terminal.

export PATH='/voc/work/.local/bin':$PATH


### 2. Activate Virtual Environment

To activate the virtual environment, run:
```sh
python -m pipenv shell
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