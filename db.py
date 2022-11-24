from flask_mysqldb import MySQL
from flask import Flask

app = Flask("__name__")

mysql = MySQL(app)