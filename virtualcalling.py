from twilio.rest import Client
# Your Twilio account SID and auth token
account_sid = 'Your_Account_SID'
auth_token = 'Your_Auth_Token'
# Your Twilio virtual number and the recipient's number
virtual_number = 'Your_Virtual_Number'
recipient_number = 'Recipient_Phone_Number'
# Create a Twilio client
client = Client(account_sid, auth_token)
# Make a call
call = client.calls.create(
    twiml='<Response><Say>Hello from your virtual number!</Say></Response>',
    from_=virtual_number,
    to=recipient_number
)
print(f"Call SID: {call.sid}")