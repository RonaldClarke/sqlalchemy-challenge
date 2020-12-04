import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
#SQLAlchemy 
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
inspector = inspect(engine)
print(inspector.get_table_names())
Measurement = Base.classes.measurement
Station = Base.classes.station
#Flask 
app = Flask(__name__)
@app.route("/")
def main():    
    return "Welcome to my Home page!"
    return "Routes: Precipitation, Stations, Temperatures"
@app.route("/api/v1.0/precipitation")
def precipitation(): 
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= "2016-08-23").all()
    session.close()
    precip_list = []
    for date, prcp in results: 
        precip_dict = {}
        precip_dict['date'] = date 
        precip_dict['prcp'] = prcp
        precip_list.append(precip_dict)
    return jsonify(precip_list)
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Measurement.station).group_by(Measurement.station).all())
    session.close()
    stns = [item[0] for item in stations]
    return jsonify(stns)
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    tobserve = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= "2016-08-23").all()
    session.close()
    all_tobs = []
    for date, tobs in tobserve:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)
@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results = session.query(Measurement.date, func.min(Measurement.tobs, func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).group_by(Measurement.date).all()
    session.close()
start_list = []
for date, min, avg, max in results:
    start_dict = {}
    start_dict["Date"] = date
    start_dict["TMIN"] = min
    start_dict["TAVG"] = avg
    start_dict["TMAX"] = max
    start_list.append(start_dict)
return jsonify()
if __name__ == '__main__': 
    app.run(debug=True)