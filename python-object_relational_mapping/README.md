# python-object_relational_mapping

This project covers connecting Python scripts to a MySQL database using
`MySQLdb`, and mapping Python classes to MySQL tables using the SQLAlchemy
ORM (Object-Relational Mapper).

## Learning Objectives

At the end of this project, you should be able to explain:

* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Requirements

* Ubuntu 20.04 LTS, `python3` (version 3.8.5)
* `MySQLdb` version 2.0.x
* `SQLAlchemy` version 1.4.x
* All files start with `#!/usr/bin/python3`, end with a new line, and are
  executable
* Code follows `pycodestyle` (version 2.7.*)
* Every module, class, and function has a documentation string
* `execute()` is not used with SQLAlchemy

## Installation

Install MySQL server:

```bash
sudo apt update
sudo apt install mysql-server
```

Install `MySQLdb`:

```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
```

Install `SQLAlchemy`:

```bash
sudo pip3 install SQLAlchemy==1.4.22
```

## Files

| File | Description |
| --- | --- |
| `0-select_states.sql` | SQL dump used to create/populate the `hbtn_0e_0_usa` database |
| `1-filter_states.py` | Lists all states with a name starting with `N` |
| `4-cities_by_state.sql` | SQL dump used to create/populate the `hbtn_0e_4_usa` database |
| `5-filter_cities.py` | Lists all cities of a given state (SQL injection free) |

## Usage

```bash
./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
```

Example:

```bash
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```

## Author

LEEN ALGARAAWI !
