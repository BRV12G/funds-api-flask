from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instance of Flask
db = SQLAlchemy() #instance of SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Gawas304@localhost:5432/funds-db"

db.init_app(app)
