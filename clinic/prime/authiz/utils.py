import json, requests, urllib3
from django.conf import settings
from bs4 import BeautifulSoup

# Works in python3.x
# in python2.x you have to user httplib

import http.client

def number_prettify(number=None):
	chars_list = '+()-– '
	number = number
	for char in chars_list:
		if char in chars_list:
			number = number.replace(char, '')
	return number

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode("utf-8") # <- or any other encoding of your choice
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def send_sms(xml_location):
	
	request = xml_location
	soup = BeautifulSoup(request, 'lxml')

	headers = {'Content-Type': 'application/xml'}

	http = urllib3.PoolManager()
	response = http.request('POST', settings.SMS_HOST+settings.SMS_API, headers=headers, body=soup)

	print("\n\n")
	print(response.read())
	print("\n\n")
	return response.read()

	# send_request = requests.post('http://'+settings.SMS_HOST+settings.SMS_API, data=request, headers=headers)

	# webservice = http.client.HTTPConnection(settings.SMS_HOST)
	# webservice.putrequest("POST", settings.SMS_API)
	# webservice.putheader("Host", settings.SMS_HOST)
	# webservice.putheader("User-Agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
	# webservice.putheader("Content-type", "text/html; charset=\"UTF-8\"")
	# webservice.putheader("Content-length", "%d" % len(request))
	# webservice.endheaders()
	# webservice.send(soup.encode('utf-8'))
	# # statuscode, statusmessage, header = webservice.getreply()
	# # result = webservice.getfile().read()

	# # print(statuscode, statusmessage, header)
	# # print(result)