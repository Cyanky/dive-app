# Dive
A musicial web app to help musicians upload their information and let listeners find specific songs and musicians.
  
  *** This app has been deployed to Heroku, check this url: https://dive-app.herokuapp.com/
# Overview  
## Tech Stack
Tech stack includes:

- SQLAlchemy ORM to be my ORM library of choice.
- PostgreSQL as my database of choice.
- Python3 and Flask as my server-side language and server-side framework.
- Flask-Migrate for creating and running schema migrations.
- HTML, CSS, and Javascript for the website's frontend.

## Main Files: Project Structure
```
├── README.md
├── app.py ***  Main driver of the app. Includes SQLAlchemy models.
├── error.log
├── forms.py *** Web forms
├── requirements.txt *** Project dependencies.
├── static *** Website Frontend files.
│   ├── css
│   ├── uploads
│   └── js
└── templates
    ├── errors
    ├── forms
    ├── layouts
    └── pages  
```  
    
## Getting Started

### Installation

Make sure to be in the root directory of the project and that you have Python 3.6 or above installed.

#### Create Virtual Environment

Run the following to create a virtual environment:

```
python3 -m venv env
```

Activate your newly created virtual environment by running:

```
source env/bin/activate
```

#### Installing Dependencies

To install all project's dependencies, simply run:

```
pip install -r requirements.txt
```

### Database Configuration

Make sure to have PostgreSQL installed, if it is not, execute:

```
sudo apt-get -y install postgresql
```

#### Create Database

First, start your PostgreSQL database server by running:

```
sudo service postgresql start
```

Then, create your project's database by running:

```
createdb <database_name>
```

Lastly, replace your database url in app.py #Set database url# session:

```
postgresql://username:password@localhost:5432/database
```

#### Apply Database Schema

Using migrations, apply the database schema and relationships by executing:

```
flask db migrate
flask db upgrade
```

### Running the Server

Prepare the development environment by executing:

```
export FLASK_APP=app
export FLASK_ENV=development
```

To run the server at any time, use:

```
flask run
```

This will run the server on [http://localhost:5000](http://localhost:5000/) in development mode.
