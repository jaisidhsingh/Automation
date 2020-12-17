from twilio.rest  import Client

client = Client(account_sid, auth_token)

try:
    client.messages.create(
        to=f"+91{number1}",
        from_= f"{number2}",
        body="You son of a b*tch you did it"
    )
except:
    print("error")
finally:
    print("done")
