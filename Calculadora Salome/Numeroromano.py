class NumeroRomano:
    romanos = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    def __init__(self, valor):
        # Validación de número romano
        if not self.es_romano_valido(valor):
            raise ValueError(f"El valor '{valor}' no es un número romano válido.")
        self.valor = valor
    
    def es_romano_valido(self, valor):
        # Validar que solo contenga símbolos romanos válidos
        for c in valor:
            if c not in self.romanos:
                return False
        return True
    
    def sumar(self, otro_numero):
        # Implementación de suma para números romanos
        pass

    def restar(self, otro_numero):
        # Implementación de resta para números romanos
        pass
