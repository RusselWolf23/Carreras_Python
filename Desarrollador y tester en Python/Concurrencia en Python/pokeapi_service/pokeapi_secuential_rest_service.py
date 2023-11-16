from typing import List

import requests
from requests import RequestException

from pokeapi_service.pokeapi_rest_service import PokeAPIRestService
from pokemon import Pokemon


class PokeAPISecuentialRestService(PokeAPIRestService):

    def get_by_names(self, names: List[str]) -> List[Pokemon]:
        pokemons = []
        for name in names:
            try:
                response = requests.get(self.BASE_API_URL + name)
                response.raise_for_status()
                pokemon_json = response.json()
            except RequestException:
                continue

            pokemons.append(Pokemon(id=pokemon_json['id'], nombre=pokemon_json['name'], tipos=[tipo['type']['name'] for tipo in pokemon_json['types']]))

        return pokemons
