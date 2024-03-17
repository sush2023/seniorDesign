from Pushover_app import PushoverApp

if __name__ == "__main__":
  application_token = "a21o5exe854jysccbyi17riq25wssj"
  user_token = "upm598s42frx6121mr5cet8b8bcjo4"

  pushover_obj = PushoverApp(application_token, user_token)
  pushover_obj.sendMessage("hello I am notifying")
