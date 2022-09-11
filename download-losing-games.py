import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/x-ndjson"
headers["Content-Type"] = "application/x-ndjson"
data = '{"Content-type":"application/x-ndjson"}'

url = 'https://lichess.org/api/games/user/jtorrex?rated=true,perfType=blitz'

print ("Starting! Downloading games:")
games = requests.get(url)
print ("Download complete.! Printing games")
print(games.text)
print(games.status_code)

print ("Starting! Downloading JSON games:")
games_json = requests.get(url,headers=headers,data=data)
print ("Download complete.! Printing games")
print(games_json.text)
print(games_json.status_code)
