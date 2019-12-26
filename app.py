# import necessary libraries
import numpy as np 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


#link to db
engine = create_engine("sqlite:///fungi_db.sqlite")

Base = automap_base()

# reflect db
Base.prepare(engine, reflect=True)

# save reference to the table
Fungi = Base.classes.findings

#setup Flask
app = Flask(__name__)


#create api route
@app.route("/api")
def data_display():

    session = Session(engine)

    """Return a list of data"""
    # Query all data in Fungi
    session = Session(engine)
    results = session.query(Fungi.id, Fungi.date, Fungi.type, Fungi.aka, Fungi.finder, Fungi.city, Fungi.state, Fungi.lat, Fungi.lon, Fungi.ref).all()

    session.close()

    # Create a dictionary from the row data and append to a list of fungi_cols and other stuff
    fungi_cols = []
    for id, date, type, aka, finder, city, state, lat, lon, ref in results:
        fungi_dict = {}
        fungi_dict["id"] = id
        fungi_dict["date"] = date
        fungi_dict["type"] = type
        fungi_dict["aka"] = aka
        fungi_dict["finder"] = finder
        fungi_dict["city"] = city
        fungi_dict["state"] = state
        fungi_dict["lat"] = lat
        fungi_dict["lon"] = lon
        fungi_dict["ref"] = ref
        fungi_cols.append(fungi_dict)

    return jsonify(fungi_cols)


# # # create page routes
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/map2")
def map2():
    return render_template("map2.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/share")
def share():
    return render_template("share.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/projectplan")
def projectplan():
    return render_template("projectplan.html")


if __name__ == "__main__":
    app.run(debug=True)

