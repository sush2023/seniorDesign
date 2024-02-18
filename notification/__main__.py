from pushover import Pushover, PushoverError

def pushover_init():
  #po = Pushover("a21o5exe854jysccbyi17riq25wssj")
  po = Pushover("a21o5exe854jysccbyi17riq25wsssdfsdfasdfsdf")
  #test false token
  po.user("upcv258kexr2suv1ei4d3t2kmeer9k")
  #po.user("upcv258kexr2suv1ei4d3t2kmeer9m")
  return po

def send_message():
  water_flow_time = 2
  msg = po.msg(f"Water flow detected for {water_flow_time} minutes")
  msg.set("Water Water", "water")
  try:
    po.send(msg)
  except PushoverError as error:
    error_s = repr(error)
    print(error_s)

if __name__ == "__main__":
  po = pushover_init()
  send_message()
