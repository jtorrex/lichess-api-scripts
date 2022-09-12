# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236
import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/x-ndjson"
headers["Content-Type"] = "application/x-ndjson"
data = '{"Content-type":"application/x-ndjson"}'

white_url = 'https://lichess.org/api/games/user/jtorrex?color=white&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true'

print ("Starting! Downloading games played as white")

#white_games = requests.get(white_url)
#print ("Download complete.! Printing games")
#print(white_games.text)
#print(white_games.status_code)

print ("Starting! Downloading JSON games played as white")
white_games = requests.get(white_url,headers=headers,data=data)
#white_games_json = white_games.json()
print ("Download complete.! Printing games")
print(white_games.text)
print(white_games.status_code)
#print(white_games_json)

#for p in white_games['winner']:
#    print(p['status'])

black_url = 'https://lichess.org/api/games/user/jtorrex?color=black&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true'

print ("Starting! Downloading games played as black")

#black_games = requests.get(black_url)
#print ("Download complete.! Printing games")
#print(black_games.text)
#print(black_games.status_code)

print ("Starting! Downloading JSON games played as black")
black_games = requests.get(black_url,headers=headers,data=data)
#black_games_json = black_games.json()
print ("Download complete.! Printing games")
print(black_games.text)
print(black_games.status_code)

#for p in black_games['winner']:
#    print(p['status'])
#print(black_moves_json)
