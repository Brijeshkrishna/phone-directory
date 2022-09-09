
from flask import Flask ,render_template,request,redirect

app = Flask(__name__, template_folder="template", static_folder="static")

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


@app.route('/addPhone/', methods=["POST"])
def addPhone():
    if request.method == 'POST':
        print(request.form.get("phone_number"))
    return redirect("/")



@app.route('/api/getPhones', methods=["GET"])
def getPhones():
    return 