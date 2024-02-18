from pushover import Pushover, PushoverError

import json


def pushover_init():
  po = Pushover("a21o5exe854jysccbyi17riq25wssj")
  #po = Pushover("a21o5exe854jysccbyi17riq25wsssdfsdfasdfsdf")
  #test false token
  #po.user("upcv258kexr2suv1ei4d3t2kmeer9k")
  po.user("upcv258kexr2suv1ei4d3t2kmeer9m")
  return po

def send_message():
  water_flow_time = 2
  msg = po.msg(f"Water flow detected for {water_flow_time} minutes")
  msg.set("Water Water", "water")
  try:
    po.send(msg)
  except PushoverError as error:
    error_s = repr(error)
    error_s = error_s.strip("PushoverError")
    error_s = error_s.replace("\'", "")
    error_s = error_s.replace("(", "")
    error_s = error_s.replace(")", "")
    data = json.loads(error_s)
    if "user" in data.keys():
      if data["user"] == "invalid":
        print("User token invalid")
    elif "token" in data.keys():
      print("Application token invalid.")

if __name__ == "__main__":
  po = pushover_init()
  send_message()
