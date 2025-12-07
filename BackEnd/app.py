from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
import json, os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI= os.getenv("MONGO_URI")
app = Flask(__name__, template_folder="../FrontEnd/templates")

client = MongoClient(MONGO_URI)
db = client["test_db"]
collection = db["test_collection"]


# @app.route("/api")
# def api_data():
#     file = os.path.join(os.path.dirname(__file__), "data.json")
#     data = json.load(open(file))
#     return jsonify(data)
@app.route("/api")
def api_data():
    try:
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        print("Received:", name, email) 

        if not name or not email:
            return render_template("index.html", error="Enter all fields")
        
        result = collection.insert_one({"name": name, "email": email})
        print("Inserted ID:", result.inserted_id)  # <-- Debug print

        # collection.insert_one({"name": name, "email": email})
        return redirect("/success")

    except Exception as e:
        return render_template("index.html", error=str(e))

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)
