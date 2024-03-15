import os

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    message = f"Hello, {name}! You are {age} years old."
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(host="0.0.0.0")