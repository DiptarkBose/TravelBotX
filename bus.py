from pprint import pprint
import requests
import json
app_id="b2f41b4c"
api_key="c8958fb975a5fdcaca0d46e502cb8ec1"
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

result = search("bangalore","mangalore","20180301")
print(result)