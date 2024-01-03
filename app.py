from flask import Flask, render_template, request




app = Flask (__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/booked")
def booked():
    return render_template("booked.html", name=request.args.get("name", "valued customer"), date=request.args.get("date", "null"), time=request.args.get("time","null"), number=request.args.get("number", "null"))

