# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236
# https://pynative.com/parse-json-response-using-python-requests-library/
import requests
from requests.structures import CaseInsensitiveDict
from requests.exceptions import HTTPError

headers = CaseInsensitiveDict()
headers["Accept"] = "application/x-ndjson"
headers["Content-Type"] = "application/x-ndjson"
data = '{"Content-type":"application/x-ndjson"}'

white_url = 'https://lichess.org/api/games/user/jtorrex?color=white&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true&max=1'

try:
    response_white_games = requests.get(white_url,headers=headers)
    response_white_games.raise_for_status()

    white_games_json = response_white_games.json()
    print("White JSON response")
    #print(white_games_json)

    #print("Print each key-value pair from JSON response")
    #for key, value in white_games_json.items():
    #    print(key, ":", value)

    print("Printing atomic keys from white games JSON")
    print(white_games_json["winner"])
    print(white_games_json["pgn"])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

black_url = 'https://lichess.org/api/games/user/jtorrex?color=black&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true&max=1'

try:
    response_black_games = requests.get(black_url,headers=headers)
    response_black_games.raise_for_status()

    black_games_json = response_black_games.json()
    print("Black JSON response")
    #print(black_games_json)

    #print("Print each key-value pair from JSON response:")
    #for key, value in black_games_json.items():
    #    print(key, ":", value)

    print("Printing atomic keys from black games JSON:")
    print(black_games_json["winner"])
    print(black_games_json["pgn"])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
