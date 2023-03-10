import requests

token = '49bf2ebdc8dfe9606b41d336edf3c108'

add_pokemon_response=requests.post('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type':'application/json', 'trainer_token':token}, 
              json={"name":  "Питон", "photo": "https://dolnikov.ru/pokemons/albums/346.png"} )

print(add_pokemon_response.text)

add_pokemon_name_response=requests.put('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type':'application/json', 'trainer_token':token}, 
              json={"pokemon_id":'6082', "name":"Альфа", "photo": "https://dolnikov.ru/pokemons/albums/613.png"} )

print(add_pokemon_name_response.text)

add_pokemon_ball_response=requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers={'Content-Type':'application/json', 'trainer_token':token}, 
              json={"pokemon_id":'6082'} )

print(add_pokemon_ball_response.text)



 