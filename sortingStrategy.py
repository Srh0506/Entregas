# SortingStrategy.py
from typing import List, Dict
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[Dict], key: str) -> List[Dict]:
        """Ordena y devuelve una nueva lista ordenada según la clave 'key'."""
        pass
