from twilio.rest import Client

account_sid = 'AC6d85289ebbb74c75a999d91f538eb605'
auth_token = '2a299e6dca49a44878279a6a34572df3'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12056497401',
    body="Don't worry, Everything happens for a reason. I am with you forever :)" ,
    to='+16475632510'
)

print(message.sid)
