from flask import Flask, jsonify, request
from tasks import add_task, list_tasks, delete_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = add_task(data["title"], data.get("priority", "Normal"))
    return jsonify(task), 201

@app.route("/tasks/<title>", methods=["DELETE"])
def remove_task(title):
    delete_task(title)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
