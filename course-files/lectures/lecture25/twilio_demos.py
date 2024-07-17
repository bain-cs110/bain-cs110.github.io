from apis import twilio

to_address = "" # use your email address if you want to test it!
subject = "Pre-Recorded Demos"
text = "To Whom it May Concern,<br>Your computer has achieved sentience.<br>Sincerely,<br>Your Friendly Neighborhood CS Student"

did_it_send = twilio.send_email(to_address, subject, text)

print("result:", did_it_send)
