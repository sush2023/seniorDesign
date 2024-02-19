from Pushover_app import PushoverApp

application_token = "a21o5exe854jysccbyi17riq25wssj"

def test_false_user_token():
    application_token = "a21o5exe854jysccbyi17riq25wssj"
    user_token = "sdf"
    pushover_obj = PushoverApp(application_token, user_token)
    pushover_obj.sendMessage("hello I am notifying")
    assert (pushover_obj.result == False)

def test_false_application_token():
    application_token = "asdfasdfasdf"
    user_token = "upcv258kexr2suv1ei4d3t2kmeer9m"
    pushover_obj = PushoverApp(application_token, user_token)
    pushover_obj.sendMessage("hello I am notifying")
    assert (pushover_obj.result == False)
