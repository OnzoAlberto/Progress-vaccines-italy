import urllib.request
import json


def download_from_url():
	url = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati"
	italy_list = []
	try:
		with urllib.request.urlopen(url + '/vaccini-summary-latest.json') as response:
			region_list = json.loads(response.read())
			for region in region_list['data']:
				italy_list.append(region)
		return italy_list
	except ValueError:
		print("URL form is invalid")
		print("Ex: http://www.google.com")
		return -1


#I take the data from the official website
region_list = download_from_url()
for region in region_list:
    print('Regione: ' + region['nome_area']+ '\n')
    print('Dosi somministrate: ' + str(region['dosi_somministrate']) + '\n')
