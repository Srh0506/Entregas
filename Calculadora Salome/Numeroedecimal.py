class NumeroDecimal:
    def __init__(self, valor):
        # Validación de número decimal
        try:
            self.valor = float(valor)  # Si no es convertible a float, generará ValueError
        except ValueError:
            raise ValueError(f"El valor '{valor}' no es un número decimal válido.")
    
    def sumar(self, otro_numero):
        return self.valor + otro_numero.valor

    def restar(self, otro_numero):
        return self.valor - otro_numero.valor
