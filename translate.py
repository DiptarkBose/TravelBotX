# -*- coding: utf-8 -*-

import http.client, urllib.parse
import xml.etree.ElementTree

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
def translate(text, t_l):
	subscriptionKey = '<subKey>'

	host = 'api.microsofttranslator.com'
	path = '/V2/Http.svc/Translate'
	t_l.lower()
	if(t_l=="german"):
		target ='de'
	elif(t_l=="english"):
		target= 'en-us'
	elif(t_l=="chinese"):
		target='zh-CHS'
	elif(t_l=="spanish"):
		target='es'
	elif(t_l=="french"):
		target='fr'

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
print(translate("My  name is Diptark", "french"))
