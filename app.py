from flask import Flask, render_template, request




app = Flask (__name__,template_folder='templates')

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/booked")
def booked():
    date = request.args.get("date","null") 
    name = request.args.get("name", "valued customer")
    number = request.args.get("number","null")
    time = request.args.get("time", "null")
    REGISTRANTS[name,number,date,time] = name
  
    # REGISTRANTS[time] = name
    # REGISTRANTS[date] = name

   
    return render_template("booked.html",name=name, date=date, number=number, time = time)

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants = REGISTRANTS)
