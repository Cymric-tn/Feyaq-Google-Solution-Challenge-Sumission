from twilio.rest import Client

account_sid = 'AC6dc92fa3e9d5524a45583d2b21c2f283'
auth_token = '42250d6519fc357330b840774d9d31d0'
client = Client(account_sid, auth_token)
def send_message():
    message = client.messages.create(
    from_='+15076206061',
    body='''Feyaq: Immediate Action Required 🚨

Action needed at provided location. Please review and address urgently. Report appreciated.

Form link: https://forms.office.com/r/7nFJyNZRJF
''',
    to='+21620799539'
    )

    print(message.sid)
