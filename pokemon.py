import requests

url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

# Dosyayı aç
pokemon_dosyası = open("pokemon_dosyası.txt", "w")
pokemon_dosyası.write(url + "\n")  # URL'yi yaz

for offset in range(0, 1000, 100):
    params['offset'] = offset
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()

        for item in data['results']:
            pokemon_dosyası.write(item['name'] + "\n")
            print(item['name'])

pokemon_dosyası.close()