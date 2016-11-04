# Geschreven door Robin


import requests
import json
import datetime

class ClientRequest:
	_apiUrl = "https://overheid.io/api/voertuiggegevens/{}?ovio-api-key={}"
	# de api key te vinden bij account profiel p de website
	_apiSignKey = "169dc709eb5e9318b23b159a1dce75414e3c252100236b647dcb26a6bf7d2f22"


	def Request(self,url):
		return requests.get(url, verify=False)


	def GetPlateData(self,strNumberPlate):
		try:
			"Haalt number plaat data op door middel van string nummer plaat"
			strNumberPlate = str(strNumberPlate).strip()

			requestUrl = self._apiUrl.format(strNumberPlate, self._apiSignKey)
			response = None
			try:
				response = self.Request(requestUrl)
			except Exception as e:
				print("Error:",str(e))
				pass

			if response is None:
				return
			# Jun 1 2005  1:33PM
			# 2012-02-24T00:00:00+00:00

			jsonData = response.json()
			date = str(jsonData["datumeerstetoelating"]).split("+")
			numberPlate = NumberPlate()
			numberPlate.Data = jsonData
			numberPlate.Fuel = jsonData["hoofdbrandstof"]
			numberPlate.DateFirstEntry = datetime.datetime.strptime(date[0], '%Y-%m-%dT%H:%M:%S')
			numberPlate.Fuel = jsonData["hoofdbrandstof"]

			numberPlate.Plate = strNumberPlate
			numberPlate.Url = requestUrl
			return numberPlate
		except:
			return None


class NumberPlate:
	Url = ""
	Plate = ""
	DateFirstEntry = ""
	Fuel = ""
	Data = {}
