from pprint import pprint
import requests
import csv
import json
app_id="b2f41b4c"
api_key="c8958fb975a5fdcaca0d46e502cb8ec1"
base_url= "http://developer.goibibo.com/api/voyager/get_hotels_by_cityid/?app_id=b2f41b4c&app_key=949f76f49eca84daa9990c3ae7e42efa&city_id="

def getid(city):
	with open("city_list.csv") as csvfile:
		readCSV = csv.reader(csvfile,delimiter=',')
		city_id=1
		for row in readCSV:
			if row[0].lower() == city.lower():
				city_id=row[1]
	return city_id

def search_hotel(city):
	city_id=getid(city)
	url=base_url+city_id
	response = requests.get(url)
	data = response.json()
	data = data["data"]
	res=""
	keys = list(data.keys())
	keys=keys[:10]
	for k in keys:
		l = data[k]["hotel_data_node"]
		res+="Name:"+l["name"]+"\n"
		res+="Cost:"+l["extra"]["check_in"]+"\n"
		if "location" in l["loc"]:
			res+="Location:"+l["loc"]["location"]+"\n"
		res+="\n"
	return res

result = search_hotel("mumbai")
print(result)