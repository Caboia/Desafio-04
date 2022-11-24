from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from db import mysql, app

def create_app():
  from app import routes
  routes.init_app(app)

  return app

Bootstrap(app)
# conexão com banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contatos'



    
app.run()