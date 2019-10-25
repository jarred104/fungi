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

    """Return a list of eater data including the age, gender, state, education, political party, race, and religion of each eater"""
    # Query all data in Fungi
    session = Session(engine)
    results = session.query(Fungi.id, Fungi.date, Fungi.type, Fungi.aka, Fungi.finder, Fungi.notes, Fungi.lat, Fungi.lon, Fungi.ref).all()

    session.close()

    # Create a dictionary from the row data and append to a list of fungi_cols and other stuff
    fungi_cols = []
    for id, date, type, aka, finder, notes, lat, lon, ref in results:
        fungi_dict = {}
        fungi_dict["id"] = id
        fungi_dict["date"] = date
        fungi_dict["type"] = type
        fungi_dict["aka"] = aka
        fungi_dict["finder"] = finder
        fungi_dict["notes"] = notes
        fungi_dict["lat"] = lat
        fungi_dict["lon"] = lon
        fungi_dict["ref"] = ref
        fungi_cols.append(fungi_dict)

    return jsonify(fungi_cols)


# # # create route that renders index.html template
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

