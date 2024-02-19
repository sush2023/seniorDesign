from pushover import Pushover, PushoverError
import json

class PushoverApp:
    
    def __init__(self, application_token, user_token):
        self.app_token = application_token
        self.user_token = user_token
        self.message = "Water Sense"
        self.pushover_app = Pushover(self.app_token)
        self.pushover_app.user(self.user_token)
    
    def _handleException(self, error_string):
        error_s = error_string.strip("PushoverError")
        error_s = error_s.replace("\'", "")
        error_s = error_s.replace("(", "")
        error_s = error_s.replace(")", "")
        data = json.loads(error_s)
        if "user" in data.keys():
            if data["user"] == "invalid":
                print("User token invalid")
        elif "token" in data.keys():
            if data["token"] == "invalid":
                print("Application token invalid.")

    def sendMessage(self, message):
        msg = self.pushover_app.msg(message)
        msg.set("title", "WaterSense")
        try:
            self.pushover_app.send(msg)
        except PushoverError as error:
            self._handleException(repr(error))
            self.result = False
            return
       print("hello") 
        self.result = True
            
