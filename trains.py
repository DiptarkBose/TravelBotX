import json, requests
import urllib
import datetime

def name_to_code(station_name):
	url="https://api.railwayapi.com/v2/name-to-code/station/"+station_name+"/apikey/<apikey>/"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	str_ans=parsed_json['stations'][0]['code']
	return(str_ans)
print(name_to_code("udupi"))

def train_between(f_station, t_station, date):
	from_station=name_to_code(f_station)
	to_station=name_to_code(t_station)
	url="https://api.railwayapi.com/v2/between/source/"+from_station+"/dest/"+to_station+"/date/"+date+"/apikey/<apikey>/"
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
	return (str_ans)
	
print(train_between("udupi", "madgaon", "12-03-2018"))

def live_train_status(train_number):
	date=datetime.datetime.today().strftime('%d-%m-%Y')
	url="https://api.railwayapi.com/v2/live/train/"+str(train_number)+"/date/"+str(date)+"/apikey/<apikey>/"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	str_ans=parsed_json['position']+"\n"
	return (str_ans)
print(live_train_status(56640))

def pnr_status(pnr):
	url="https://api.railwayapi.com/v2/pnr-status/pnr/"+str(pnr)+"/apikey/<apikey>/"
	resp = requests.get(url)
	parsed_json=json.loads(resp.text);
	total_passengers=parsed_json['total_passengers']
	str_ans="Your current PNR status is as follows: \n"
	str_ans+="PNR: "+str(pnr)+"\n"
	str_ans+="Date of Journey: "+parsed_json['doj']+"\n"
	str_ans+="Total Passengers: "+str(total_passengers)+"\n"
	str_ans+="Chart Prepared: "+str(parsed_json['chart_prepared'])+"\n"
	str_ans+="From: "+parsed_json['from_station']['name']+"\n"
	str_ans+="To: "+parsed_json['to_station']['name']+"\n"
	str_ans+="Reservation upto: "+parsed_json['reservation_upto']['name']+"\n"
	str_ans+="Train Name: "+parsed_json['train']['name']+"\n"
	str_ans+="Train Number: "+parsed_json['train']['number']+"\n"
	p_list=parsed_json['passengers']
	for i in range(0, total_passengers):
		str_ans+="Passenger "+str(i+1)+str(p_list[i]['no'])+"\n"
		str_ans+="Current Status: "+p_list[i]['current_status']+"\n"
		str_ans+="Status at the time of booking: "+p_list[i]['booking_status']+"\n"
	return(str_ans)
print(pnr_status(4759809237))
