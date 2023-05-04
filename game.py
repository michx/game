from eodhd import APIClient
import requests, json

YOUR_API_TOKEN =""



url = "https://eodhistoricaldata.com/api/real-time/VOW.F?api_token="+YOUR_API_TOKEN+"&fmt=json"

response = requests.get(url)

data = json.loads(response.text)

for key in data.keys():
    print (key+"  :  "+str(data[key]))