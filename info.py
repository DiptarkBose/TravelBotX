import json, requests
import urllib

def search_duckduckgo_instant_api(s_string):
	search_string=""
	for i in range(0, len(s_string)):
		if(s_string[i]==' '):
			search_string+="+"
		else:
			search_string+=s_string[i]
	
	url="https://api.duckduckgo.com/?q="+search_string+"&format=json&pretty=1"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	str_ans=parsed_json['AbstractText']
	return(str_ans)
print(search_duckduckgo_instant_api("kuala lumpur"))

#Search works on things like Mahatma Gandhi, Bangkok, Kuala Lumpur