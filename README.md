# Eleos
This project use python with django and sqlite3 as local database.

### Folders
    eleos > the main folder of the project
    template > the templates files for view
    zoom_app > the application that deal with with api connection and the local database

### Installation
```
pip install -r requirements.txt
./manage.py migrate
```
### Running the project
```
TOKEN=<the token> ./manage.py runserver <port>
```
by default the port is 8000

The site address:
```
http://127.0.0.1:<port>/zoom_app/table/
```

You can see the db table on:
```
http://127.0.0.1:<port>/zoom_app/table/
```
