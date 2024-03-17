import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/calibration")
def calibration_view():
    print("calibration called")
    return render_template("calibration.html")

@app.route("/process", methods=["POST"])
def process():
    print("Inside process")
    try:
        data = request.get_json()
        token = data["token"]
        message = f"The token is: {token}"
        print(f"{message}")
        return jsonify({'message': message, 'calibration_state': 1})
        #return render_template("calibration.html")
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    #app.run(host="0.0.0.0",debug=False)
    app.run(debug=True)