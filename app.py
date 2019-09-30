from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from sqlalchemy.sql import label

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#open homeworkutd.ipynb import dict_precip, stations, dict_temps

stations_data = ["USC00519281", "USC00519397", "USC00513117", "USC00519523", "USC00516128", "USC00514830", "USC00511918", "USC00517948", "USC00518838"]

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f"Server received request for 'Home' page..."
        f"Welcome to the Weather Station API <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )



# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")

# Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()

# Save the query results as a Pandas DataFrame and set the index to the date colum
    dates = [result[0] for result in results]
    precipitation = [result[1] for result in results]

# Create a zip object from two lists
    dates_precip = zip(dates, precipitation)
 
# Create a dictionary from zip object
    dict_precip = dict(dates_precip)
    dict_precip1 = dict_precip
    return jsonify(dict_precip1)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    stations1 = stations_data
    return jsonify(stations1)









@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")

    date_temps = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()
#date_temps

    dates_1 = [date_temp[0] for date_temp in date_temps]
    temps_1= [date_temp[1] for date_temp in date_temps]
#temps_1

    date_temps2 = zip(dates_1, temps_1)
 
# Create a dictionary from zip object
    dict_temps = dict(date_temps2)

    dict_temps1 = dict_temps
    return jsonify(dict_temps1)


@app.route("/api/v1.0/<start>")
def start():
    print("Server received request for 'start' page...")
    return "Welcome to my start page!"


@app.route("/api/v1.0/<start>/<end>")
def end():
    print("Server received request for 'end' page...")
    return "Welcome to my end page!"

if __name__ == "__main__":
    app.run(debug=True)


