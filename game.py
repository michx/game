from eodhd import APIClient
import requests, json

YOUR_API_TOKEN ="645364ce9033d9.45059006"



url = "https://eodhistoricaldata.com/api/real-time/VOW.F?api_token="+YOUR_API_TOKEN+"&fmt=json"

response = requests.get(url)

data = json.loads(response.text)

for key in data.keys():
    print (key+"  :  "+str(data[key]))