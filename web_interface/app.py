import os
from flask import Flask, render_template, request, jsonify
from Pushover_app import PushoverApp

app = Flask(__name__)

NOTIF_STATUS = False
CALIBRATION_STATUS = False


@app.route("/")
def hello_world():
    print(f"notification_object.result is: {notification_object.result}")
    print(f"NOTIF_STATUS is: {NOTIF_STATUS}")
    if not NOTIF_STATUS:
        return render_template("index.html", token_status="led_red")
    else:
        print("detected correct value for notif_acknowledge")
        return render_template("index.html", token_status="led_green" )

@app.route("/calibration", methods=['GET', 'POST'])
def calibration_view():
    print("calibration called")
    return render_template("calibration.html")

@app.route("/notification", methods=['GET', 'POST'])
def notification_view():
    print("notification called")
    return render_template("notification.html")

@app.route("/process", methods=["POST"])
def process():
    print("Inside process")
    try:
        data = request.get_json()
        token = data["token"]
        message = f"The token is: {token}"
        print(f"{message}")
        return jsonify({'message': message, 'calibration_state': 1})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred"}), 500

@app.route("/processToken", methods=["POST"])
def processToken():
    print("Got user token")
    data = request.get_json()
    token = data["token"]
    notification_object.setUserToken(token)
    print("sending message")
    notification_object.sendMessage("TEST NOTIFICATION!")
    return

@app.route("/updateStatus", methods=["POST"])
def updateStatus():
    print("Got user token")
    data = request.get_json()
    if data["function"] == "Notification":
        print("CHANGING NOTIF_STATUS TO TRUE")
        global NOTIF_STATUS
        NOTIF_STATUS = True
    print(f"NOTIF STATUS IS: {NOTIF_STATUS}")
    return jsonify({"status": NOTIF_STATUS}), 500

if __name__ == "__main__":
    #app.run(host="0.0.0.0",debug=False)
    app_token = "a21o5exe854jysccbyi17riq25wssj"
    global notification_object
    notification_object = PushoverApp(application_token= app_token)
    app.run(debug=True)
    