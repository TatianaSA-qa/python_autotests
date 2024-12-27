import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1cf86cfecbace76afaa09b8f2ef8c108'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "173069",
    "name": "Хаги Ваги",
    "photo_id": 1
    }

body_in_pokeball = {
    "pokemon_id": "173069"
}



response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text) 

response_in_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(response_in_pokeball.text)