from flask import Flask, request, jsonify
from models import create_todo_item

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Missing fields"}), 400

    todo_item = create_todo_item(item_name, item_description)

    return jsonify({
        "message": "Item saved successfully",
        "todo": todo_item
    }), 201

if __name__ == "__main__":
    app.run(debug=True)

