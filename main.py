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

@app.route("/changes")
def changes():
    return render_template("changes.html")

@app.route("/api/search/", methods=["GET"])
def search():
    try :
        ph = request.args.get("ph")
        if ph == None:
            raise
        print(ph)
        temp = db.get_user(str(ph))
        print(temp)
        resp = make_response({"data": [{"id": temp[0], "name": temp[1], "phone": temp[2], "email": temp[3]} ]})
   
    except :
        resp = make_response({"data": []})
        
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["mode"] = "cors"
    return resp


@app.route("/api/update/", methods=["POST"])
def update_phone():
    if request.method == "POST":
        try:
            name = str(request.args.get("na"))
            phone = int(request.args.get("ph"))
            if len(str(phone)) != 10:
                raise Exception
            email = str(request.args.get("em"))
            ph_old = str(request.args.get("with"))
            print((name,phone, email,ph_old))
            db.update_user(name,phone,email,ph_old)
            return {"success": True}, 200
        except:
            pass
    return {"success": False, "request": request.args.to_dict()}, 400

@app.route("/api/delete/", methods=["POST"])
def delete_phone():
    if request.method == "POST":

            ph_old = str(request.args.get("with"))
            db.delete(ph_old)
            return {"success": True}, 200

    return {"success": False, "request": request.args.to_dict()}, 400