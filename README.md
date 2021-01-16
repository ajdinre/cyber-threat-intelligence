# Cyber Threat Intelligence

A Django application for analyzing Apache logs for possible Denial-of-service attacks.

## Detecting Dos Attacks
//TODO


## How to run this app

1. Install Postgres, Python3 and Neo4J

On Ubuntu:
```
sudo apt install neo4j-client postgresql python3 python-is-python3
```

2. Start the Postgres service

On Linux:
```
$ systemctl start postgresql.service
```

3. Create a database "cti_db" in Postgres
```
$ sudo -iu postgres                     #switch to postgres user
$ psql                                  #enter psql as postgres user
psql (12.5)
Type "help" for help.

postgres=# CREATE DATABASE cti_db;       #create the database with the instructions from db.sql
CREATE DATABASE
postgres=# 
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

9. Create a superuser account
```
$ python manage.py createsuperuser
```
This will propmt for information like username, email and password.


The app should now be running http://localhost:8000 and you should be able to log into it with the credentials from step 9.

## Bug reporting
Please submit any bugs you encounter to GitHub Issues
