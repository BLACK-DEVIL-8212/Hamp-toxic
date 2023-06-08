from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'Your_Account_SID'
auth_token = 'Your_Auth_Token'

# Your Twilio phone number and the recipient's phone number
twilio_number = 'Your_Twilio_Phone_Number'
recipient_number = 'Recipient_Phone_Number'

# Message content
message_content = 'This is a system-generated message.'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body=message_content,
    from_=twilio_number,
    to=recipient_number
)

print(f"Message SID: {message.sid}")
