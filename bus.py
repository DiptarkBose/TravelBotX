from pprint import pprint
import requests
import json
app_id="Insert id here"
api_key="Insert key here"
base_url="http://developer.goibibo.com/api/bus/search/?app_id=b2f41b4c&app_key=949f76f49eca84daa9990c3ae7e42efa&format=json&"
def search(src,dest,dateDep):
	dateDep=str(dateDep)
	url=base_url+"source="+src+"&destination="+dest+"&dateofdeparture="+dateDep
	response = requests.get(url)
	data = response.json()
	data = data["data"]["onwardflights"]
	res=""
	for row in data:
		res+="Origin:"+row["origin"]+"\n"
		res+="Destination:"+row["destination"]+"\n"
		res+="Departure Time:"+row["DepartureTime"]+"\n"
		res+="Arrival Time:"+row["ArrivalTime"]+"\n"
		res+="Seat:"+row["seat"]+"\n"
		res+="Duration:"+row["duration"]+"\n"
		res+="Type:"+row["BusType"]+"\n"
		res+="Fare:"+row["fare"]["totalfare"]+"\n"
		res+="Travels Name"+row["TravelsName"]+"\n"
		res+="\n"
	return res

def filter1(src,dest,dateDep,filter):
	dateDep=str(dateDep)
	url=base_url+"source="+src+"&destination="+dest+"&dateofdeparture="+dateDep
	response = requests.get(url)
	data = response.json()
	data = data["data"]["onwardflights"]
	res=""
	for row in data:
		if(filter in row["seat"]):
			res+="Origin:"+row["origin"]+"\n"
			res+="Destination:"+row["destination"]+"\n"
			res+="Departure Time:"+row["DepartureTime"]+"\n"
			res+="Arrival Time:"+row["ArrivalTime"]+"\n"
			res+="Seat:"+row["seat"]+"\n"
			res+="Duration:"+row["duration"]+"\n"
			res+="Type:"+row["BusType"]+"\n"
			res+="Fare:"+row["fare"]["totalfare"]+"\n"
			res+="Travels Name:"+row["TravelsName"]+"\n"
			res+="\n"
	return res


seat_type_filter = "ST"
result = filter1("bangalore","mangalore","20180301",seat_type_filter)
print(result)
