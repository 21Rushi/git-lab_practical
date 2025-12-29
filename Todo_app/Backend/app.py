from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI= os.getenv("MONGO_URI")
app = Flask(__name__, template_folder="../FrontEnd/")

client = MongoClient(MONGO_URI)
db = client["tododb"]
collection = db["todoitems"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }
    collection.insert_one(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
