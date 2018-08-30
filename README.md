# Simple Flask API

Getting my feet wet with the following in a Flask application:
- API JSON responses
- SQLite3 DB

To run this:
1. Run the database creation script
```bash
python db_creation.py
```

2. Substitute your own username and password for auth in your own separate config_vars.py file
```python
#config_vars.py
DATABASE="tasks.db"
test_username="<your own username>"
test_password="<your own password>"
```

3. Run the flask app (note that the DB has two test entries in it)
```bash
python simpleAPI.py
```


## TODO

1. Use Row_Factory magic for SQLite3 DB connections

2. Create POST/PUT methods