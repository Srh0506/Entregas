# pokemonSorter.py
class PokemonSorter:
    def __init__(self, data):
        self.data = data

    def sort(self, strategy, col, ascending=True):
        """
        Ordena usando el algoritmo dado (strategy) y columna numérica.
        """
        sorted_data = strategy.sort(self.data, col, ascending)
        return sorted_data
