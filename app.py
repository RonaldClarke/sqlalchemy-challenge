import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
#SQLAlchemy 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
#Flask 
app = Flask(__name__)
@app.route("/")
def main():    
    return "Welcome to my Home page!"
    return "Routes: Precipitation, Stations, Temperatures"
@app.route("/api/v1.0/precipitation")
def names(): 
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= "2016-08-23").all()
    session.close()
     precip_list = []
    for date, prcp in results: 
        precip_dict = {}
        precip_dict['date'] = date 
        precip_dict['prcp'] = prcp
        precip_list.sqlitengers.append(precip_dict)
    return jsonify(results)
