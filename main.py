from flask import Flask, render_template, request, redirect, make_response
from dbms import database

app = Flask(__name__, template_folder="template", static_folder="static")
db = database()

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/addPhone/", methods=["POST"])
def addPhone():
    if request.method == "POST":
        try:
            name = str(request.args.get("na"))
            country_code = abs(int(request.args.get("cc")))
            phone_number = int ( request.args.get("ph"))
            db.insert(name, country_code, phone_number)
            return {'success': True},200
        except:
            pass
    return {'success': False},400



@app.route("/api/getPhones", methods=["GET"])
def getPhones():
    rv = []
    for i in db.get_users():
        rv.append({"id":i[0],"name": i[1], "country_code": i[2], "phone_num": i[3]})
    resp = make_response({"data": rv})
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["mode"] = "cors"
    return resp
