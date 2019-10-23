import datetime
import json
import sqlite3
import csv
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, String
from sqlalchemy.ext.automap import automap_base

engine = create_engine("sqlite:///fungi_db.sqlite")

# # reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# # references to each table
Table = Base.classes.findings


# # create instance of Flask app
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/jarredb/Desktop/test/test_db'
# db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


# # create route that renders index.html template
# @app.route("/index")
# def index():
#     return render_template("index.html")


# #create a route for the data
@app.route("/api")
def api():
#     # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all results"""
    # Query all test_db
    results = session.query(
        Table.id,
        Table.date,
        Table.type,
        Table.aka,
        Table.finder,       
        Table.notes,
        Table.lat,
        Table.lon,
        Table.ref).all()

    session.close()

    # Create a dictionary from the row data and append to a list
    test_db = []
    for id, date, type, notes, lat, lon in results:
        test_dict = {}
        test_dict["id"] = id
        test_dict["date"] = date
        test_dict["type"] = type
        test_dict["notes"] = notes
        test_dict["lat"] = lat
        test_dict["lon"] = lon
        test_db.append(test_dict)
    return jsonify(test_db)


# if __name__ == "__main__":
#     app.run(debug=True)

