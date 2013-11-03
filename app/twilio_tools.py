from twilio.util import TwilioCapability
import twilio.twiml
import os
 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
application_sid = os.environ['TWILIO_APPLICATION_SID']

def generate_capability_token():
	capability = TwilioCapability(account_sid, auth_token)
	capability.allow_client_outgoing(application_sid)
	return capability.generate()




def record_twiml():
	resp = twilio.twiml.Response()
	resp.say("Record your comment after the tone.")
	resp.record(maxLength="20", action="/api/handle-recording")
	return str(resp)


