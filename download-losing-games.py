# https://pynative.com/python-parse-multiple-json-objects-from-file/
# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236
# https://pynative.com/parse-json-response-using-python-requests-library/

import requests
import json
from requests.structures import CaseInsensitiveDict
from requests.exceptions import HTTPError

headers = CaseInsensitiveDict()
headers["Accept"] = "application/x-ndjson"
headers["Content-Type"] = "application/x-ndjson"
data = '{"Content-type":"application/x-ndjson"}'

print("=== Lichess Losing Games Exporter ===\n")

try:

    print("- Downloading White Games...\n")
    white_url = 'https://lichess.org/api/games/user/jtorrex?color=white&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true'

    # Make the request to the Lichess API
    response_white_games = requests.get(white_url,headers=headers)
    response_white_games.raise_for_status()

    # Store the result of the request as a JSON file
    with open("white_games.json", "w") as file:
    	file.write(response_white_games.text)
    	file.close()

    # Defines a list to store all the games as dict objects
    # Read the white_games.json file, one line at a time
    white_games_list = []
    with open("white_games.json") as file:
        for json_game in file:
            white_games_dict = json.loads(json_game)
            white_games_list.append(white_games_dict)

    # Print each JSON decoded Object (game)
    for game in white_games_list:
        if game["status"] == "draw":
            game = "https://lichess.org/"+game["id"]
            print(game + " - Draw")
            with open("white_drawing_games_urls.out", "w") as file:
                file.write(game)

        elif game["winner"] == "black":
            game = "https://lichess.org/"+game["id"]
            print(game + " - Lose")
            with open("white_losing_games_urls.out", "w") as file:
                file.write(game)
        else:
            game = "https://lichess.org/"+game["id"]
            print(game + " - Win")
            with open("white_winning_games_urls.out", "w") as file:
                file.write(game)

    print("- Done!\n")

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

try:

    print("- Downloading Black Games...\n")
    black_url = 'https://lichess.org/api/games/user/jtorrex?color=black&rated=true&tags=true&clocks=false&evals=false&opening=false&perfType=blitz&pgnInJson=true'

    # Make the request to the Lichess API
    response_black_games = requests.get(black_url,headers=headers)
    response_black_games.raise_for_status()

    # Store the result of the request as a JSON file
    with open("black_games.json", "w") as file:
    	file.write(response_black_games.text)
    	file.close()

    # Defines a list to store all the games as dict objects
    # Read the black_games.json file, one line at a time
    black_games_list = []
    with open("black_games.json") as file:
        for json_game in file:
            black_games_dict = json.loads(json_game)
            black_games_list.append(black_games_dict)

    # Print each JSON decoded Object
    for game in black_games_list:

        if game["winner"] == "white":
            game = "https://lichess.org/"+game["id"]
            print(game + " - Lose")
            with open("black_losing_games_urls.out", "w") as file:
                file.write(game)
        
        else:
            game = "https://lichess.org/"+game["id"]
            print(game + " - Win")
            with open("black_winning_draw_games_urls.out", "w") as file:
                file.write(game)

    print("- Done!\n")

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
