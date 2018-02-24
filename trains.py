#cphfd4goh2
import json, requests
import urllib
import datetime
'''
def name_to_code(station_name):
	url="https://api.railwayapi.com/v2/name-to-code/name/station_name/apikey/cphfd4goh2/"
	resp = requests.get(url).json()
	print(resp);
'''
def train_between(from_station, to_station, date):
	url="https://api.railwayapi.com/v2/between/source/"+from_station+"/dest/"+to_station+"/date/"+date+"/apikey/cphfd4goh2/"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	total_trains=parsed_json['total']
	str_ans="The following trains are available: \n"
	for i in range(0, total_trains):
		str_ans+="Option "+str(i+1)+":\nTrain Number: "+str(parsed_json['trains'][i]['number'])+"\n"
		str_ans+="Train Name: "+parsed_json['trains'][i]['name']+"\n"
		str_ans+="Departure: "+parsed_json['trains'][i]['src_departure_time']+"\n"
		str_ans+="Arrival: "+parsed_json['trains'][i]['dest_arrival_time']+"\n"
		str_ans+="Duration: "+parsed_json['trains'][i]['travel_time']+"\n"
		str_ans+='\n'
	print(str_ans)
	
#train_between("gkp", "jat", "12-03-2018")

def live_train_status(train_number):
	date=datetime.datetime.today().strftime('%d-%m-%Y')
	url="https://api.railwayapi.com/v2/live/train/"+str(train_number)+"/date/"+str(date)+"/apikey/cphfd4goh2/"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	str_ans=parsed_json['position']
	print(str_ans)
live_train_status(56640);