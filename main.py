from typing import Tuple
from flask import Flask, render_template, request, make_response,Response
from dbms import database

app = Flask(__name__, template_folder="template", static_folder="static")
db = database()


@app.route("/", methods=["GET"])
def home() -> str:
    return render_template("home.html")

@app.route("/change/")
def changes() -> str:
    return render_template("change.html")

@app.route("/api/addRecord/", methods=["POST"])
def addRecord() -> Tuple[Response,int]:

    if request.method == "POST":
        name  = request.args.get("na")
        phone = request.args.get("ph")
        email = request.args.get("em")
       
        if len(phone) == 10 and name != None and email != None and phone.isdigit():
            db.insert_user(name, phone, email)
            resp = make_response({"success": True,"message": "Record added successfully"}),200

        else:
            resp = make_response({"success": False, "message": f"Invalid parameters\n{request.args.to_dict()}"}),400

    else:
        resp = make_response({"success": False, "message": "Method Not Allowed"}),405

    resp[0].headers['Access-Control-Allow-Origin'] = '*'
    resp[0].headers['mode'] = 'cors'
    return resp

@app.route("/api/getAllRecord/", methods=["GET"])
def getPhones() -> Tuple[Response,int] :

    if request.method != "GET":
        resp:Response = make_response({"data": [],"message":"Method Not Allowed "}),405

    else:
        rv = []
        record = db.get_all_users()
        if record == None:
            record = []

        for i in record:
            rv.append({"id": i[0], "name": i[1], "phone": i[2], "email": i[3]})
        resp = make_response({"data": rv,"message":""}),200
    
    resp[0].headers['Access-Control-Allow-Origin'] = '*'
    resp[0].headers['mode'] = 'cors'
    return resp

@app.route("/api/search/", methods=["GET"])
def search() -> Tuple[Response,int] :

    ph = request.args.get("ph",default=None)

    if ph != None and len(ph) == 10 and ph.isdigit():
        temp = db.get_user(ph)
        resp = make_response({"data": [{"id": temp[0], "name": temp[1], "phone": temp[2], "email": temp[3]} ],"message":""}),200
        
    else:
        resp = make_response({"data": [],"message":f"Invalid parameters\n{request.args.to_dict()}"}),400
            
    resp[0].headers['Access-Control-Allow-Origin'] = '*'
    resp[0].headers['mode'] = 'cors'
    return resp

@app.route("/api/update/", methods=["UPDATE"])
def update_record() -> Tuple[Response,int] :
       
    if request.method == "UPDATE":
        name  = request.args.get("na")
        phone = request.args.get("ph")
        email = request.args.get("em")
        ph_old = request.args.get("with")
        
        if name != None and phone != None and phone.isdigit() and email != None and ph_old !=None and ph_old.isdigit():
            db.update_user(name,phone,email,ph_old)
            resp =  make_response({"success": True,"message":"Updated Successfully"}), 200
        
        else:
            resp = make_response({"success": False, "message":f"Invalid parameters \n{request.args.to_dict()}"}), 400
    else:
        resp = make_response({"success": False, "message": "Method Not Allowed"}),405

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['mode'] = 'cors'
    return resp


@app.route("/api/delete/", methods=["DELETE"])
def delete_record() -> Tuple[Response,int] :

    if request.method == "DELETE":
        ph_old = request.args.get("with")
        if ph_old!=None and ph_old.isdigit():
            db.delete(ph_old)
            resp =  make_response({"success": True,"message":"Updated Successfully"}), 200
        else:
            resp = make_response({"success": False, "message":f"Invalid parameters \n{request.args.to_dict()}"}), 400
    else:
        resp = make_response({"success": False, "message": "Method Not Allowed"}),405

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['mode'] = 'cors'
    return resp