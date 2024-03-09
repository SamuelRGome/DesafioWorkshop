from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'.lower()]
        pokemon = pokemon.replace(' ', '%20')
        url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
        url_pokeapi.add_header('user-Agent','charmander')

        source = urllib.request.urlopen(url_pokeapi).read()

        list_of_data = json.loads(source)

        data = {
            "numero": str(list_of_data['id']),
            "nome": str(list_of_data['name']).capitalize(),
            "altura": str(list_of_data['height']),
            "peso": str(list_of_data['weight']),
            "sprite": str(list_of_data['sprites']['front_default']),
        }
        print(data)
    else:
        data = {}
    return render(request, 'main/index.html', 'Pokelib\models.py', data)