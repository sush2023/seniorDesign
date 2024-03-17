from Pushover_app import PushoverApp

if __name__ == "__main__":
  application_token = "a21o5exe854jysccbyi17riq25wssj"
  user_token = "upcv258kexr2suv1ei4d3t2kmeer9m"

  pushover_obj = PushoverApp(application_token, user_token)
  pushover_obj.sendMessage("hello I am notifying")
