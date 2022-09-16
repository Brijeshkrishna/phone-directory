from flask import Flask, render_template, request, make_response
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
            phone = int(request.args.get("ph"))
            if len(str(phone)) != 10:
                raise Exception
            email = str(request.args.get("em"))
            db.insert_user(name, phone, email)
            return {"success": True}, 200
        except:
            pass
    return {"success": False, "request": request.args.to_dict()}, 400


@app.route("/api/getPhones", methods=["GET"])
def getPhones():
    rv = []
    looper = db.get_all_users()
    looper = [] if looper == None else looper
    for i in looper:
        rv.append({"id": i[0], "name": i[1], "phone": i[2], "email": i[3]})
    resp = make_response({"data": rv})
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["mode"] = "cors"
    return resp
