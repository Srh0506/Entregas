# ApiRequest.py
import requests

class ApiRequest:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon?limit=20"

    def fetch_data(self):
        """
        Obtiene una lista de Pokémon con estadísticas numéricas: hp, attack y defense.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            results = response.json()["results"]

            pokemon_list = []
            for p in results:
                details = requests.get(p["url"]).json()
                stats = {s["stat"]["name"]: s["base_stat"] for s in details["stats"]}
                pokemon_list.append({
                    "hp": stats.get("hp", 0),
                    "attack": stats.get("attack", 0),
                    "defense": stats.get("defense", 0)
                })
            return pokemon_list
        except Exception as e:
            raise Exception(f"Error al obtener Pokémon: {e}")

if __name__ == "__main__":
    api = ApiRequest()
    data = api.fetch_data()
    print("Primeros 5 Pokémon:")
