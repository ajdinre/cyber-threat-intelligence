# Cyber Threat Intelligence

A Django application for analyzing Apache logs for possible Denial-of-service attacks.

## Detecting Dos Attacks
//TODO


## How to run this app

1. Install Postgres and Python

2. Start the Postgres service

On Linux:
```
$ sudo systemctl start postgresql.service
```

3. Create a database "cti_db" in Postgres
```
$ sudo postgresql-setup initdb          #initialize PG cluster
$ sudo -iu postgres                     #switch to postgres user
$ psql                                  #enter psql as postgres user
psql (12.5)
Type "help" for help.

postgres=# CREATE DATABASE cti_db;
postgres=# CREATE USER cti_user WITH ENCRYPTED PASSWORD 'cti_password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE cti_db TO cti_user;
```
4. Clone this repository and enter it
```
$ git clone https://github.com/ajdintrejic/cyber-threat-intelligence.git
$ cd cyber-threat-intelligence
```

5. Install the  pip packages from requirements.txt 
```
$ pip install -r requirements.txt
```

7. Enter the Django directory and migrate
```
$ cd django_project
$ python manage.py migrate
```

8. Start the server
```
$ python manage.py runserver
```

## Bug reporting
Please submit any bugs you encounter to GitHub Issues
