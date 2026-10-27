import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
                                        #200 é um https code, means it worked
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'Failed to retrieve data: {response.status_code}')

pokemon_name = 'squirtle' # <- give the pokemon name you want to search'
pokemon_info = get_pokemon_info(pokemon_name)



if pokemon_info:
    print(f'Name: {pokemon_info["name"]}')
    print(f'Id: {pokemon_info["id"]}')
    print(f'Height: {pokemon_info["height"]}')
    print(f'Weight: {pokemon_info["weight"]}')
