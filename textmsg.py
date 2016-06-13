from twilio.rest import TwilioRestClient

sid = "ACb0239d4d23403a135f56158fb28e4f1f"
auth = "5683535fe884a2643434addd31eab353"

client = TwilioRestClient(sid, auth)

message = client.sms.messages.create(
    body = "Sending from python - Nitheen",
    to="+17734310933",
    from_="+13126255512"
)

print(message.sid)