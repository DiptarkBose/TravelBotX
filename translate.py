# -*- coding: utf-8 -*-

import http.client, urllib.parse
import xml.etree.ElementTree

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
def translate(text):
	subscriptionKey = 'f2cc99279b4444a58e89ce9a7c816c33'

	host = 'api.microsofttranslator.com'
	path = '/V2/Http.svc/Translate'

	target = 'en-us'

	params = '?to=' + target + '&text=' + urllib.parse.quote (text)

	def get_suggestions ():

	    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
	    conn = http.client.HTTPSConnection(host)
	    conn.request ("GET", path + params, None, headers)
	    response = conn.getresponse ()
	    return response.read ()

	result = get_suggestions ()
	z= (result.decode("utf-8"))
	z=z[68: len(z)-9]
	return(z)
print(translate("Mein Name Ist Diptark"))